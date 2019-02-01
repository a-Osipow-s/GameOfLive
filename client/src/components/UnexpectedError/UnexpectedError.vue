<template>
    <div class="background">
        <div class="desc-text">Unexpected error:(</div>
        <div>
            <router-link to="/game" class="back-home-link">ENTER DATA AGAIN</router-link>
            <router-link to="/" class="back-home-link">BACK HOME</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'UnexpectedError', 
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
    margin: 20px;
}
.desc-text {
    font-size: 40px;
    margin: 50px;
}
</style>