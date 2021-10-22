<template>
    <div class="modal-content">
        <div class="modal-header">
            <h3 class="modal-title">Cambio de contraseña</h3>
            <button type="button" @click="cerrar" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true"></span>
            </button>
        </div>
        <div class="modal-body">
            <form class="mt-3 info_personal">
                <fieldset>
                    <div v-if="!id_edicion" class="form-group mb-3">
                        <label for="pw" class="form-label mb-0">Contraseña actual</label>
                        <input type="password" class="form-control" v-model="password" id="pw" placeholder="Contraseña actual" />
                    </div>
                    <div class="form-group">
                        <label for="new_pw" class="form-label mb-0">Contraseña nueva</label>
                        <input type="password" class="form-control" v-model="new_password" id="new_pw" placeholder="Contraseña nueva" />
                    </div>
                    <div class="form-group mt-3">
                        <label for="re_pw" class="form-label mb-0">Confirmar contraseña</label>
                        <input type="password" class="form-control" v-model="re_password" id="re_pw" placeholder="Confirmar contraseña" />
                    </div>
                </fieldset>
            </form>

        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-success" @click="actualizarPassword">Cambiar contraseña</button>
            <button type="button" class="btn btn-danger" @click="cerrar">Cancelar</button>
        </div>
    </div>
</template>

<script>
import { actualizarPassword } from '../../services/usuarios.service';
export default {
    name: "ModalPassword",
    data() {
        return {
            password: null,
            new_password: null,
            re_password: null
        }
    },
    computed: {
        id_edicion() {
            return this.$store.state.modal.id_edicion;
        },
    },
    methods: {
        async actualizarPassword() {
            this.$store.dispatch('showLoading');
            const data = {
                password: this.password,
                new_password: this.new_password,
                re_password: this.re_password,
            }
            try {
                const result = await actualizarPassword(this.id_edicion ? this.id_edicion : null, JSON.stringify(data));
                this.$store.dispatch('hideLoading');
                if(!result.error) {
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
