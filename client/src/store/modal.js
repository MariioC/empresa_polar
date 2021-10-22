const modal = {
    state: {
        open: false,
        visible: false,
        show_modal: null,
        id_edicion: null
    },
    mutations: {
		showModal(state, { show_modal, id_edicion }) {
            state.open = true;
            state.visible = true;
            state.show_modal = show_modal;
            state.id_edicion = id_edicion;
		},
		closeModal(state) {
			state.open = false;
            state.show_modal = null;
            state.id_edicion = null;
		},
		hideModal(state) {
			state.visible = false;
		}
    },
    actions: {
        showModal({ commit }, { show_modal, id_edicion = null }) {
            commit("showModal", {show_modal, id_edicion});
        },
		closeModal({ commit }) {
			commit('hideModal');
			setTimeout(() => {
				commit('closeModal');
			}, 300);
		}
    }
}

export default modal;