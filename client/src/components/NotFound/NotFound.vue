<template>
    <div class="background">
        <div class="desc-text">Please, enter data later!</div>
        <router-link to="/" class="back-home-link">BACK HOME</router-link>
    </div>
</template>

<script>
export default {
    name: 'NotFound', 
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
    background-image: url("../../assets/404.jpg");
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
.desc-text{
    font-size: 40px;
    margin: 50px;
}
</style>