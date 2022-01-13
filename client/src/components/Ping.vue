<!--

Ping component. Just for tests.

-->

<!-- Simple template, just for tests.-->
<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<!-- Simple template, just for tests.-->
<script>
// importing axios library to sendo AJAX requests
// and connect the client-side Vue app with the back-end Flask app
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'Pang?',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
