import Vue from "vue";
import Vuex from "vuex";

// Modules
import modal from './modal';
import alertas from './alertas';
import dependencias from './dependencias';
import usuarios from './usuarios';
import retroalimentaciones from './retroalimentaciones';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        roles: {
            E : 'Empleado',
            A : 'Administrador',
            SA : 'SuperAdmin',
        },
        usuario: {
            info_personal: null,
            info_laboral: null
        },
        summary: null
    },
    mutations: {
        //Loading
        setUsuario(state, usuario) {
            state.usuario = usuario;
        },
        setSummary(state, summary) {
            state.summary = summary;
        },
    },
    actions: {
        //loading
        setUsuario({ commit }, usuario = { info_personal: null, info_laboral: null }) {
            commit('setUsuario', usuario);
        },
        setSummary({ commit }, summary = null) {
            commit('setSummary', summary);
        },
    },
    modules: {
        modal,
        alertas,
        dependencias,
        usuarios,
        retroalimentaciones
    },
});
