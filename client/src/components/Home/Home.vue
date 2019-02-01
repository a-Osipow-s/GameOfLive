<template>
    <div>
        <nav>
            <div class="nav-wrapper teal darken-1">
                <router-link to="/" class="brand-logo right">
                    GiL
                </router-link>
                <ul id="nav-mobile" class="left hide-on-med-and-down"> 
                    <li><router-link to="/">Home</router-link></li>
                    <li><router-link to="/game">Game</router-link></li>
                </ul>
            </div>
        </nav>
        <div class="content-title">
            <span class="green-color-letters"><b>GAME OF</b></span>
            <span class="green-color-letters"><b> LI</b></span>
            <span class="white-color-letters teal lighten-3"><b>VE</b></span>
        </div>
        <div class="container">
            <ul class="collection with-header">
                <li class="collection-header"><h4>Rules:</h4></li>
                <li class="collection-item">The scene of this game, the “universe,” is a surface or plane marked up into cells — infinite, bounded, or closed (in the limit, an infinite plane).</li>
                <li class="collection-item">Each cell on this surface can be in two states: to be “alive” (filled) or to be “dead” (empty). The cell has eight neighbors surrounding it.</li>
            </ul>
            <ul class="collection with-header">
                <li class="collection-header"><h4>Generation calculation:</h4></li>
                <li class="collection-item">In an empty (dead) cell, next to which there are exactly three living cells, life begins;</li>
                <li class="collection-item">If a living cell has two or three living neighbors, then that cell continues to live; otherwise, if there are less than two neighbors or more than three, the cell dies ("from loneliness" or "from overpopulation")</li>
            </ul>
            <ul class="collection with-header">
                <li class="collection-header"><h4>The game ends if:</h4></li>
                <li class="collection-item">on the field there will be no "living" cells;</li>
                <li class="collection-item">the configuration at the next step in accuracy (without shifts and turns) will repeat itself at one of the earlier steps (a periodic configuration is added)</li>
                <li class="collection-item">at the next step, none of the cells change their state (a stable configuration is formed; the previous rule degenerate to one step back)</li>
            </ul>
        </div>
        <button class="btn waves-effect waves-light" type="button" name="action" @click="goGame">Let's go!
            <i class="material-icons right">send</i>
        </button>
    </div>
</template>

<script>
export default {
    name: 'Home',
    methods: {
        goGame() {
            this.$router.push('/game');
        }
    }
}
</script>

<style scoped>
.collection-item{
    font-size: 18px;
    text-align: left;
}
.green-color-letters{
    color: #80cbc4;
}
.white-color-letters{
    color: #ffffff;
    background-image: linear-gradient(to left, rgb(57, 203, 165) 35.1%, rgb(212, 250, 240) 100%);
}
span{
    font-size: 48px;    
}
.content-title{
    margin-top: 40px;
}
</style>  
     