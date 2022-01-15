/*

File to define URLs and map components

*/

// imports
import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Books from '../components/Books.vue';
import Ping from '../components/Ping.vue';

// vue setup
Vue.use(VueRouter);

// Define routes
const routes = [
  {
    path: '/books',
    name: 'Books',
    component: Books,
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
];

// Router instance
const router = new VueRouter({
  // hash mode (default) contains # in URL, which history mode doesn't
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
