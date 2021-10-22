<template>
    <div class="contacto animated fadeIn fast">
        <div class="container my-5">
            <div class="jumbotron">
                <h1 class="display-4 text-center">
                    <RouterLink :to="{ name: 'Home' }" class="text-decoration-none text-dark">EMPRESA POLAR</RouterLink>
                </h1>
                <p class="lead text-center">Conoce nuestros asesores...</p>
                <div class="row justify-content-center">
                    <div class="card border-primary border-3 mb-3 col-md-4 mx-2">
                        <div class="card-header fw-bolder text-center bg-primary text-white" style="font-size: 1.7rem;">Mario Carreño</div>
                        <div class="card-body">
                            <h4 class="card-title text-center">Programador Backend</h4>
                            <p class="card-text text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi et est deserunt corrupti. Debitis, deleniti?</p>
                        </div>
                    </div>
                    <div class="card border-danger border-3 mb-3 col-md-4 mx-2">
                        <div class="card-header fw-bolder text-center bg-danger text-white" style="font-size: 1.7rem;">José Ballesteros</div>
                        <div class="card-body">
                            <h4 class="card-title text-center">Programador Frontend</h4>
                            <p class="card-text text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi et est deserunt corrupti. Debitis, deleniti?</p>
                        </div>
                    </div>
                    <div class="card border-danger border-3 mb-3 col-md-4 mx-2">
                        <div class="card-header fw-bolder text-center bg-danger text-white" style="font-size: 1.7rem;">Byron Agudelo</div>
                        <div class="card-body">
                            <h4 class="card-title text-center">Analista</h4>
                            <p class="card-text text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi et est deserunt corrupti. Debitis, deleniti?</p>
                        </div>
                    </div>
                    <div class="card border-primary border-3 mb-3 col-md-4 mx-2">
                        <div class="card-header fw-bolder text-center bg-primary text-white" style="font-size: 1.7rem;">Carlos Eduardo</div>
                        <div class="card-body">
                            <h4 class="card-title text-center">Diseñador</h4>
                            <p class="card-text text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi et est deserunt corrupti. Debitis, deleniti?</p>
                        </div>
                    </div>
                    <div class="card border-danger border-3 mb-3 col-md-4 mx-2">
                        <div class="card-header fw-bolder text-center bg-danger text-white" style="font-size: 1.7rem;">César Santana</div>
                        <div class="card-body">
                            <h4 class="card-title text-center">Diseñador</h4>
                            <p class="card-text text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi et est deserunt corrupti. Debitis, deleniti?</p>
                        </div>
                    </div>
                </div>
                <hr class="divider my-2">
                <h1 class="display-6 text-center">Formulario de contacto</h1>
                <p class="text-center">Empresa polar se conecta contigo y por eso ponemos a tu disposición el siguiente formulario de atención al usuario:</p>
                <form class="form_login col-md-5 mx-auto" @submit.prevent="enviarCorreo">
                    <div class="form-group mb-3">
                        <input type="text" name="asunto" class="form-control" v-model="asunto" placeholder="Asunto">
                    </div>
                    <div class="form-group mb-3">
                        <input type="email" name="correo" class="form-control" v-model="correo" placeholder="Escribe aquí tu correo">
                    </div>
                    <div class="form-group col-md-12">
                        <textarea class="form-control mb-3" id="exampleTextarea" rows="3" v-model="mensaje" placeholder="Escriba su mensaje"></textarea>
                    </div>
                    <button type="submit" class="btn btn-success d-block mx-auto"><i class="fas fa-paper-plane mx-1"></i> Enviar mensaje</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { enviarMensajeContacto } from '../services/usuarios.service';
export default {
    name: "Contacto",
    data() {
        return {
            asunto: null,
            correo: null,
            mensaje: null
        }
    },
    methods: {
        async enviarCorreo() {
            const mensaje = {
                asunto: this.asunto,
                correo: this.correo,
                mensaje: this.mensaje
            }
            console.log(mensaje);
            
            this.$store.dispatch('showLoading');
            try {
                const result = await enviarMensajeContacto(JSON.stringify(mensaje));
                this.$store.dispatch('hideLoading');
                if(!result.error) {
                    this.$store.dispatch('showSuccess', result.mensaje)
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
.card-header:first-child {
    border-radius: 0;
}
</style>