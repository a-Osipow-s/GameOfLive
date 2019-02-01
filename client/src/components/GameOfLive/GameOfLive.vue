e<template>
  <div class="container">
    <div v-if="visabilityGameField" class="wrapper-inputs-size">
      <h2>Please, enter data</h2>
      <p class="description-enter-data">Enter the size of the playing field, I am one generation time. 
        <br>(the size is indicated in the cells, the lifetime of one generation in seconds)
      </p>
      <div>
        <label><b>Width:</b></label>
        <input type="text"
              v-model.number="width.value" placeholder="max size: 50" 
              v-bind:class="{'validate':isValidData([width]),
                             'invalid':!isValidData([width])}"/>
      </div>
      <div>
        <label><b>Height</b></label>
        <input type="text" 
              v-model.number="height.value" placeholder="max size: 20" 
              v-bind:class="{'validate':isValidData([height]), 
                             'invalid':!isValidData([height])}"/>
      </div>
      <div>
        <label><b>Time(s)</b></label>
        <input type="text" 
              v-model.number="time.value" placeholder="max time: 10"
              v-bind:class="{'validate':isValidData([time]), 
                             'invalid':!isValidData([time])}"/>
      </div>
      <a class="waves-effect waves-light btn create-field-btn" 
        v-bind:class="{'disabled':!isValidData([width, height, time])}"
        v-on:click="cleanGameField()">create game field</a>
    </div>

    <table v-if="!visabilityGameField" 
           v-bind:style="{width:setWidthGameField()}">
      <tbody>
        <tr v-for="n in height.value" :key="n">
          <td v-for="k in width.value" :key="k" 
              v-on:click="createLivingCellWithClick(n, k)"
              v-bind:class="{'isAlive': isAliveCell(n, k)}"></td>
        </tr>
      </tbody>
    </table>

    <div class="initial-position-buttons" v-if="!visabilityGameField">
      <a class="waves-effect waves-light btn" v-on:click="editField()">edit size and time</a>
      <p class="description-position">Set the initial location of living cells or using random</p>
      <a class="waves-effect waves-light btn"
        v-on:click="createLivingCellWithRandom()"
        v-bind:class="{'disabled': visabilityBtnStopGame}">random</a>
      <a class="waves-effect waves-light btn" 
        v-bind:class="{'disabled': !startActiveBtn}"
        v-if="!visabilityBtnStopGame"
        v-on:click="postRequest('http://0.0.0.0:7000/api/game-of-live/', aliveCons, width, height)">start game</a>
      <a class="waves-effect waves-light btn" 
        v-on:click="stopGameOfLive()"
        v-if="visabilityBtnStopGame">stop game</a>
    </div> 

   <footer>
      <a class="back-home-link"
        v-on:click="backHome()">BACK HOME</a>
    </footer>
  </div>
</template>

<script src = "./GameOfLive.js"></script>
<style scoped src = "./GameOfLive.css"></style> 