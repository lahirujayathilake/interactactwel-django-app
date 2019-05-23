import Vue from 'vue'
import App from './components/App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueGoogleCharts from 'vue-google-charts'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTimesCircle } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faTimesCircle)

Vue.component('font-awesome-icon', FontAwesomeIcon)


Vue.config.productionTip = false
Vue.use(BootstrapVue);
Vue.use(VueGoogleCharts)

new Vue({
    render: h => h(App),
}).$mount('#app')