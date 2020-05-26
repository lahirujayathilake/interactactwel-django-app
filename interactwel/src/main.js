import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import router from './router'
import store from "./store";
import App from './App.vue'

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.use(BootstrapVue);

new Vue({
    store,
    router,
  render: h => h(App),
}).$mount('#app')
