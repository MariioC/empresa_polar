<template>
    <div class="modal-content">
        <div class="modal-header">
            <h3 class="modal-title">Información de usuario</h3>
            <button type="button" @click="cerrar" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true"></span>
            </button>
        </div>
        <div class="modal-body">
            <div v-if="(rol == 'A' || rol == 'SA') && !id_edicion">
                <p class="text-center fw-bolder text-muted">Al registrar un usuario, la contraseña sera su mismo número de documento</p>
            </div>
            <div v-if="rol == 'A' || rol == 'SA'" class="btn-group d-flex justify-content-center" role="group" aria-label="Basic example">
                <button type="button" class="btn btn-outline-info" :class="{ 'active' : informacion_personal }" @click="toggleInformacion('personal')">Información personal</button>
                <button type="button" class="btn btn-outline-info" :class="{ 'active' : informacion_laboral }" @click="toggleInformacion('laboral')">Información laboral</button>
            </div>
            <form class="mt-3 info_personal animated fadeIn fast" :class="{ 'd-none' : !informacion_personal }">
                <fieldset>
                    <div class="form-group">
                        <label for="nombres" class="form-label mb-0">Nombres</label>
                        <input type="text" class="form-control" v-model="info_personal.nombres" id="nombres" placeholder="Nombres" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="apellidos" class="form-label mb-0">Apellidos</label>
                        <input type="text" class="form-control" v-model="info_personal.apellidos" id="apellidos" placeholder="Apellidos" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="documento" class="form-label mb-0">N° de documento</label>
                        <input type="text" class="form-control" v-model="info_personal.documento" id="documento" placeholder="N° de documento" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="fecha_nacimiento" class="form-label mb-0">Fecha de nacimiento</label>
                        <input type="date" class="form-control" v-model="info_personal.fecha_nacimiento" id="fecha_nacimiento" placeholder="Fecha de nacimiento" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="genero" class="form-label mb-0">Género</label>
                        <select class="form-select" v-model="info_personal.genero" id="genero">
                            <option value="">Seleccione...</option>
                            <option value="Masculino">Masculino</option>
                            <option value="Femenino">Femenino</option>               
                            <option value="Otro">Otro</option>               
                        </select>
                    </div>
                    <div class="form-group mt-3">
                        <label for="correo" class="form-label mb-0">Correo</label>
                        <input type="text" class="form-control" v-model="info_personal.correo" id="correo" placeholder="Correo" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="celular" class="form-label mb-0">Celular</label>
                        <input type="text" class="form-control" v-model="info_personal.celular" id="celular" placeholder="Celular" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="direccion" class="form-label mb-0">Dirección</label>
                        <input type="text" class="form-control" v-model="info_personal.direccion" id="direccion" placeholder="Dirección" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="ciudad" class="form-label mb-0">Ciudad</label>
                        <input type="text" class="form-control" v-model="info_personal.ciudad" id="ciudad" placeholder="Ciudad" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="estado" class="form-label mb-0">Estado civil</label>
                        <select class="form-select" v-model="info_personal.estado_civil" id="estado_civil">
                            <option value="">Seleccione...</option>
                            <option value="Soltero(a)">Soltero(a)</option>
                            <option value="Casado(a)">Casado(a)</option>               
                            <option value="Divorciado(a)">Divorciado(a)</option>               
                            <option value="Viudo(a)">Viudo(a)</option>               
                        </select>
                    </div>
                    <div v-if="rol == 'SA'" class="form-group mt-3">
                        <label for="estado" class="form-label mb-0">Rol</label>
                        <select class="form-select" v-model="info_personal.rol" id="rol">
                            <option value="">Seleccione...</option>
                            <option value="SA">Superadministrador</option>
                            <option value="A">Administrador</option>               
                            <option value="E">Empleado</option>               
                        </select>
                    </div>
                </fieldset>
            </form>

            <form class="mt-3 info_laboral animated fadeIn fast" :class="{ 'd-none' : !informacion_laboral }">
                <fieldset>
                    <div class="form-group">
                        <label for="dependencia" class="form-label mb-0">Dependencia</label>
                        <select class="form-select" v-model="info_laboral.id_dependencia" id="dependencia">
                            <option value="">Seleccione...</option>
                            <option v-for="(dependencia, index) in dependencias" :key="index" :value="dependencia.dependencia.id_dependencia">{{ dependencia.dependencia.nombre_dependencia }}</option>
                        </select>
                    </div>
                    <div class="form-group mt-3">
                        <label for="cargo" class="form-label mb-0">Cargo</label>
                        <select class="form-select" v-model="info_laboral.id_cargo" id="id_cargo">
                            <option value="">Seleccione...</option>
                            <template v-if="cargos_dependencia">                                    
                                <option v-for="(cargo, index) in cargos_dependencia" :key="index" :value="cargo.id_cargo">{{ cargo.nombre_cargo }}</option>
                            </template>
                        </select>
                    </div>
                    <div class="form-group mt-3">
                        <label for="tipo_contrato" class="form-label mb-0">Tipo de contrato</label>
                        <select class="form-select" v-model="info_laboral.tipo_contrato" id="tipo_contrato">
                            <option value="">Seleccione...</option>
                            <option value="Termino fijo">Termino fijo</option>
                            <option value="Termino indefinido">Termino indefinido</option>               
                            <option value="Prestación de servicios">Prestación de servicios</option>               
                        </select>
                    </div>
                    <div class="form-group mt-3">
                        <label for="salario" class="form-label mb-0">Salario</label>
                        <div class="input-group">
                        <span class="input-group-text">$</span>
                            <input type="text" class="form-control" id="salario" v-model="salario" disabled>
                        </div>
                    </div>
                    <div class="form-group mt-3">
                        <label for="fecha_ingreso" class="form-label mb-0">Fecha de ingreso</label>
                        <input type="date" class="form-control" v-model="info_laboral.fecha_ingreso" id="fecha_ingreso" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="fecha_terminacion" class="form-label mb-0">Fecha de terminación</label>
                        <input type="date" class="form-control" v-model="info_laboral.fecha_terminacion" id="fecha_terminacion" />
                    </div>
                </fieldset>
            </form>
        </div>
        <div class="modal-footer">
            <button v-if="id_edicion" type="button" class="btn btn-success" @click.prevent="actualizarUsuario">Actualizar usuario</button>
            <button v-else type="button" class="btn btn-success" @click.prevent="registrarUsuario">Registrar usuario</button>
            <button type="button" class="btn btn-danger" @click="cerrar">Cancelar</button>
        </div>
    </div>
</template>

<script>
import { obtenerDependencias } from '../../services/dependencias.service';
import { registrarUsuario, actualizarUsuario } from '../../services/usuarios.service';
export default {
    name: "ModalUsuario",
    data() {
        return {
            informacion_personal: true,
            informacion_laboral: false,
            info_personal: {
                nombres: null,
                apellidos: null,
                documento: null,
                fecha_nacimiento: null,
                genero: "",
                correo: null,
                celular: null,
                direccion: null,
                ciudad: null,
                estado_civil: "",
                rol: "",
                password: ""
            },
            info_laboral: {
                id_dependencia: "",
                id_cargo: "",
                tipo_contrato: "",
                fecha_ingreso: null,
                fecha_terminacion: null
            }
        };
    },
    computed: {
        id_edicion() {
            return this.$store.state.modal.id_edicion;
        },
        usuario() {
            return this.$store.state.usuario?.info_personal;
        },
        rol() {
            return this.usuario.rol;
        },
        dependencias() {
            return JSON.parse(JSON.stringify(this.$store.state.dependencias.dependencias));
        },
        cargos_dependencia() {
            if(this.info_laboral.id_dependencia){
                if (this.dependencias.length) {
                    const cargos = this.dependencias.filter(d => d.dependencia.id_dependencia == this.info_laboral.id_dependencia);
                    return cargos.length ? cargos[0]['cargos'] : false;
                }
                return false;
            }
            
            return false;
        },
        salario() {
            if(this.info_laboral.id_cargo){
                if (this.cargos_dependencia.length) {
                    const salario = this.cargos_dependencia.filter(c => c.id_cargo == this.info_laboral.id_cargo)
                    return salario.length ? salario[0]['salario'] : 0;
                }
                return false;
            }
            return 0;
        }
    },
    created() {
        if(this.id_edicion) {
            if(this.id_edicion == this.usuario.id_usuario) {
                this.info_personal = JSON.parse(JSON.stringify(this.$store.state.usuario?.info_personal));
                if(this.$store.state.usuario?.info_laboral) {
                    this.info_laboral = JSON.parse(JSON.stringify(this.$store.state.usuario?.info_laboral));
                }
            } else{
                // HAGO LA PETICION DE LOS DAATOS DEL USUARIO
                this.obtenerUsuarioState();
            }
        }

        if(!this.dependencias.length)
            this.getDependencias();
    },
    methods: {
        toggleInformacion(info) {
            if(info == 'personal') {
                this.informacion_personal = true;
                this.informacion_laboral = false;
            } else {
                this.informacion_personal = false;
                this.informacion_laboral = true;
            }
        },
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
        async registrarUsuario() {
            this.$store.dispatch('showLoading');
            const usuario = {
                info_personal: this.info_personal,
                info_laboral: this.info_laboral
            }
            try {
                const result = await registrarUsuario(JSON.stringify(usuario));
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    this.$store.dispatch('showSuccess', result.mensaje);

                    const usuarios = JSON.parse(JSON.stringify(this.$store.state.usuarios.usuarios));
                    if( usuarios.length ) {
                        usuarios.unshift(result.usuario)
                        this.$store.dispatch('setUsuarios', usuarios)
                    }

                    this.cerrar();

                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        async actualizarUsuario() {
            this.$store.dispatch('showLoading');
            const usuario = {
                info_personal: this.info_personal,
                info_laboral: this.info_laboral
            }
            try {
                const result = await actualizarUsuario(this.id_edicion == this.usuario.id_usuario ? null : this.id_edicion, JSON.stringify(usuario));
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    this.$store.dispatch('showSuccess', result.mensaje);

                    const usuarios = JSON.parse(JSON.stringify(this.$store.state.usuarios.usuarios));
                    const idexActulizado = usuarios.findIndex(u => u.info_personal.id_usuario == result.usuario.info_personal.id_usuario)

                    usuarios[idexActulizado] = result.usuario;
                    
                    this.$store.dispatch('setUsuarios', usuarios)

                    if(this.id_edicion == this.usuario.id_usuario)
                        this.$store.dispatch('setUsuario', result.usuario);

                    this.cerrar();
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        obtenerUsuarioState() {
            const usuarios = JSON.parse(JSON.stringify(this.$store.state.usuarios.usuarios));
            const usuario = usuarios.filter(u => u.info_personal.id_usuario == this.id_edicion)[0];
            
            this.info_personal = JSON.parse(JSON.stringify(usuario?.info_personal));
            if(usuario?.info_laboral) {
                this.info_laboral = JSON.parse(JSON.stringify(usuario?.info_laboral));
            }
        },
        cerrar() {
            this.$store.dispatch("closeModal");
        },
    },
};
</script>
