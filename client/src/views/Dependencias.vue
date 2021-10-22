<template>
    <div class="usuarios animated fadeIn fast">
        <h1 class="text-center">Dependencias</h1>
        <p class="text-center">A continuación, puede gestionar las dependencias y cargos existentes en la empresa</p>
        <div class="row mb-4">
            <h3 class="text-center">Busqueda de dependencias</h3>
            <div class="row col-md-5 col-10 mx-auto justify-content-center">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="nombre de la dependencia" aria-label="Recipient's username" aria-describedby="button-addon2">
                    <button class="btn btn-primary" type="button" id="button-addon2">Buscar</button>
                </div>
            </div>
        </div>
        <hr class="divider">
            <button type="button" class="btn btn-lg btn-success d-block mx-auto my-2" @click="ModalDependencia(null)">
                <i class="fas fa-cubes mx-1"></i> Crear Dependencia
            </button>
        <div class="row overflow-auto">
            <h3 class="text-center my-3">Dependencias</h3>
            <table class="table table-hover table-striped table-responsive text-center">
                <thead>
                    <tr>
                        <th class="fw-bold" scope="col">Dependencia</th>
                        <th class="fw-bold" scope="col">N° de cargos</th>
                        <th class="fw-bold" scope="col">Editar</th>
                        <th class="fw-bold" scope="col">Eliminar</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(dependencia, index) in dependencias" :key="index">
                        <td scope="row">{{ dependencia.dependencia.nombre_dependencia }}</td>
                        <td>{{ dependencia.cargos.length }}</td>
                        <td>
                            <button type="button" class="btn btn-primary" @click="ModalDependencia(dependencia.dependencia.id_dependencia)">
                                <i class="fas fa-pencil-alt mx-1"></i> Editar
                            </button>
                        </td>
                        <td>
                            <button type="button" class="btn btn-danger" @click="alertaEliminarDependencia(dependencia.dependencia.id_dependencia)">
                                <i class="fas fa-trash mx-1"></i> Eliminar
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import { obtenerDependencias, eliminarDependencia } from '../services/dependencias.service'
export default {
    name: "Dependencias",
    computed: {
        dependencias() {
            return this.$store.state.dependencias.dependencias;
        }
    },
    created() {
        if(!this.dependencias.length)
            this.getDependencias();
    },
    methods: {
        async getDependencias() {
            this.$store.dispatch('showLoading');
            try {
                const result = await obtenerDependencias();
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    this.$store.dispatch('setDependencias', result.dependencias)
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        ModalDependencia(id_edicion) {
            this.$store.dispatch('showModal', { show_modal: 'ModalDependencia', id_edicion });
        },
        alertaEliminarDependencia(id_dependencia) {
            this.$swal.fire({
                title: '¿Eliminar dependencia?',
                text: "Adicionalmente se eliminarán los cargos pertenecientes a la dependencia",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Eliminar',
                cancelButtonText: 'Cancelar',
                reverseButtons: true
            }).then((result) => {
                if (result.isConfirmed) {
                    this.eliminarDependencia(id_dependencia);
                }
            });
        },
        async eliminarDependencia(id_dependencia) {
            this.$store.dispatch('showLoading');
            try {
                const result = await eliminarDependencia(id_dependencia);
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    const dependencias = JSON.parse(JSON.stringify(this.dependencias));
                    const indexEliminada = dependencias.findIndex(d => d.dependencia.id_dependencia == id_dependencia);
                    dependencias.splice(indexEliminada, 1);

                    this.$store.dispatch('setDependencias', dependencias);

                    this.$store.dispatch('showSuccess', result.mensaje);
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        }
    },
};
</script>

<style scoped>
table tr td {
    font-weight: 500;
}
</style>
