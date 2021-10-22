const usuarios = {
    state: {
        usuarios: []
    },
    mutations: {
		setUsuarios(state, usuarios) {
			state.usuarios = usuarios;
		}
    },
    actions: {
        setUsuarios({ commit }, usuarios) {
            commit("setUsuarios", usuarios);
        },
    }
}

export default usuarios;