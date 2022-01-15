<!--

Hello World component. It displays the home page after the second div,
which is the Home view.

-->

<template>
  <div class="welcome">
    <h1>{{ msg }}</h1>
    <p>
      AT_Library is a study project, developed by André Trigueiro.
    </p>
    <p>
      Check out the
      <a href="http://localhost:8080/books" target="_blank" rel="noopener">Books Section</a>
      to see the project.
    </p>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.welcome h1 {
  margin-bottom: 25px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: whitesmoke;
  font-weight: bold;
}
</style>
