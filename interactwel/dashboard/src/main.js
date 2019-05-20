import Vue from 'vue'
import App from './components/App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueGoogleCharts from 'vue-google-charts'
//import L from 'vue2-leaflet'


Vue.config.productionTip = false
Vue.use(BootstrapVue);
Vue.use(VueGoogleCharts)

new Vue({
    render: h => h(App),
}).$mount('#app')
