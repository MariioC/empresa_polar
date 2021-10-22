<template>
    <div class="sidebar" :class="{ 'open' : open , 'close': !open }">
        <div class="row">
            <i class="fas fa-bars menu_sidebar" @click.prevent="toggleSidebar"></i>

            <h3 v-if="rol == 'SA'" class="text-center text-muted mt-3 mb-5">
                <i class="fas fa-user-shield"></i> <span class="descripcion">Super-admin</span>
            </h3>
            <h3 v-else-if="rol == 'A'" class="text-center text-muted mt-3 mb-5">
                <i class="fas fa-users-cog"></i> <span class="descripcion">Administrador</span>
            </h3>
            <h3 v-else class="text-center text-muted mt-3 mb-5">
                <i class="fas fa-users"></i> <span class="descripcion">Empleado</span>
            </h3>

            <RouterLink class="side_link" :class="{ 'hint--right': !open }" aria-label="Perfil" :to="{ name: 'Perfil' }">
                <i class="fas fa-user"></i>
                <span class="descripcion">Perfil</span>
            </RouterLink>

            <hr class="divider">

            <RouterLink  v-if="rol == 'SA' || rol == 'A'" class="side_link mb-2" :class="{ 'hint--right': !open }" aria-label="Dependencias" :to="{ name: 'Home' }">
                <i class="fas fa-home"></i>
                <span class="descripcion">Dashboard</span>
            </RouterLink>

            <RouterLink  v-if="rol == 'SA'" class="side_link mb-2" :class="{ 'hint--right': !open }" aria-label="Dependencias" :to="{ name: 'Dependencias' }">
                <i class="fas fa-cubes"></i>
                <span class="descripcion">Dependencias</span>
            </RouterLink>

            <RouterLink  v-if="rol == 'A' || rol == 'SA'" class="side_link mb-2" :class="{ 'hint--right': !open }" aria-label="Empleados" :to="{ name: 'Empleados' }">
                <i class="fas fa-users"></i>
                <span class="descripcion">Empleados</span>
            </RouterLink>

            <RouterLink class="side_link mb-2" :class="{ 'hint--right': !open }" aria-label="Retrolimentación" :to="{ name: 'Retroalimentacion' }">
                <i class="fas fa-comments"></i>
                <span class="descripcion">Retrolimentaciones</span>
            </RouterLink>

            <a href="#" class="side_link mb-2" :class="{ 'hint--right': !open }" aria-label="Salir" @click="cerrarSesion">
                <i class="fas fa-power-off"></i>
                <span class="descripcion">Cerrar sesión</span>
            </a>

        </div>
    </div>
</template>

<script>
export default {
    name: 'SideBar',
    props: ['open_sidebar'],
    computed: {
        open() {
            return this.open_sidebar;
        },
        rol() {
            return this.$store.state.usuario?.info_personal?.rol;
        },
        descripcion_rol() {
            return this.$store.state.roles[this.rol];
        }
    },
    methods: {
        toggleSidebar() {
            this.$emit('toggleSidebar');
        },
        cerrarSesion() {
            localStorage.removeItem('token');
            this.$store.dispatch('setUsuario');
            this.$store.dispatch('setSummary');

            setTimeout(() => {
                this.$router.push({ name: 'Login' });
            }, 300);
        }
    },
}
</script>

<style scoped>

.sidebar {
    width: 305px;
    height: 100%;
    display: block;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 3;
    /* overflow: hidden; */
    border-right: 1px solid #DDD;
    box-shadow: 5px 0px 11px 0px rgba(0,0,0,0.1);
    padding: 2rem 1rem;
    transition: .3s ease all;
}
.sidebar.open {
    width: 305px;
    padding: 2rem 1.5rem;
}
.sidebar.close {
    width: 80px;
}
.sidebar .menu_sidebar {
    position: absolute;
    top: 10px;
    right: 20px;
    display: block;
    font-size: 1.6rem;
    width: 1.6rem;
    cursor: pointer;
    transition: .3s ease all;
}
.menu_sidebar:hover {
    color: #333333;
}
.sidebar.close .menu_sidebar {
    right: 27px;
}
.side_link {
    color: #333333b4;
    text-decoration: none;
    font-size: 1.2rem;
    outline: none;
    padding: 10px;
    transition: .3s ease all;
    font-weight: bold;
}
.side_link:hover {
    color: #333333;
    background: #33333312;
}
.side_link.active {
    color: #333333;
    background: #33333312;
}
.sidebar .descripcion{
    margin-left: 0.8rem;
}
.sidebar h3 .descripcion {
    margin-left: 0.2rem;
}

.sidebar.open .descripcion {
    display: inline-block;
}
.sidebar.close .descripcion {
    display: none;
}
.sidebar.open .side_link {
    text-align: left;
    padding: 10px;
}
.sidebar.close .side_link {
    text-align: center;
    padding: 10px 0;
}
.active {
    font-weight: 700;
}
</style>