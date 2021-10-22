<template>
    <div class="home animated fadeIn fast">
		<AppSideBar :open_sidebar="open_sidebar" @toggleSidebar="toggleSidebar"/>
	
		<RouterLink :to="{ name: 'Contacto' }" class="btn-contacto btn btn-info fw-bolder text-decoration-none mt-3"><i class="fas fa-id-card mx-1"></i> Contacto</RouterLink>

        <div class="content" :class="{ 'close' : !open_sidebar }">
			<div v-if="ruta == 'Home' && !summary" class="jumbotron p-5">
				<h1 class="display-4">Bienvenido<span v-if="usuario" class="animated fadeIn">, {{ usuario.nombres }}</span></h1>
				<p class="lead">En este espacio podras conocer las retroalimentaciones y el puntaje que se te ha asignado en cada una de ellas, esto lo hacemos con la finalidad de calificar y darte conocimiento de como es tu desempeño en la empresa.</p>
				<hr class="my-4">
				<p class="text-center">Puedes actualizar tu información personal y tu contraseña en el menu "Perfil"</p>
				<RouterLink class="btn btn-primary btn-lg mx-auto" :to="{ name: 'Retroalimentacion' }" role="button">Ver retroalimentaciones</RouterLink>
			</div>
			<div v-if="ruta == 'Home' && summary" class="row justify-content-center animated fadeIn fast">

				<h1 class="text-center mb-4 mt-3">Información general</h1>				
				<div v-for="(s, index) in summary_usuarios" :key="index" class="card text-white bg-primary m-1" style="max-width: 24%;">
					<div class="card-header text-center fw-bolder" style="font-size: 1.8rem;"><span class="mx-1" v-html="s[0]"></span> {{ index.charAt(0).toUpperCase() + index.slice(1).replace('_', ' ') }}</div>
					<div class="card-body py-3">
						<p class="card-text fw-normal text-center display-5">{{ s[1] }}</p>
					</div>
				</div>

				<hr class="divider">
				
				<h1 class="text-center mb-4 mt-3">Información laboral</h1>				
				<div v-for="(s, index) in summary_dependencias" :key="index" class="card text-white bg-success m-1" style="max-width: 24%;">
					<div class="card-header text-center fw-bolder" style="font-size: 1.8rem;"><span class="mx-1" v-html="s[0]"></span> {{ index.charAt(0).toUpperCase() + index.slice(1) }}</div>
					<div class="card-body py-3">
						<p class="card-text fw-normal text-center display-5">{{ index == 'nómina' ? '$': '' }}{{ s[1] }}</p>
					</div>
				</div>

				<hr class="divider">
				
				<h1 class="text-center mb-4 mt-3">Información retroalimentaciones</h1>				
				<div v-for="(s, index) in summary_empleados" :key="index" class="card text-white bg-warning m-1" style="max-width: 24%;">
					<div class="card-header text-center fw-bolder" style="font-size: 1.8rem;"><span class="mx-1" v-html="s[0]"></span> {{ index.charAt(0).toUpperCase() + index.slice(1) }}</div>
					<div class="card-body py-3">
						<p class="card-text fw-normal text-center display-5">{{ s[1] }}</p>
					</div>
				</div>
			</div>
			<template v-else>					
				<router-view></router-view>
			</template>
		</div>
    </div>
</template>

<script>
export default {
    name: "Home",
	data() {
		return {
			open_sidebar: true,
		}
	},
	computed: {
		ruta() {
			return this.$route.name;
		},
		summary() {
			return this.$store.state.summary;
		},
		usuario() {
			return this.$store.state.usuario?.info_personal;
		},
		summary_usuarios() {
			const summary = JSON.parse(JSON.stringify(this.$store.state.summary))
			const resumen = {
				"super-admins": ['<i class="fas fa-user-shield"></i>', summary['superadmins']],
				admins: ['<i class="fas fa-users-cog"></i>', summary['admins']],
				empleados: ['<i class="fas fa-users"></i>', summary['empleados']]
			}
			return resumen;
		},
		summary_dependencias() {
			const summary = JSON.parse(JSON.stringify(this.$store.state.summary))
			const resumen = {
				dependencias: ['<i class="fas fa-cubes"></i>', summary['dependencias']],
				cargos: ['<i class="fab fa-black-tie"></i>', summary['cargos']],
				"nómina": ['<i class="fas fa-hand-holding-usd"></i>', summary['nomina']]
			}
			return resumen;
		},
		summary_empleados() {
			const summary = JSON.parse(JSON.stringify(this.$store.state.summary))
			const resumen = {
				total: ['<i class="fas fa-comments"></i>', summary['retroalimentaciones']],
				"mejor puntaje": ['<i class="fas fa-thumbs-up"></i>', summary['mejor_puntaje']]
			}
			return resumen;
		}
	},
	methods: {
		toggleSidebar() {
			this.open_sidebar = !this.open_sidebar;
		}
	},
	components: {
		AppSideBar: () => import( /* webpackChunkName: "sidebar" */ "@/components/AppSideBar.vue" )
	}
};
</script>

<style scoped>
.content {
	padding: 1rem;
	padding-left: 315px;
	transition: .3s ease all;
}

.content.close{
	padding-left: 95px;
}

.btn-contacto {
	position: absolute;
	top: .1rem;
	right: 1rem;
	z-index: 99;
}
</style>
