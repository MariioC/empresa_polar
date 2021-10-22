<template>
    <div class="perfil animated fadeIn fast">
        <h1 class="text-center">Información de perfil</h1>
        <p class="text-center">A continuación, se muestra su información personal y su información laboral</p>
        <div class="row">
            <hr class="divider">
            <h2 class="text-center">Información personal</h2>
            <div v-if="info_personal" class="row col-md-6 mx-auto mb-4 mt-3">
                <div class="row col-md-6">
                    <p><b>Nombre: </b>{{ info_personal.nombres }}</p>
                    <p><b>Apellidos: </b>{{ info_personal.apellidos }}</p>
                    <p><b>Fecha de nacimiento: </b>{{ info_personal.fecha_nacimiento }}</p>
                    <p><b>Genero: </b>{{ info_personal.genero }}</p>
                    <p><b>Documento: </b>{{ info_personal.documento }}</p>
                </div>
                <div class="row col-md-6">
                    <p><b>Celular: </b>{{ info_personal.celular }}</p>
                    <p><b>Correo: </b>{{ info_personal.correo }}</p>
                    <p><b>Dirección: </b>{{ info_personal.direccion }}</p>
                    <p><b>Ciudad: </b>{{ info_personal.ciudad }}</p>
                    <p><b>Estado civil: </b>{{ info_personal.estado_civil }}</p>
                </div>
            </div>
        </div>
        <div class="row">
            <hr class="divider">
            <h2 class="text-center">Información laboral</h2>
            <div class="row col-md-3 mx-auto mt-3">
                <div v-if="info_laboral" class="row col-md-12">
                    <p><b>Dependencia: </b>{{ info_laboral.nombre_dependencia }}</p>
                    <p><b>Cargo: </b>{{ info_laboral.nombre_cargo }}</p>
                    <p><b>Salario: </b>${{ info_laboral.salario }}</p>
                    <p><b>Tipo de contrato: </b>{{ info_laboral.tipo_contrato }}</p>
                    <p><b>Fecha de ingreso: </b>{{ info_laboral.fecha_ingreso }}</p>
                    <p><b>Terminación de contrato: </b>{{ info_laboral.fecha_terminacion }}</p>
                </div>
                <div v-else class="row col-md-12">
                    <h4 class="text-danger text-center fw-normal">Infomación laboral aún no registrada</h4>
                </div>
            </div>
        </div>
        <hr class="divider">
        <div class="d-flex justify-content-center mt-5">
            <button type="button" class="btn btn-primary mx-1" @click="modalPerfil"><i class="fas fa-user mx-1"></i> Actualizar perfil</button>
            <button type="button" class="btn btn-info mx-1" @click="modalPassword"><i class="fas fa-lock mx-1"></i> Actualizar contraseña</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Perfil',
    computed: {
        info_personal() {
            return this.$store.state.usuario?.info_personal;
        },
        info_laboral() {
            return this.$store.state.usuario?.info_laboral;
        }
    },
    methods: {
        modalPerfil() {
            this.$store.dispatch('showModal', { show_modal: 'ModalUsuario', id_edicion: this.info_personal.id_usuario });
        },
        modalPassword() {
            this.$store.dispatch('showModal', { show_modal: 'ModalPassword' });
        }
    },
}
</script>

<style scoped>

</style>