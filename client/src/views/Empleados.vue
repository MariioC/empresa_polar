<template>
    <div class="usuarios animated fadeIn fast">
        <h1 class="text-center">Empleados</h1>
        <p class="text-center px-3 mt-3">
            A continuación, puede gestionar todos los usuarios registrados en la empresa, registrar usuarios, actualizar información de usuarios, eliminar usuarios y ver las retroalimentaciones de cada usuario.
        </p>

        <div class="row mb-4">
            <h3 class="text-center">Busqueda de usuarios</h3>
            <!-- <p class="text-center">A continuación puede consultar un usuario por los siguientes terminos: Nombre, Usuario, Documento o Dependencia</p> -->
            <div class="row col-md-5 col-10 mx-auto justify-content-center">
                <div class="input-group">
                    <input type="text" class="form-control" v-model="query" @keyup="delayBuscarUsuarios" placeholder="Ingrese: Nombre, Usuario, Documento o Dependencia">
                    <button type="button" class="btn btn-primary" @click="buscarUsuarios">Buscar</button>
                </div>
            </div>
        </div>
        <hr class="divider">
        
        
        <div>
            <button type="button" @click="modalUsuario(null)" class="btn btn-lg btn-success d-block mx-auto my-2">
                <i class="fas fa-user mx-1"></i> Crear Usuario
            </button>
            <h3 class="text-center my-3">Usuarios / Empleados</h3>

            <button type="button" @click="obtenerUsuarios" class="btn btn-primary btn-sm mb-2 d-block mx-auto hint--bottom" aria-label="Cargar usuarios"><i class="fas fa-sync-alt mx-1"></i> Cargar</button>

            <div class="row overflow-auto">
                <table class="table table-hover table-striped table-responsive text-center">
                    <thead>
                        <tr>
                            <th class="fw-bold" scope="col">Nombre</th>
                            <th class="fw-bold" scope="col">Documento</th>
                            <th class="fw-bold" scope="col">Dependencia</th>
                            <th class="fw-bold" scope="col">Cargo</th>
                            <th class="fw-bold" scope="col">Salario</th>
                            <th class="fw-bold" scope="col">Editar</th>
                            <th class="fw-bold" scope="col">Eliminar</th>
                            <th class="fw-bold" scope="col">Contraseña</th>
                            <th class="fw-bold" scope="col">Retroalimentaciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <template v-if="usuarios && usuarios.length">
                            <tr v-for="(usuario, index) in usuarios" :key="index">
                                <td scope="row">{{ usuario.info_personal.nombres }}</td>
                                <td>{{ usuario.info_personal.documento }}</td>
                                <td v-if="usuario.info_laboral">{{ usuario.info_laboral.nombre_dependencia }}</td>
                                <td v-else class="text-danger">Sin asignar</td>
                                <td v-if="usuario.info_laboral">{{  usuario.info_laboral.nombre_cargo }}</td>
                                <td v-else class="text-danger">Sin asignar</td>
                                <td v-if="usuario.info_laboral">${{ usuario.info_laboral.salario }}</td>
                                <td v-else class="text-danger">$0</td>
                                <td>
                                    <button type="button" class="btn btn-primary hint--left" aria-label="Editar usuario" @click="modalUsuario(usuario.info_personal.id_usuario)">
                                        <i class="fas fa-pencil-alt"></i>
                                    </button>
                                </td>
                                <td>
                                    <button type="button" class="btn btn-danger hint--left" aria-label="Eliminar usuario" @click="alertaEliminarUsuario((usuario.info_personal.id_usuario))">
                                        <i class="fas fa-trash"></i>
                                    </button>
                                </td>
                                <td>
                                    <button type="button" class="btn btn-info hint--left" aria-label="Cambiar contraseña de usuario" @click="modalPassword((usuario.info_personal.id_usuario))">
                                        <i class="fas fa-lock"></i>
                                    </button>
                                </td>
                                <td>
                                    <RouterLink :to="{ name: 'Retroalimentacion', params:{ id_usuario: usuario.info_personal.id_usuario } }" type="button" class="btn btn-success hint--left" aria-label="Ver retroalimentaciones del usuario">
                                        <i class="fas fa-comments mx-1"></i> Retroalimentaciones
                                    </RouterLink>
                                </td>
                            </tr>
                        </template>
                        <template v-else>
                            <tr>
                                <td v-if="!query" colspan="9" class="text-center fw-bolder text-danger">Aún no hay usuarios registrados</td>
                                <td v-else colspan="9" class="text-center fw-bolder text-danger">No se ha encontrado nigún usuario</td>
                            </tr>
                        </template>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import { buscarUsuarios, eliminarUsuario, obtenerUsuarios } from '../services/usuarios.service';
export default {
    name: "Empleados",
    data() {
        return {
            query: null,
            timer: null
        }
    },
    computed: {
        usuarios() {
            return this.$store.state.usuarios.usuarios;
        }
    },
    created() {
        if(!this.usuarios.length)
            this.obtenerUsuarios()
    },
    methods: {
        async obtenerUsuarios() {
            this.query = null;
            this.$store.dispatch('showLoading');
            try {
                const result = await obtenerUsuarios();
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    this.$store.dispatch('setUsuarios', result.usuarios)
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        delayBuscarUsuarios() {
            if (this.timer) {
                clearTimeout(this.timer);
                this.timer = null;
            }
            this.timer = setTimeout(() => {
                this.buscarUsuarios()
            }, 800);
        },
        async buscarUsuarios() {
            if (this.query) {
                if(this.query.length > 2) {
                    this.$store.dispatch('showLoading');
                    try {
                        const result = await buscarUsuarios(this.query);
                        this.$store.dispatch('hideLoading');
                        if(!result.error) {
                            this.$store.dispatch('setUsuarios', result.resultados)
                        } else {
                            this.$store.dispatch('showError', result.error);
                        }
                    } catch(error) {
                        this.$store.dispatch('showError');
                        console.error(error);
                    }
                }
            } else {
                this.obtenerUsuarios();
            }
        },
        modalUsuario(id_usuario) {
            this.$store.dispatch('showModal', { show_modal: 'ModalUsuario', id_edicion: id_usuario});
        },
        modalPassword(id_usuario) {
            this.$store.dispatch('showModal', { show_modal: 'ModalPassword', id_edicion: id_usuario });
        },
        alertaEliminarUsuario(id_usuario) {
            this.$swal.fire({
                title: '¿Seguro que desea eliminar el usuario?',
                text: "Se eliminará el usuario y toda la información relacionada a él",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Eliminar',
                cancelButtonText: 'Cancelar',
                reverseButtons: true
            }).then((result) => {
                if (result.isConfirmed) {
                    this.eliminarUsuario(id_usuario);
                }
            });
        },
        async eliminarUsuario(id_usuario) {
            this.$store.dispatch('showLoading');
            try {
                const result = await eliminarUsuario(id_usuario);
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    const usuarios = JSON.parse(JSON.stringify(this.usuarios));
                    const indexEliminado = usuarios.findIndex(u => u.info_personal.id_usuario == id_usuario);
                    usuarios.splice(indexEliminado, 1);

                    this.$store.dispatch('setUsuarios', usuarios);

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
