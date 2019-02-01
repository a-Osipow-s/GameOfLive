<template>
    <div class="background">
        <div class="desc-text">Server denied:(</div>
        <router-link to="/" class="back-home-link">BACK HOME</router-link>
    </div>
</template>

<script>
export default {
    name: 'ServerError', 
    data: function() {
        return {

        }
    }
}
</script>

<style scoped>
.background {
    width: 100%;
    height: 100vh;
    background-image: url("../../assets/500.png");
    background-repeat: no-repeat;
    background-position: center center;
    padding-bottom: 60px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.back-home-link {
    color: #00897b;
}
.desc-text {
    font-size: 40px;
    margin: 50px;
}
</style>