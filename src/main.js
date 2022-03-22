import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

// axios
import axios from 'axios'
Vue.prototype.$http = axios

Vue.prototype.$hostname = 'http://127.0.0.1:4211/api'
Vue.prototype.$public_url = 'http://127.0.0.1:4211/productImage/'

Vue.prototype.$config = {
  headers: {
    Authorization: "Bearer " + localStorage.token,
  },
}
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
