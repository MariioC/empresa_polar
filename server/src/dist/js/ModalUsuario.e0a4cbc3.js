(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["ModalUsuario"],{"0483":function(e,t,a){"use strict";a.d(t,"b",(function(){return n})),a.d(t,"a",(function(){return i})),a.d(t,"d",(function(){return s})),a.d(t,"c",(function(){return l})),a.d(t,"e",(function(){return c}));var r=a("1da1"),o=(a("96cf"),a("d3b7"),a("99af"),a("c3e4")),n=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t){var a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,fetch("".concat(o["a"],"dependencias/"),{method:"POST",headers:Object(o["b"])(),body:t});case 2:return a=e.sent,e.next=5,a.json();case 5:return e.abrupt("return",e.sent);case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),i=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t){var a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,fetch("".concat(o["a"],"dependencias/"),{method:"PUT",headers:Object(o["b"])(),body:t});case 2:return a=e.sent,e.next=5,a.json();case 5:return e.abrupt("return",e.sent);case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),s=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t){var a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,fetch("".concat(o["a"],"dependencias/").concat(t),{method:"DELETE",headers:Object(o["b"])()});case 2:return a=e.sent,e.next=5,a.json();case 5:return e.abrupt("return",e.sent);case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),l=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t){var a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,fetch("".concat(o["a"],"dependencias/cargo/").concat(t),{method:"DELETE",headers:Object(o["b"])()});case 2:return a=e.sent,e.next=5,a.json();case 5:return e.abrupt("return",e.sent);case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),c=function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(){var t;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,fetch("".concat(o["a"],"dependencias/"),{headers:Object(o["b"])()});case 2:return t=e.sent,e.next=5,t.json();case 5:return e.abrupt("return",e.sent);case 6:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}()},b424:function(e,t,a){"use strict";a.r(t);var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"modal-content"},[a("div",{staticClass:"modal-header"},[a("h3",{staticClass:"modal-title"},[e._v("Información de usuario")]),a("button",{staticClass:"btn-close",attrs:{type:"button","data-bs-dismiss":"modal","aria-label":"Close"},on:{click:e.cerrar}},[a("span",{attrs:{"aria-hidden":"true"}})])]),a("div",{staticClass:"modal-body"},["A"!=e.rol&&"SA"!=e.rol||e.id_edicion?e._e():a("div",[a("p",{staticClass:"text-center fw-bolder text-muted"},[e._v("Al registrar un usuario, la contraseña sera su mismo número de documento")])]),"A"==e.rol||"SA"==e.rol?a("div",{staticClass:"btn-group d-flex justify-content-center",attrs:{role:"group","aria-label":"Basic example"}},[a("button",{staticClass:"btn btn-outline-info",class:{active:e.informacion_personal},attrs:{type:"button"},on:{click:function(t){return e.toggleInformacion("personal")}}},[e._v("Información personal")]),a("button",{staticClass:"btn btn-outline-info",class:{active:e.informacion_laboral},attrs:{type:"button"},on:{click:function(t){return e.toggleInformacion("laboral")}}},[e._v("Información laboral")])]):e._e(),a("form",{staticClass:"mt-3 info_personal animated fadeIn fast",class:{"d-none":!e.informacion_personal}},[a("fieldset",[a("div",{staticClass:"form-group"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"nombres"}},[e._v("Nombres")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.nombres,expression:"info_personal.nombres"}],staticClass:"form-control",attrs:{type:"text",id:"nombres",placeholder:"Nombres"},domProps:{value:e.info_personal.nombres},on:{input:function(t){t.target.composing||e.$set(e.info_personal,"nombres",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"apellidos"}},[e._v("Apellidos")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.apellidos,expression:"info_personal.apellidos"}],staticClass:"form-control",attrs:{type:"text",id:"apellidos",placeholder:"Apellidos"},domProps:{value:e.info_personal.apellidos},on:{input:function(t){t.target.composing||e.$set(e.info_personal,"apellidos",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"documento"}},[e._v("N° de documento")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.documento,expression:"info_personal.documento"}],staticClass:"form-control",attrs:{type:"text",id:"documento",placeholder:"N° de documento"},domProps:{value:e.info_personal.documento},on:{input:function(t){t.target.composing||e.$set(e.info_personal,"documento",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"fecha_nacimiento"}},[e._v("Fecha de nacimiento")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.fecha_nacimiento,expression:"info_personal.fecha_nacimiento"}],staticClass:"form-control",attrs:{type:"date",id:"fecha_nacimiento",placeholder:"Fecha de nacimiento"},domProps:{value:e.info_personal.fecha_nacimiento},on:{input:function(t){t.target.composing||e.$set(e.info_personal,"fecha_nacimiento",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"genero"}},[e._v("Género")]),a("select",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.genero,expression:"info_personal.genero"}],staticClass:"form-select",attrs:{id:"genero"},on:{change:function(t){var a=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.info_personal,"genero",t.target.multiple?a:a[0])}}},[a("option",{attrs:{value:""}},[e._v("Seleccione...")]),a("option",{attrs:{value:"Masculino"}},[e._v("Masculino")]),a("option",{attrs:{value:"Femenino"}},[e._v("Femenino")]),a("option",{attrs:{value:"Otro"}},[e._v("Otro")])])]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"correo"}},[e._v("Correo")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.correo,expression:"info_personal.correo"}],staticClass:"form-control",attrs:{type:"text",id:"correo",placeholder:"Correo"},domProps:{value:e.info_personal.correo},on:{input:function(t){t.target.composing||e.$set(e.info_personal,"correo",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"celular"}},[e._v("Celular")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.celular,expression:"info_personal.celular"}],staticClass:"form-control",attrs:{type:"text",id:"celular",placeholder:"Celular"},domProps:{value:e.info_personal.celular},on:{input:function(t){t.target.composing||e.$set(e.info_personal,"celular",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"direccion"}},[e._v("Dirección")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.direccion,expression:"info_personal.direccion"}],staticClass:"form-control",attrs:{type:"text",id:"direccion",placeholder:"Dirección"},domProps:{value:e.info_personal.direccion},on:{input:function(t){t.target.composing||e.$set(e.info_personal,"direccion",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"ciudad"}},[e._v("Ciudad")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.ciudad,expression:"info_personal.ciudad"}],staticClass:"form-control",attrs:{type:"text",id:"ciudad",placeholder:"Ciudad"},domProps:{value:e.info_personal.ciudad},on:{input:function(t){t.target.composing||e.$set(e.info_personal,"ciudad",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"estado"}},[e._v("Estado civil")]),a("select",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.estado_civil,expression:"info_personal.estado_civil"}],staticClass:"form-select",attrs:{id:"estado_civil"},on:{change:function(t){var a=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.info_personal,"estado_civil",t.target.multiple?a:a[0])}}},[a("option",{attrs:{value:""}},[e._v("Seleccione...")]),a("option",{attrs:{value:"Soltero(a)"}},[e._v("Soltero(a)")]),a("option",{attrs:{value:"Casado(a)"}},[e._v("Casado(a)")]),a("option",{attrs:{value:"Divorciado(a)"}},[e._v("Divorciado(a)")]),a("option",{attrs:{value:"Viudo(a)"}},[e._v("Viudo(a)")])])]),"SA"==e.rol?a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"estado"}},[e._v("Rol")]),a("select",{directives:[{name:"model",rawName:"v-model",value:e.info_personal.rol,expression:"info_personal.rol"}],staticClass:"form-select",attrs:{id:"rol"},on:{change:function(t){var a=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.info_personal,"rol",t.target.multiple?a:a[0])}}},[a("option",{attrs:{value:""}},[e._v("Seleccione...")]),a("option",{attrs:{value:"SA"}},[e._v("Superadministrador")]),a("option",{attrs:{value:"A"}},[e._v("Administrador")]),a("option",{attrs:{value:"E"}},[e._v("Empleado")])])]):e._e()])]),a("form",{staticClass:"mt-3 info_laboral animated fadeIn fast",class:{"d-none":!e.informacion_laboral}},[a("fieldset",[a("div",{staticClass:"form-group"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"dependencia"}},[e._v("Dependencia")]),a("select",{directives:[{name:"model",rawName:"v-model",value:e.info_laboral.id_dependencia,expression:"info_laboral.id_dependencia"}],staticClass:"form-select",attrs:{id:"dependencia"},on:{change:function(t){var a=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.info_laboral,"id_dependencia",t.target.multiple?a:a[0])}}},[a("option",{attrs:{value:""}},[e._v("Seleccione...")]),e._l(e.dependencias,(function(t,r){return a("option",{key:r,domProps:{value:t.dependencia.id_dependencia}},[e._v(e._s(t.dependencia.nombre_dependencia))])}))],2)]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"cargo"}},[e._v("Cargo")]),a("select",{directives:[{name:"model",rawName:"v-model",value:e.info_laboral.id_cargo,expression:"info_laboral.id_cargo"}],staticClass:"form-select",attrs:{id:"id_cargo"},on:{change:function(t){var a=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.info_laboral,"id_cargo",t.target.multiple?a:a[0])}}},[a("option",{attrs:{value:""}},[e._v("Seleccione...")]),e.cargos_dependencia?e._l(e.cargos_dependencia,(function(t,r){return a("option",{key:r,domProps:{value:t.id_cargo}},[e._v(e._s(t.nombre_cargo))])})):e._e()],2)]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"tipo_contrato"}},[e._v("Tipo de contrato")]),a("select",{directives:[{name:"model",rawName:"v-model",value:e.info_laboral.tipo_contrato,expression:"info_laboral.tipo_contrato"}],staticClass:"form-select",attrs:{id:"tipo_contrato"},on:{change:function(t){var a=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.$set(e.info_laboral,"tipo_contrato",t.target.multiple?a:a[0])}}},[a("option",{attrs:{value:""}},[e._v("Seleccione...")]),a("option",{attrs:{value:"Termino fijo"}},[e._v("Termino fijo")]),a("option",{attrs:{value:"Termino indefinido"}},[e._v("Termino indefinido")]),a("option",{attrs:{value:"Prestación de servicios"}},[e._v("Prestación de servicios")])])]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"salario"}},[e._v("Salario")]),a("div",{staticClass:"input-group"},[a("span",{staticClass:"input-group-text"},[e._v("$")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.salario,expression:"salario"}],staticClass:"form-control",attrs:{type:"text",id:"salario",disabled:""},domProps:{value:e.salario},on:{input:function(t){t.target.composing||(e.salario=t.target.value)}}})])]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"fecha_ingreso"}},[e._v("Fecha de ingreso")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_laboral.fecha_ingreso,expression:"info_laboral.fecha_ingreso"}],staticClass:"form-control",attrs:{type:"date",id:"fecha_ingreso"},domProps:{value:e.info_laboral.fecha_ingreso},on:{input:function(t){t.target.composing||e.$set(e.info_laboral,"fecha_ingreso",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"form-label mb-0",attrs:{for:"fecha_terminacion"}},[e._v("Fecha de terminación")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.info_laboral.fecha_terminacion,expression:"info_laboral.fecha_terminacion"}],staticClass:"form-control",attrs:{type:"date",id:"fecha_terminacion"},domProps:{value:e.info_laboral.fecha_terminacion},on:{input:function(t){t.target.composing||e.$set(e.info_laboral,"fecha_terminacion",t.target.value)}}})])])])]),a("div",{staticClass:"modal-footer"},[e.id_edicion?a("button",{staticClass:"btn btn-success",attrs:{type:"button"},on:{click:function(t){return t.preventDefault(),e.actualizarUsuario.apply(null,arguments)}}},[e._v("Actualizar usuario")]):a("button",{staticClass:"btn btn-success",attrs:{type:"button"},on:{click:function(t){return t.preventDefault(),e.registrarUsuario.apply(null,arguments)}}},[e._v("Registrar usuario")]),a("button",{staticClass:"btn btn-danger",attrs:{type:"button"},on:{click:e.cerrar}},[e._v("Cancelar")])])])},o=[],n=a("1da1"),i=(a("96cf"),a("4de4"),a("c740"),a("0483")),s=a("e7b7"),l={name:"ModalUsuario",data:function(){return{informacion_personal:!0,informacion_laboral:!1,info_personal:{nombres:null,apellidos:null,documento:null,fecha_nacimiento:null,genero:"",correo:null,celular:null,direccion:null,ciudad:null,estado_civil:"",rol:"",password:""},info_laboral:{id_dependencia:"",id_cargo:"",tipo_contrato:"",fecha_ingreso:null,fecha_terminacion:null}}},computed:{id_edicion:function(){return this.$store.state.modal.id_edicion},usuario:function(){var e;return null===(e=this.$store.state.usuario)||void 0===e?void 0:e.info_personal},rol:function(){return this.usuario.rol},dependencias:function(){return JSON.parse(JSON.stringify(this.$store.state.dependencias.dependencias))},cargos_dependencia:function(){var e=this;if(this.info_laboral.id_dependencia){if(this.dependencias.length){var t=this.dependencias.filter((function(t){return t.dependencia.id_dependencia==e.info_laboral.id_dependencia}));return!!t.length&&t[0]["cargos"]}return!1}return!1},salario:function(){var e=this;if(this.info_laboral.id_cargo){if(this.cargos_dependencia.length){var t=this.cargos_dependencia.filter((function(t){return t.id_cargo==e.info_laboral.id_cargo}));return t.length?t[0]["salario"]:0}return!1}return 0}},created:function(){var e,t,a;this.id_edicion&&(this.id_edicion==this.usuario.id_usuario?(this.info_personal=JSON.parse(JSON.stringify(null===(e=this.$store.state.usuario)||void 0===e?void 0:e.info_personal)),null!==(t=this.$store.state.usuario)&&void 0!==t&&t.info_laboral&&(this.info_laboral=JSON.parse(JSON.stringify(null===(a=this.$store.state.usuario)||void 0===a?void 0:a.info_laboral)))):this.obtenerUsuarioState());this.dependencias.length||this.getDependencias()},methods:{toggleInformacion:function(e){"personal"==e?(this.informacion_personal=!0,this.informacion_laboral=!1):(this.informacion_personal=!1,this.informacion_laboral=!0)},getDependencias:function(){var e=this;return Object(n["a"])(regeneratorRuntime.mark((function t(){var a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e.$store.dispatch("showLoading"),t.prev=1,t.next=4,Object(i["e"])();case 4:a=t.sent,e.$store.dispatch("hideLoading"),a.error?e.$store.dispatch("showError",a.error):e.$store.dispatch("setDependencias",a.dependencias),t.next=13;break;case 9:t.prev=9,t.t0=t["catch"](1),e.$store.dispatch("showError"),console.error(t.t0);case 13:case"end":return t.stop()}}),t,null,[[1,9]])})))()},registrarUsuario:function(){var e=this;return Object(n["a"])(regeneratorRuntime.mark((function t(){var a,r,o;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e.$store.dispatch("showLoading"),a={info_personal:e.info_personal,info_laboral:e.info_laboral},t.prev=2,t.next=5,Object(s["i"])(JSON.stringify(a));case 5:r=t.sent,e.$store.dispatch("hideLoading"),r.error?e.$store.dispatch("showError",r.error):(e.$store.dispatch("showSuccess",r.mensaje),o=JSON.parse(JSON.stringify(e.$store.state.usuarios.usuarios)),o.length&&(o.unshift(r.usuario),e.$store.dispatch("setUsuarios",o)),e.cerrar()),t.next=14;break;case 10:t.prev=10,t.t0=t["catch"](2),e.$store.dispatch("showError"),console.error(t.t0);case 14:case"end":return t.stop()}}),t,null,[[2,10]])})))()},actualizarUsuario:function(){var e=this;return Object(n["a"])(regeneratorRuntime.mark((function t(){var a,r,o,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e.$store.dispatch("showLoading"),a={info_personal:e.info_personal,info_laboral:e.info_laboral},t.prev=2,t.next=5,Object(s["b"])(e.id_edicion==e.usuario.id_usuario?null:e.id_edicion,JSON.stringify(a));case 5:r=t.sent,e.$store.dispatch("hideLoading"),r.error?e.$store.dispatch("showError",r.error):(e.$store.dispatch("showSuccess",r.mensaje),o=JSON.parse(JSON.stringify(e.$store.state.usuarios.usuarios)),n=o.findIndex((function(e){return e.info_personal.id_usuario==r.usuario.info_personal.id_usuario})),o[n]=r.usuario,e.$store.dispatch("setUsuarios",o),e.id_edicion==e.usuario.id_usuario&&e.$store.dispatch("setUsuario",r.usuario),e.cerrar()),t.next=14;break;case 10:t.prev=10,t.t0=t["catch"](2),e.$store.dispatch("showError"),console.error(t.t0);case 14:case"end":return t.stop()}}),t,null,[[2,10]])})))()},obtenerUsuarioState:function(){var e=this,t=JSON.parse(JSON.stringify(this.$store.state.usuarios.usuarios)),a=t.filter((function(t){return t.info_personal.id_usuario==e.id_edicion}))[0];this.info_personal=JSON.parse(JSON.stringify(null===a||void 0===a?void 0:a.info_personal)),null!==a&&void 0!==a&&a.info_laboral&&(this.info_laboral=JSON.parse(JSON.stringify(null===a||void 0===a?void 0:a.info_laboral)))},cerrar:function(){this.$store.dispatch("closeModal")}}},c=l,u=a("2877"),d=Object(u["a"])(c,r,o,!1,null,null,null);t["default"]=d.exports},c740:function(e,t,a){"use strict";var r=a("23e7"),o=a("b727").findIndex,n=a("44d2"),i="findIndex",s=!0;i in[]&&Array(1)[i]((function(){s=!1})),r({target:"Array",proto:!0,forced:s},{findIndex:function(e){return o(this,e,arguments.length>1?arguments[1]:void 0)}}),n(i)}}]);
//# sourceMappingURL=ModalUsuario.e0a4cbc3.js.map