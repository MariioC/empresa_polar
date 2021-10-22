<template>
    <div class="modal-content">
        <div class="modal-header">
            <h3 class="modal-title">Dependencia</h3>
            <button type="button" @click="cerrar" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true"></span>
            </button>
        </div>
        <div class="modal-body">
            <form class="mt-3 info_personal">
                <fieldset>
                    <div class="form-group">
                        <label for="dependencia" class="form-label mb-0">Nombre dependencia</label>
                        <input type="text" class="form-control" v-model="dependencia.nombre_dependencia" id="dependencia" placeholder="Nombre dependencia" />
                    </div>
                    <div class="form-group mt-3 ">
                        <button v-if="!agregar_cargo" type="button" class="btn btn-info mx-auto d-block mb-2" @click="mostrarFormCargo">Agregar cargos</button>
                        <button v-else type="button" class="btn btn-danger mx-auto d-block mb-2" @click="mostrarFormCargo">Cerrar cargos</button>
                        <form class="border border-1 border-muted p-4 animated fadeIn" :class="{ 'd-none': !agregar_cargo}">
                            <div class="form-group">
                                <label for="cargo" class="form-label mb-0">Nombre cargo</label>
                                <input type="text" class="form-control" v-model="cargo.nombre_cargo" placeholder="Nombre del cargo" />
                            </div>
                            <div class="form-group mt-3">
                                <label for="salario" class="form-label mb-0">Salario</label>
                                <div class="input-group">
                                <span class="input-group-text">$</span>
                                    <input type="text" class="form-control" v-model="cargo.salario" placeholder="Salario">
                                </div>
                            </div>
                            <button v-if="cargo.id_cargo" type="button" class="btn btn-success mx-auto d-block mt-3" @click.prevent="actualizarCargo">Actualizar cargo</button>
                            <button v-else type="button" class="btn btn-success mx-auto d-block mt-3" @click.prevent="agregarCargo">Agregar</button>
                        </form>
                        <legend class="text-center fw-bolder mt-3">Cargos</legend>
                    </div>
                    <div class="form-group mt-3">
                        <table class="table table-hover table-striped table-responsive text-center">
                            <thead>
                                <tr>
                                    <th class="fw-bold" scope="col">Cargo</th>
                                    <th class="fw-bold" scope="col">Salario</th>
                                    <th class="fw-bold" scope="col">Editar</th>
                                    <th class="fw-bold" scope="col">Eliminar</th>
                                </tr>
                            </thead>
                            <tbody>
                                <template v-if="cargos.length">
                                    <tr v-for="(cargo, index) in cargos" :key="index">
                                        <td scope="row">{{ cargo.nombre_cargo }}</td>
                                        <td>{{ cargo.salario }}</td>
                                        <td v-if="cargo.id_cargo">
                                            <button type="button" class="btn btn-primary hint--top" aria-label="Editar cargo" @click="editarCargo(cargo.id_cargo)">
                                                <i class="fas fa-pencil-alt"></i>
                                            </button>
                                        </td>
                                        <td v-else></td>
                                        <td v-if="cargo.id_cargo">
                                            <button type="button" class="btn btn-danger hint--top" aria-label="Eliminar cargo" @click="alertaEliminarCargo(cargo.id_cargo)">
                                                <i class="fas fa-trash"></i>
                                            </button>
                                        </td>
                                        <td v-else>
                                            <button type="button" class="btn btn-info hint--top" aria-label="Eliminar cargo" @click="quitarCargo(cargo.nombre_cargo)">
                                                <i class="fas fa-trash"></i>
                                            </button>
                                        </td>
                                    </tr>
                                </template>
                                <template v-else>
                                    <tr>
                                        <td colspan="4" class="text-center text-danger fw-bold">Aún no se han agregado cargos</td>
                                    </tr>
                                </template>
                            </tbody>
                        </table>
                    </div>
                </fieldset>
            </form>

        </div>
        <div class="modal-footer">
            <button v-if="id_edicion && edicion_dependencia" type="button" class="btn btn-success" @click="actualizarDependencia">Actualizar depencia</button>
            <button v-else type="button" class="btn btn-success" @click="crearDependencia">Crear depencia</button>
            <button type="button" class="btn btn-danger" @click="cerrar">Cancelar</button>
        </div>
    </div>
</template>

<script>
import { crearDependencia, actualizarDependencia, eliminarCargo } from '../../services/dependencias.service';
export default {
    name: 'ModalDependencia',
    data() {
        return {
            agregar_cargo: false,
            dependencia: {
                nombre_dependencia: null
            },
            cargos: [],
            cargo: {
                nombre_cargo: null,
                salario: null
            }
        }
    },
    computed: {
        id_edicion() {
            return this.$store.state.modal.id_edicion;
        },
        dependencias() {
            if(this.id_edicion)
                return this.$store.state.dependencias.dependencias;
            return false
        },
        edicion_dependencia() {
            if(this.dependencias && this.id_edicion)
                return this.dependencias.filter(d => d.dependencia.id_dependencia == this.id_edicion)[0]
            return false
        },
    },
    created() {
        if(this.id_edicion && this.edicion_dependencia) {
            this.dependencia = JSON.parse(JSON.stringify(this.edicion_dependencia.dependencia))
            this.cargos = JSON.parse(JSON.stringify(this.edicion_dependencia.cargos))
        }
    },
    methods: {
        mostrarFormCargo() {
            this.agregar_cargo = !this.agregar_cargo;
        },
        agregarCargo() {
            if(this.cargo.nombre_cargo && this.cargo.salario) {
                this.cargos.unshift(this.cargo)
                this.cargo = {
                    nombre_cargo: null,
                    salario: null
                }
            } else {
                this.$store.dispatch('showError', 'Debe completar todos los campos para agregar un cargo')
            }
        },
        quitarCargo(nombre_cargo) {
            this.cargos = this.cargos.filter(c => c.nombre_cargo != nombre_cargo);
        },
        async crearDependencia() {
            this.$store.dispatch('showLoading');
            const dependencia = {
                dependencia: this.dependencia,
                cargos: this.cargos
            } 
            try {
                const result = await crearDependencia(JSON.stringify(dependencia));
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    const dependencias = JSON.parse(JSON.stringify(this.$store.state.dependencias.dependencias));
                    dependencias.unshift(result.dependencia);

                    this.$store.dispatch('showSuccess', result.mensaje);
                    this.$store.dispatch('setDependencias', dependencias);

                    this.cerrar();
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        async actualizarDependencia() {
            this.$store.dispatch('showLoading');
            const dependencia = {
                dependencia: this.dependencia,
                cargos: this.cargos
            }
            try {
                const result = await actualizarDependencia(JSON.stringify(dependencia));
                this.$store.dispatch('hideLoading');
                if(!result.error) {

                    const { dependencia : dependencia_actualizada } = result.dependencia;

                    const dependencias = JSON.parse(JSON.stringify(this.$store.state.dependencias.dependencias));
                    
                    dependencias[dependencias.findIndex(d => d.dependencia.id_dependencia == dependencia_actualizada.id_dependencia)] = result.dependencia;

                    this.$store.dispatch('showSuccess', result.mensaje);
                    this.$store.dispatch('setDependencias', dependencias);

                    this.cerrar();
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        editarCargo(id_cargo) {
            this.agregar_cargo = true;
            this.cargo = this.cargos.filter(c => c.id_cargo == id_cargo)[0]
        },
        actualizarCargo() {
            this.cargo = {
                nombre_cargo: null,
                salario: null
            }
        },
        alertaEliminarCargo(id_cargo) {
            this.$swal.fire({
                title: '¿Eliminar cargo?',
                text: "Se eliminará el cargo deseado en esta dependencia",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Eliminar',
                cancelButtonText: 'Cancelar',
                reverseButtons: true
            }).then((result) => {
                if (result.isConfirmed) {
                    this.eliminarCargo(id_cargo);
                }
            });
        },
        async eliminarCargo(id_cargo){
            this.$store.dispatch('showLoading');
            try {
                const result = await eliminarCargo(id_cargo);
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    const cargos = JSON.parse(JSON.stringify(this.cargos));
                    const indexEliminado = cargos.findIndex(c => c.id_cargo == id_cargo);
                    cargos.splice(indexEliminado, 1);

                    this.cargos = cargos;
                    
                    this.$store.dispatch('showSuccess', result.mensaje);
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        cerrar() {
            this.$store.dispatch("closeModal");
        },
    },
};
</script>
