import Vue from 'vue'
import App from './components/App.vue'
import BootstrapVue from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(BootstrapVue);

new Vue({
  render: h => h(App),
}).$mount('#app')
