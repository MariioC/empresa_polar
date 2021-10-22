<template>
    <div class="modal-content">
        <div class="modal-header">
            <h3 class="modal-title">Olvidé mi contraseña</h3>
            <button type="button" @click="cerrar" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true"></span>
            </button>
        </div>
        <div class="modal-body">
            <form class="mt-3 info_personal">
                <p class="text-center small text-muted mb-3">Se enviará la información necesaria al correo registrado en la empresa para que pueda restablecer su contraseña</p>
                <fieldset>
                    <div class="form-group">
                        <label for="usuario" class="form-label mb-0">Documento o correo:</label>
                        <input type="text" class="form-control" v-model="usuario" id="usuario" placeholder="Digite su documento o correo registrado" />
                    </div>
                </fieldset>
            </form>

        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-success" @click="restablecerPassword">Restablecer contraseña</button>
            <button type="button" class="btn btn-danger" @click="cerrar">Cancelar</button>
        </div>
    </div>
</template>

<script>
import { restablecerPassword } from '../../services/usuarios.service';
export default {
    name: "ModalPassword",
    data() {
        return {
            usuario: null
        }
    },
    methods: {
        async restablecerPassword() {
            this.usuario = this.usuario.trim();
            
            if(!this.usuario)
                return;

            this.$store.dispatch('showLoading');

            try {
                const result = await restablecerPassword(this.usuario);
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
