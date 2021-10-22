<template>
    <div id="app">
        <RouterView />
        <AppModal />
    </div>
</template>

<script>
import { comprobarSesion } from '@/services/usuarios.service'
export default {
	name: 'App',
	components: {
        AppModal: () => import(/* webpackChunkName: "AppModal" */ '@/components/modales/AppModal'),
	},
    created() {
        this.comprobarSesion()  
    },
    methods: {
        async comprobarSesion() {
            this.$store.dispatch('showLoading');
            const token = localStorage.getItem('token');
            if(token){
                try {
                    const result = await comprobarSesion();
                    this.$store.dispatch('hideLoading');
                    if (!result.error) {
                        this.$store.dispatch('setUsuario', result.usuario);
                        
                        if(result.summary)
                            this.$store.dispatch('setSummary', result.summary);

                    } else {
                        this.$store.dispatch('showError', result.error);
                        this.$store.dispatch('setUsuario', null);
                        localStorage.removeItem('token');
                        setTimeout(() => {
                            this.$router.push({ name: 'Login' });
                        }, 500)
                    }
                } catch (error) {
                    console.error(error);
                    this.$store.dispatch('showError');
                    this.$store.dispatch('setUsuario', null);
                    localStorage.removeItem('token');
                    this.$router.push({ name: 'Login' });
                }
            } else {
                localStorage.removeItem('token');
                this.$store.dispatch('setUsuario', null);
                this.$store.dispatch('hideLoading');
            }
        }
    },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap");

@import "assets/css/bootstrap.min.css";
@import "assets/css/animate.css";
@import "assets/css/hint.min.css";

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Montserrat", sans-serif;
}

html {
    font-size: 16px;
}

body {
    font-family: "Montserrat", sans-serif;
    font-size: 16px;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    font-weight: 700 !important;
    letter-spacing: -2px;
    color: #333333 !important;
}

h1 {
    font-size: 3rem;
    margin: 15px 0;
}

h2 {
    font-size: 2.4rem;
    font-weight: bold;
}
h3 {
    font-size: 1.75rem;
}
h4 {
    font-size: 1.2rem;
}

hr.divider {
    /* width: 100%; */
    width: calc(100% - 12%);
    height: 2px!important;
    margin: 1rem auto;
    background-color: #2b2b2b;
}

/* ESTILOS AL SWAL ALERT */
.swal2-popup.swal2-loading {
    max-width: 280px;
}
.swal2-popup.swal2-icon-error,
.swal2-popup.swal2-icon-success {
    max-width: 300px;
}
.swal2-popup.swal2-icon-warning {
    max-width: 400px;
}
.swal2-popup.swal2-icon-error .swal2-icon,
.swal2-popup.swal2-icon-success .swal2-icon {
    margin: 2rem auto .6rem
}
.swal2-popup.swal2-icon-error .swal2-title,
.swal2-popup.swal2-icon-success .swal2-title {
    padding: .5rem 1rem;
}
.swal2-popup.swal2-icon-error .swal2-html-container,
.swal2-popup.swal2-icon-success .swal2-html-container {
    margin: .5rem auto;
    padding: 0 1rem;
}

/*  MODALES */
.modal .modal-header {
    padding: 1rem 1rem .2rem 1rem;
}
.modal .modal-body {
    padding: .2rem 1rem 1rem 1rem;
}
</style>
