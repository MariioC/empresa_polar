(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["home"],{"1e3f":function(t,a,s){"use strict";s("98cd")},"98cd":function(t,a,s){},b0c0:function(t,a,s){var e=s("83ab"),i=s("5e77").EXISTS,n=s("9bf2").f,r=Function.prototype,c=r.toString,o=/^\s*function ([^ (]*)/,d="name";e&&!i&&n(r,d,{configurable:!0,get:function(){try{return c.call(this).match(o)[1]}catch(t){return""}}})},bb51:function(t,a,s){"use strict";s.r(a);var e=function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"home animated fadeIn fast"},[s("AppSideBar",{attrs:{open_sidebar:t.open_sidebar},on:{toggleSidebar:t.toggleSidebar}}),s("RouterLink",{staticClass:"btn-contacto btn btn-info fw-bolder text-decoration-none mt-3",attrs:{to:{name:"Contacto"}}},[s("i",{staticClass:"fas fa-id-card mx-1"}),t._v(" Contacto")]),s("div",{staticClass:"content",class:{close:!t.open_sidebar}},["Home"!=t.ruta||t.summary?t._e():s("div",{staticClass:"jumbotron p-5"},[s("h1",{staticClass:"display-4"},[t._v("Bienvenido"),t.usuario?s("span",{staticClass:"animated fadeIn"},[t._v(", "+t._s(t.usuario.nombres))]):t._e()]),s("p",{staticClass:"lead"},[t._v("En este espacio podras conocer las retroalimentaciones y el puntaje que se te ha asignado en cada una de ellas, esto lo hacemos con la finalidad de calificar y darte conocimiento de como es tu desempeño en la empresa.")]),s("hr",{staticClass:"my-4"}),s("p",{staticClass:"text-center"},[t._v('Puedes actualizar tu información personal y tu contraseña en el menu "Perfil"')]),s("RouterLink",{staticClass:"btn btn-primary btn-lg mx-auto",attrs:{to:{name:"Retroalimentacion"},role:"button"}},[t._v("Ver retroalimentaciones")])],1),"Home"==t.ruta&&t.summary?s("div",{staticClass:"row justify-content-center animated fadeIn fast"},[s("h1",{staticClass:"text-center mb-4 mt-3"},[t._v("Información general")]),t._l(t.summary_usuarios,(function(a,e){return s("div",{key:e,staticClass:"card text-white bg-primary m-1",staticStyle:{"max-width":"24%"}},[s("div",{staticClass:"card-header text-center fw-bolder",staticStyle:{"font-size":"1.8rem"}},[s("span",{staticClass:"mx-1",domProps:{innerHTML:t._s(a[0])}}),t._v(" "+t._s(e.charAt(0).toUpperCase()+e.slice(1).replace("_"," ")))]),s("div",{staticClass:"card-body py-3"},[s("p",{staticClass:"card-text fw-normal text-center display-5"},[t._v(t._s(a[1]))])])])})),s("hr",{staticClass:"divider"}),s("h1",{staticClass:"text-center mb-4 mt-3"},[t._v("Información laboral")]),t._l(t.summary_dependencias,(function(a,e){return s("div",{key:e,staticClass:"card text-white bg-success m-1",staticStyle:{"max-width":"24%"}},[s("div",{staticClass:"card-header text-center fw-bolder",staticStyle:{"font-size":"1.8rem"}},[s("span",{staticClass:"mx-1",domProps:{innerHTML:t._s(a[0])}}),t._v(" "+t._s(e.charAt(0).toUpperCase()+e.slice(1)))]),s("div",{staticClass:"card-body py-3"},[s("p",{staticClass:"card-text fw-normal text-center display-5"},[t._v(t._s("nómina"==e?"$":"")+t._s(a[1]))])])])})),s("hr",{staticClass:"divider"}),s("h1",{staticClass:"text-center mb-4 mt-3"},[t._v("Información retroalimentaciones")]),t._l(t.summary_empleados,(function(a,e){return s("div",{key:e,staticClass:"card text-white bg-warning m-1",staticStyle:{"max-width":"24%"}},[s("div",{staticClass:"card-header text-center fw-bolder",staticStyle:{"font-size":"1.8rem"}},[s("span",{staticClass:"mx-1",domProps:{innerHTML:t._s(a[0])}}),t._v(" "+t._s(e.charAt(0).toUpperCase()+e.slice(1)))]),s("div",{staticClass:"card-body py-3"},[s("p",{staticClass:"card-text fw-normal text-center display-5"},[t._v(t._s(a[1]))])])])}))],2):[s("router-view")]],2)],1)},i=[],n=(s("b0c0"),s("d3b7"),s("3ca3"),s("ddb0"),{name:"Home",data:function(){return{open_sidebar:!0}},computed:{ruta:function(){return this.$route.name},summary:function(){return this.$store.state.summary},usuario:function(){var t;return null===(t=this.$store.state.usuario)||void 0===t?void 0:t.info_personal},summary_usuarios:function(){var t=JSON.parse(JSON.stringify(this.$store.state.summary)),a={"super-admins":['<i class="fas fa-user-shield"></i>',t["superadmins"]],admins:['<i class="fas fa-users-cog"></i>',t["admins"]],empleados:['<i class="fas fa-users"></i>',t["empleados"]]};return a},summary_dependencias:function(){var t=JSON.parse(JSON.stringify(this.$store.state.summary)),a={dependencias:['<i class="fas fa-cubes"></i>',t["dependencias"]],cargos:['<i class="fab fa-black-tie"></i>',t["cargos"]],"nómina":['<i class="fas fa-hand-holding-usd"></i>',t["nomina"]]};return a},summary_empleados:function(){var t=JSON.parse(JSON.stringify(this.$store.state.summary)),a={total:['<i class="fas fa-comments"></i>',t["retroalimentaciones"]],"mejor puntaje":['<i class="fas fa-thumbs-up"></i>',t["mejor_puntaje"]]};return a}},methods:{toggleSidebar:function(){this.open_sidebar=!this.open_sidebar}},components:{AppSideBar:function(){return s.e("sidebar").then(s.bind(null,"d3d4"))}}}),r=n,c=(s("1e3f"),s("2877")),o=Object(c["a"])(r,e,i,!1,null,"f1ccfa82",null);a["default"]=o.exports}}]);
//# sourceMappingURL=home.15110114.js.map