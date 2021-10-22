import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// SweetAlert2
import VueSweetalert2 from "vue-sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";

const options = {
    customClass: {
        confirmButton: "btn btn-success mx-1",
        cancelButton: "btn btn-danger mx-1",
    },
    buttonsStyling: false,
};
Vue.use(VueSweetalert2, options);

Vue.filter("formatoFecha", (fecha, formato = 'full') => {
    fecha = new Date(fecha)
    function join(date, options, separator) {
        function format(m) {
           let f = new Intl.DateTimeFormat('es', m);
           return f.format(date);
        }
        return options.map(format).join(separator);
    }
    let opciones = [{ day: 'numeric' }, { month: 'short' }, { year: 'numeric' }];
    let fechaFormateada = join(fecha, opciones, ' ');
    if(formato == 'mes') {
        let opciones = [{ month: 'long' }];
        let mes = join(fecha, opciones, ' ');
        return mes;
    }
    return fechaFormateada;
});


Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app");
