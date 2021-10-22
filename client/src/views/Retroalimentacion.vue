<template>
    <div class="retroalimentacion animated fadeIn fast">
        <h1 class="text-center">Retrolimentaciones</h1>
        <p class="text-center" v-if="!id_usuario">
            A continuación, apareceran todas las retroalimentaciones mensuales que se le ha hecho a su desempeño en la empresa
        </p>
        <p class="text-center" v-else>
            A continuación, apareceran todas las retroalimentaciones mensuales que tiene este usuario en la empresa. <br><br>
            Usted puede, crear retrialimentaciones, actualizar retroalimentaciones existentes y eliminar retroalimentaciones para este usuario.
        </p>

        <div v-if="(rol == 'A' || rol == 'SA') && id_usuario" class="container">
            <button  type="button" class="btn btn-lg btn-success d-block mx-auto my-2" @click="ModalRetroalimentacion(null)"><i class="fas fa-comment mx-1"></i> Crear retroalimentación</button>
        </div>

        <hr class="divider">

        <div class="row col-md-10 mx-auto justify-content-center">

            <template v-if="!retroalimentaciones || !retroalimentaciones.length">
                <h3 class="text-center text-danger mt-4">Aún no existen retroalimentaciones</h3>
            </template>
            <template v-else>
                <div v-for="(r, index) in retroalimentaciones" :key="index"
                    class="item_retroalimentacion overflow-hidden list-group-item flex-column align-items-start border-2 d-flex justify-content-between">
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">Retroalimentación - {{ r.fecha_retroalimentacion | formatoFecha('mes') }} <i class="fas fa-comment mx-1"></i></h5>
                        <small class="text-dark fw-bold">Fecha: <i class="fas fa-calendar-alt mx-1"></i> {{ r.fecha_retroalimentacion | formatoFecha }}</small>
                    </div>
                    <p class="my-3">{{ r.retroalimentacion }}</p>
                    <small class="text-dark fw-bolder"><b>Puntuación: </b>{{ r.puntaje }}</small>
                    <div v-if="(rol == 'A' || rol == 'SA') && id_usuario" class="w-100 d-flex justify-content-end">
                        <button type="button" class="btn btn-primary mx-1" @click="ModalRetroalimentacion(r.id_retroalimentacion)">
                            <i class="fas fa-pencil-alt mx-1"></i> Editar
                        </button>
                        <button type="button" class="btn btn-danger mx-1" @click="alertaEliminarRetroalimentacion(r.id_retroalimentacion)">
                            <i class="fas fa-trash mx-1"></i> Eliminar
                        </button>
                    </div>
                </div>
            </template>
        </div>


    </div>
</template>

<script>
import { eliminarRetroalimentacion, obtenerRetroalimentaciones } from '../services/retroalimentaciones.service'
export default {
    name: "Retrolimentacion",
    computed: {
        id_usuario() {
            return this.$route.params.id_usuario ? this.$route.params.id_usuario : false; 
        },
        rol() {
            return this.$store.state.usuario?.info_personal?.rol;
        },
        retroalimentaciones() {
            return this.$store.state.retroalimentaciones.retroalimentaciones;
        }
    },
    watch: {
        id_usuario: function() {
            this.$store.dispatch('setRetroalimentaciones', []);
            this.obtenerRetroalimentaciones();
        }
    },
    created() {
        this.obtenerRetroalimentaciones();
    },
    methods: {
        async obtenerRetroalimentaciones() {
            this.$store.dispatch('showLoading');
            try {
                const result = await obtenerRetroalimentaciones(this.id_usuario);
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    this.$store.dispatch('setRetroalimentaciones', result.retroalimentaciones);
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        ModalRetroalimentacion(id_retroalimentacion) {
            if(id_retroalimentacion)
                this.$store.dispatch('showModal', { show_modal: 'ModalRetroalimentacion', id_edicion: id_retroalimentacion});
            else
                this.$store.dispatch('showModal', { show_modal: 'ModalRetroalimentacion' });
        },
        alertaEliminarRetroalimentacion(id_retroalimentacion) {
            this.$swal.fire({
                title: '¿Eliminar retroalimentación?',
                text: "Esta seguro que desea eliminar la retroalimentación",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Eliminar',
                cancelButtonText: 'Cancelar',
                reverseButtons: true
            }).then((result) => {
                if (result.isConfirmed) {
                    this.eliminarRetroalimentacion(id_retroalimentacion);
                }
            });
        },
        async eliminarRetroalimentacion(id_retroalimentacion) {
            this.$store.dispatch('showLoading');
            try {
                const result = await eliminarRetroalimentacion(id_retroalimentacion);
                this.$store.dispatch('hideLoading');
                if(!result.error) {

                    const retroalimentaciones = JSON.parse(JSON.stringify(this.$store.state.retroalimentaciones.retroalimentaciones))
                    const indexEliminada = retroalimentaciones.findIndex(r => r.id_retroalimentacion == id_retroalimentacion)
                    retroalimentaciones.splice(indexEliminada, 1);

                    this.$store.dispatch('setRetroalimentaciones', retroalimentaciones);

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
.my-3 {
    text-align: justify;
}
.item_retroalimentacion {
    max-width: 48.5%;
    margin: 7px;
    border-radius: 5px;
    border-color: #2fb380;
    background: #2fb3800a;
}
.item_retroalimentacion:nth-child(4n+0),
.item_retroalimentacion:nth-child(4n+1) {
    border-color: #3459e6;
    background: #3458e60a;
    /* border-color: #2fb380!important; */
}
</style>
