import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Materialize from 'materialize-css'
import NotFound from './components/NotFound/NotFound.vue'
import ServerError from './components/ServerError/ServerError.vue'
import GameOfLive from './components/GameOfLive/GameOfLive.vue'
import UnexpectedError from './components/UnexpectedError/UnexpectedError.vue'
import Home from './components/Home/Home.vue'
import VueResource from 'vue-resource'
import 'materialize-css/dist/css/materialize.css'
import 'materialize-css/dist/js/materialize.js'

Vue.use(VueResource)
Vue.use(VueRouter)
Vue.use(Materialize)
Vue.config.productionTip = false

const routes = [
  {path: '/game', component: GameOfLive},
  {path: '/unexpected-error', component: UnexpectedError},
  {path: '/404', component: NotFound},  
  {path: '/500', component: ServerError},
  {path: '*', redirect: '/404'},  
  {path: '/', component: Home}
];

const router = new VueRouter({
  routes,
  mode: 'history'
});

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
