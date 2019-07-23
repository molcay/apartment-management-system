import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import router from './router'

import PageHeader from './components/PageHeader'
import FormInput from './components/FormInput'
import EntityActions from './components/EntityActions'

import '../node_modules/bulma/css/bulma.css'
import '../node_modules/animate.css/animate.min.css'
import './style.css'


Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.component('PageHeader', PageHeader)
Vue.component('FormInput', FormInput)
Vue.component('EntityActions', EntityActions)

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
