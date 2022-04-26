import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import userPlugin from "./components/common/UserPlugin.js";
import StarRating from 'vue-star-rating';

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import router from './router';
import store from "./store";
import App from './App.vue';
import VueFilterDateFormat from 'vue-filter-date-format';
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";

Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('star-rating', StarRating);
Vue.component("v-select", vSelect);

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(userPlugin);
Vue.use(VueFilterDateFormat);

//toast options
const toasterOptions = {
  // You can set your default options here
  timeout: 5000,
};
Vue.use(Toast, toasterOptions);

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app');
