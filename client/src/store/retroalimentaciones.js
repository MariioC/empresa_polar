const retroalimentaciones = {
    state: {
        retroalimentaciones: []
    },
    mutations: {
		setRetroalimentaciones(state, retroalimentaciones) {
			state.retroalimentaciones = retroalimentaciones;
		}
    },
    actions: {
        setRetroalimentaciones({ commit }, retroalimentaciones) {
            commit("setRetroalimentaciones", retroalimentaciones);
        },
    }
}

export default retroalimentaciones;