<template>
    <div class="login animated fadeIn fast">
        <div class="container">
            <form class="form_login col-md-4 mx-auto mt-5" @submit.prevent="iniciarSesion">
                <h1>Iniciar sesión</h1>
                <div class="form-group mt-4 pb-3">
                    <i class="fas fa-user"></i>
                    <input type="text" name="usuario" v-model="data_login.usuario" class="form-control form-control-lg" :class="{ 'is-invalid': data_empty.usuario }" placeholder="Usuario">
                    <small v-if="data_empty.usuario" class="form-text text-danger">Digite su usuario</small>
                </div>
                <div class="form-group mt-4 pb-3">
                    <i class="fas fa-lock"></i>
                    <input :type="type_password" name="password" v-model="data_login.password" class="form-control form-control-lg" :class="{ 'is-invalid': data_empty.password }" placeholder="Contraseña">
                    <i class="fas ver_password" :class="{'fa-eye' : type_password == 'password', 'fa-eye-slash' : type_password == 'text' }" @click="toggleTypePassword"></i>
                    <small v-if="data_empty.password" class="form-text text-danger">Digite su contraseña</small>
                </div>
                <div class="row mt-4">
                    <button type="submit" class="btn btn-primary btn-lg col-md-6">Iniciar sesión</button>
                    <div class="fw-bold col-md-6 mt-2 text-muted small">
                        <p class="mb-0 text-center lh-1">¿Olvidó su contraseña?<br>
                            <a href="#" class="fw-bolder text-info text-decoration-none" @click.prevent="ModalRecovery">Clic aquí</a>
                        </p>
                    </div>
                </div>
            </form>
            <div class="row mt-4">
                <div class="fw-bold col-md-6 mt-2 text-muted mx-auto">
                    <p class="mb-0 text-center lh-1">¿Tienes algun problema o necesitas contactarnos?<br>
                        <RouterLink :to="{ name: 'Contacto' }" class="btn btn-info fw-bolder text-decoration-none mt-3">Contáctenos</RouterLink>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import { loginUsuario } from '@/services/usuarios.service'

export default {
    name: "Login",
    data() {
        return {
            data_login: {
                usuario: '',
                password: ''
            },
            data_empty: {
                usuario: false,
                password: false
            },
            type_password: 'password'
        }
    },
    methods: {
        ModalRecovery() {
            this.$store.dispatch('showModal', { show_modal: 'ModalRecovery'});
        },
        toggleTypePassword() {
            if(this.type_password == 'password') this.type_password = 'text';
            else this.type_password = 'password';
        },
        async iniciarSesion() {
            if(!this.validarForm()) {
                this.$store.dispatch('showLoading');
                try {
                    const result = await loginUsuario(JSON.stringify(this.data_login));
                    this.$store.dispatch('hideLoading');
                    if(!result.error) {
                        localStorage.setItem('token', result.token);
                        this.$store.dispatch('setUsuario', result.usuario)

                        if(result.summary)
                            this.$store.dispatch('setSummary', result.summary)

                        this.$router.push({ name: 'Home' });
                    } else {
                        this.$store.dispatch('showError', result.error);
                        localStorage.removeItem('token');
                    }
                } catch(error) {
                    this.$store.dispatch('showError');
                    console.error(error);
                }
            }
        },
        validarForm() {
            // console.log(this.$data);
            let error = false;
            for (const key in this.data_login) {
                if(key != 'data_empty'){
                    if(this.data_login[key] && this.data_login[key].trim()) {
                        this.data_empty[key] = false;
                    } else {
                        this.data_empty[key] = true;
                        error = true;
                    }
                }
            }
            return error;
        }
    },
};
</script>

<style scoped>
.form-group {
    position: relative;
}
.form-group input {
    padding-left: 2.5rem;
}
.form-group input[name='password'] {
    padding-right: 3.5rem;
}
.form-group .fas {
    position: absolute;
    top: 10px;
    left: 10px;
    font-size: 1.5rem;
}
.form-group .fas.ver_password {
    top: 12px;
    right: 15px!important;
    left: inherit;
    cursor: pointer;
}
.form-text {
    position: absolute;
    bottom: -0.5rem;
}
</style>