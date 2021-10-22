<template>
    <div class="modal" :class="{ 'd-block' : modal.open }">
        <div class="modal-dialog animated fast" :class="{ 'fadeIn' : modal.visible, 'fadeOut' : !modal.visible, 'modal-dialog-horarios' : horarios }" role="document">
            <component :is='showModal'></component>
        </div>
    </div>
</template>

<script>
export default {
    name: "AppModal",
    computed: {
        modal() {
            return this.$store.state.modal;
        },
        showModal() {
            return this.$store.state.modal.show_modal;
        },
        horarios() {
            return this.$store.state.modal.show_modal == 'ModalHorario' ? true : false; 
        }
    },
    methods: {
        cerrar() {
            this.$store.dispatch('closeModal');
        }
    },
    components: {
        ModalUsuario: () => import(/* webpackChunkName: "ModalUsuario" */ "./ModalUsuario"),
        ModalPassword: () => import(/* webpackChunkName: "ModalPassword" */ "./ModalPassword"),
        ModalDependencia: () => import(/* webpackChunkName: "ModalDependencia" */ "./ModalDependencia"),
        ModalRetroalimentacion: () => import(/* webpackChunkName: "ModalRetroalimentacion" */ "./ModalRetroalimentacion"),
    }
};
</script>

<style>
/* .modal-dialog-horarios {
    max-width: 900px !important;
} */
</style>
