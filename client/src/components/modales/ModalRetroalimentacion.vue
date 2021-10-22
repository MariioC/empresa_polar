<template>
    <div class="modal-content">
        <div class="modal-header">
            <h3 class="modal-title">Retroalimentación</h3>
            <button type="button" @click="cerrar" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true"></span>
            </button>
        </div>
        <div class="modal-body">
            <form class="mt-3 info_personal">
                <fieldset>
                    <div v-if="!id_edicion" class="form-group mb-3">
                        <label for="fecha_retroalimentacion" class="form-label mb-0">Fecha de la retroalimentación</label>
                        <input type="date" class="form-control" v-model="retroalimentacion.fecha_retroalimentacion" id="fecha_retroalimentacion" />
                    </div>
                    <div class="form-group">
                        <label for="puntaje" class="form-label mb-0">Puntaje</label>
                        <input type="number" class="form-control" v-model="retroalimentacion.puntaje" id="puntaje" name="tentacles" min="0" max="100">
                    </div>
                    <div class="form-group mt-3">
                        <label for="retroalimentacion" class="form-label mb-0">Retroalimentación</label>
                        <textarea class="form-control" v-model="retroalimentacion.retroalimentacion" id="retroalimentacion" rows="3" placeholder="Retroalimentación"></textarea>
                    </div>
                </fieldset>
            </form>

        </div>
        <div class="modal-footer">
            <button v-if="!id_edicion" type="button" class="btn btn-success" @click="registraRetroalimentacion">Crear retroalimentación</button>
            <button v-else type="button" class="btn btn-success" @click="actualizarRetroalimentacion">Actualizar retroalimentación</button>
            <button type="button" class="btn btn-danger" @click="cerrar">Cancelar</button>
        </div>
    </div>
</template>

<script>
import { actualizarRetroalimentacion, obtenerRetroalimentacion, registraRetroalimentacion } from '../../services/retroalimentaciones.service';
export default {
    name: "ModalRetroalimentacion",
    data() {
        return {
            retroalimentacion: {
                fecha_retroalimentacion: null,
                puntaje: 0,
                retroalimentacion: null
            }
        };
    },
    computed: {
        id_edicion() {
            return this.$store.state.modal.id_edicion;
        },
        id_usuario() {
            return this.$route.params.id_usuario ? this.$route.params.id_usuario : false; 
        },
    },
    created() {
        if(this.id_edicion){
            this.getRetroalimentacion();
        }
    },
    methods: {
        async getRetroalimentacion() {
            this.$store.dispatch('showLoading');
            try {
                const result = await obtenerRetroalimentacion(this.id_edicion);
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    this.retroalimentacion = result.retroalimentacion;
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        async registraRetroalimentacion() {
            this.$store.dispatch('showLoading');
            try {
                const result = await registraRetroalimentacion(this.id_usuario, JSON.stringify(this.retroalimentacion));
                this.$store.dispatch('hideLoading');
                if(!result.error) {

                    const retroalimentaciones = JSON.parse(JSON.stringify(this.$store.state.retroalimentaciones.retroalimentaciones))
                    retroalimentaciones.unshift(result.retroalimentacion);

                    this.$store.dispatch('setRetroalimentaciones', retroalimentaciones);

                    this.$store.dispatch('showSuccess', result.mensaje);

                    this.cerrar();
                } else {
                    this.$store.dispatch('showError', result.error);
                }
            } catch(error) {
                this.$store.dispatch('showError');
                console.error(error);
            }
        },
        async actualizarRetroalimentacion() {
            this.$store.dispatch('showLoading');
            try {
                const result = await actualizarRetroalimentacion(this.id_edicion, JSON.stringify(this.retroalimentacion));
                this.$store.dispatch('hideLoading');
                if(!result.error) {

                    const retroalimentaciones = JSON.parse(JSON.stringify(this.$store.state.retroalimentaciones.retroalimentaciones))
                    const indexActualizada = retroalimentaciones.findIndex(r => r.id_retroalimentacion == this.id_edicion)
                    retroalimentaciones[indexActualizada] = result.retroalimentacion;

                    this.$store.dispatch('setRetroalimentaciones', retroalimentaciones);

                    this.$store.dispatch('showSuccess', result.mensaje);

                    this.cerrar();
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
