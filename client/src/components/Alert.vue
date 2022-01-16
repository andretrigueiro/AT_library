<template>
  <div>
    <b-alert variant="success" :show="5" dismissible>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
