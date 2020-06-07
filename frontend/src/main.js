import Vue from "vue";
import App from "./App.vue";
import "@/assets/css/tailwind.css";
import VueRouter from "vue-router";
import routes from "./router";
import "@fortawesome/fontawesome-free/css/all.css";
import "@fortawesome/fontawesome-free/js/all.js";

Vue.config.productionTip = false;
Vue.use(VueRouter);
const router = new VueRouter({ mode: "history", routes });

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
