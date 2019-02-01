<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import GameOfLive from './components/GameOfLive/GameOfLive.vue'
import Home from './components/Home/Home.vue'
import NotFound from './components/NotFound/NotFound.vue'
import ServerError from './components/ServerError/ServerError.vue'
import UnexpectedError from './components/UnexpectedError/UnexpectedError.vue'

export default {
  name: 'app',
  components: {
    GameOfLive,
    Home,
    NotFound,
    ServerError,
    UnexpectedError
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
