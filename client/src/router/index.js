import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        meta: {
            requiresAuth: true,
            title: "Polar | Inicio",
        },
        component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue"),
        children: [
            {
                path: "/perfil",
                name: "Perfil",
                meta: {
                    requiresAuth: true,
                    title: "Polar | Perfil",
                },
                component: () => import(/* webpackChunkName: "perfil" */ "../views/Perfil.vue"),
            },
            {
                path: "/empleados",
                name: "Empleados",
                meta: {
                    requiresAuth: true,
                    requiresAdmin: true,
                    title: "Polar | Empleados",
                },
                component: () => import(/* webpackChunkName: "empleados" */ "../views/Empleados.vue"),
            },
            {
                path: "/retroalimentacion/:id_usuario?",
                name: "Retroalimentacion",
                meta: {
                    requiresAuth: true,
                    title: "Polar | Retroalimentacion",
                },
                component: () => import(/* webpackChunkName: "retroalimentacion" */ "../views/Retroalimentacion.vue"),
            },
            {
                path: "/dependencias",
                name: "Dependencias",
                meta: {
                    requiresAuth: true,
                    requiresAdmin: true,
                    title: "Polar | Dependencias",
                },
                component: () => import(/* webpackChunkName: "dependencias" */ "../views/Dependencias.vue"),
            },
        ]
    },
    {
        path: "/login",
        name: "Login",
        meta: {
            requiresAuth: false,
            title: "Polar | Login",
        },
        component: () => import(/* webpackChunkName: "login" */ "../views/Login.vue"),
        beforeEnter: (to, from, next) => {
            if (localStorage.getItem("token")) {
                next({ name: "Home" });
            } else {
                // console.log('ir a login');
                next();
            }
        },
    },
    {
        path: "/contacto",
        name: "Contacto",
        meta: {
            requiresAuth: false,
            title: "Polar | Contactenos",
        },
        component: () => import(/* webpackChunkName: "contacto" */ "../views/Contacto.vue"),
    },
    {
        path: "*",
        redirect: { name: "Home" }
    },
];

const router = new VueRouter({
    routes,
    // linkActiveClass: "active",
    linkExactActiveClass: "active",
});

router.beforeEach((to, from, next) => {

    //Pongo el scroll en la parte superior
    if(Object.entries(to.query).length == 0) {
        if(Object.entries(from.query).length == 0) {
            window.scrollTo({
                top: 0,
                behavior: 'smooth',
            });
        }
    }
    
    document.title = to.meta.title;
    // next();

    if (to.meta.requiresAuth && !localStorage.getItem('token')) {
        next({ name: 'Login' });
    } else if (to.meta.requiresAuth && localStorage.getItem("token") && !to.meta.requiresAdmin) {
        next();
    } else {
        if (to.meta.requiresAuth && !to.meta.requiresAdmin) {
            next();
        } else if (to.meta.requiresAuth && to.meta.requiresAdmin) {
            if (store.state.usuario.info_personal?.rol == 'SA' || store.state.usuario.info_personal?.rol == 'A') {
                next();
            } else {
                next({
                    name: 'Home'
                })
            }
        } else {
            next();
        }

    }

});

export default router;
