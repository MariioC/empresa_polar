const dependencias = {
    state: {
        dependencias: []
    },
    mutations: {
		setDependencias(state, dependencias) {
			state.dependencias = dependencias;
		}
    },
    actions: {
        setDependencias({ commit }, dependencias) {
            commit("setDependencias", dependencias);
        },
    }
}

export default dependencias;