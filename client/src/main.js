/*

App entry point, which loads and initializes Vue along with the root component (App.vue).

*/

// imports
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

// enable the bootstrap vue
Vue.use(BootstrapVue);

// prevent the production tip on Vue startup -???
Vue.config.productionTip = false;

// Initiate the app
new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
