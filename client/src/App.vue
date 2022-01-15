<!--

Main vue, Root component. This file setup the front-end application.
It shows the sections, like Home and About, and you can choose one of them,
which changes the restant of the page acoording to the choice.

-->

<!-- First template of the page, with the sections -->
<template>
  <div id="app">
    <div class="header">
      <div id="nav">
        <router-link to="/">Home</router-link> |
        <router-link to="/books">Books</router-link> |
        <router-link to="/about">About</router-link> |
        <router-link to="/ping">Ping</router-link>
      </div>
    </div>
    <router-view class="standard view"></router-view>
  </div>
</template>

<!-- Main style of the page. It sets some general attributes like test-align -->
<style>

#app {
  background-color: #f3ad78;
}

.header {
  background-color: #e8804c;
  padding-top: 40px;
  margin-bottom: 50px;
}

#nav {
  text-align: right;
  font-size: 20px;
  margin-right: 5%;
}

#nav a{
  color: white;
}

</style>
