const alertas = {
    state: {
        loading: false,
        alerta_error: false,
        alerta_success: false,
    },
    mutations: {
        showLoading(state) {
            state.loading = true;
        },
		hideLoading(state) {
            state.loading = false;
		},
        showError(state, error) {
            state.alerta_error = error;
        },
        showSuccess(state, success) {
            state.alerta_success = success; 
        }
    },
    actions: {
        showLoading({ commit }) {
            this._vm.$swal({
                title: '¡Cargando!',
                text: 'Por favor, espere...',
                allowOutsideClick: false
            });
            this._vm.$swal.showLoading();
            commit("showLoading");
        },
		hideLoading({ commit }) {
            this._vm.$swal.close();
			commit('hideLoading');
		},
        showError({ commit }, error = false) {
            this._vm.$swal.fire({
                icon: 'error',
                title: '¡Uups!',
                html: !error ? 'Ah ocurrido un error inesperado. <br>Inténtalo más tarde' : error
            });
			commit('showError');
		},
        showSuccess({ commit }, success = false) {
            this._vm.$swal.fire({
                icon: 'success',
                title: '¡Correcto!',
                html: !success ? 'Operación realizada correctamente' : success
            });
			commit('showSuccess');
		}
    }
}

export default alertas;