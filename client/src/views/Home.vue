<!--

Home view. This file setup the header part of the Home page,
which consists in the Vue logo and the introdution text.

-->

<!-- Home template, second div of the page -->
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<!-- Home script, used to pass the string contained on template to HelloWorld.vue script -->
<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';

export default {
  name: 'Home',
  components: {
    HelloWorld,
  },
};
</script>
