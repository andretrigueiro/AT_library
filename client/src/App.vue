<!--

Main vue, Root component. This file setup the front-end application.
It shows the sections, like Home and About, and you can choose one of them,
which changes the restant of the page acoording to the choice.

-->

<!-- First template of the page, with the sections -->
<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/ping">Ping</router-link>
    </div> -->
    <router-view class="standard view"></router-view>
  </div>
</template>

<!-- Main style of the page. It sets some general attributes like test-align -->
<style>
#app {
  margin-top: 60px
}
</style>
