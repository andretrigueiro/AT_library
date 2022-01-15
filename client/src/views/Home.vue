<!--

Home view. This file setup the header part of the Home page,
which consists in the Vue logo and the introdution text.

-->

<!-- Home template, second div of the page -->
<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-6 home">
        <img alt="Bob Esponja Reading" src="../assets/reading.png">
      </div>
      <div class="col-sm-6 welcome">
        <Welcome msg="Welcome to AT_Library"/>
      </div>
    </div>
  </div>
</template>

<!-- Home script, used to pass the string contained on template to Welcome.vue script -->
<script>
// @ is an alias to /src
import Welcome from '@/components/Welcome.vue';

export default {
  name: 'Home',
  components: {
    Welcome,
  },
};
</script>

<style scoped>

.home, img {
  max-height: 80%;
  max-width: 80%;
}

</style>
