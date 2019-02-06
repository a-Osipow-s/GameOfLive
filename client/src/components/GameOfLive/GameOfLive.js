export default {
  name: 'GameInLive',
  data: function () {
    return{
      aliveCons: [],
      stopGame: false,
      visabilityBtnStopGame: false,
      visabilityGameField: true,
      startActiveBtn: false,
      width: {
        value: 5,
        maxValue: 50,
        minValue: 0
      },
      height: {
        value: 5,
        maxValue: 20,
        minValue: 0
      },
      time: {
        value: 5,
        maxValue: 10,
        minValue: 0
      }
    }
  },
  methods: {
    cleanGameField: function() {
      this.visabilityGameField = !this.visabilityGameField
      this.visabilityStopGame = false
      if(this.aliveCons.length) {
        this.aliveCons.length = 0
      }
    },

    editField: function() {
      this.stopGameOfLive()
      this.startActiveBtn = false
      this.cleanGameField()
    },

    isRequiredField: function(value) {
      return !(value == '')
    },

    isValidInputRange: function(value, maxValue, minValue) {
      return !(value > maxValue || value <= minValue) 
    },

    isValidInputSymbol: function(value) {
      return !(isNaN(value))
    },

    isValidData: function(arrayCheckedFields, ) {
      for(var i=0;i<arrayCheckedFields.length;i++) {
        if(!this.isRequiredField(arrayCheckedFields[i].value)) {
          return false
        }
        if(!this.isValidInputSymbol(arrayCheckedFields[i].value)) {
          return false
        }
        if(!this.isValidInputRange(arrayCheckedFields[i].value, 
                                   arrayCheckedFields[i].maxValue, 
                                   arrayCheckedFields[i].minValue)) {
          return false    
        }
      }
      return true
    },

    createLivingCellWithRandom: function() {
      if(this.aliveCons.length) {
        this.aliveCons.length = 0
      }
      for(let i=0;i<this.height.value;i++) { 
        for(let j=0;j<this.width.value;j++) { 
          if(Math.floor(Math.random() * 6) == 1) {
            this.aliveCons.push([i, j])
          }
        }
      }
      this.aliveCons.length ? this.startActiveBtn = true : this.startActiveBtn = false  
    },

    createLivingCellWithClick: function(n, k) {
      if(this.isAliveCell(n, k)) {
        const toStringArrayAliveCons = this.aliveCons.toString()
        const clickedArray = [n, k].toString()
        const position = toStringArrayAliveCons.indexOf(clickedArray)
        this.aliveCons.splice(position, 1) 
      }
      else { 
        this.aliveCons.push([n, k])
      }
      this.aliveCons.length ? this.startActiveBtn = true : this.startActiveBtn = false
    },

    setWidthGameField: function() {
      const gameFieldSize = {
        30: '900px',
        20: '700px',
        15: '500px',
        10: '350px',
        5: '150px',
        2: '50px'
      }
      for(let key in gameFieldSize) {
        if(key >= this.width.value && this.width.value <= 30) {
          return gameFieldSize[key]
        }
      }
    },

    renderError: function(status) {
      const arrayErrorStatus = {
        404: '/404',
        500: '/500'
      }
      if(status in arrayErrorStatus) {
        this.$router.push(arrayErrorStatus[status])
      }
      else if(status == 400) {
        this.$router.push('/game')
        alert("The server received incorrect data, please enter the data again!")
      }
      else {
        this.$router.push('/unexpected-error')
      }
    },

    isAliveCell: function(n, k) {
      return this.aliveCons.some(item => {return item.toString() === [n, k].toString()})
    },

    getNextBoard: function(url, board, width, height, lastStep) {
      this.aliveCons = board
      if(this.aliveCons.length && !lastStep && !this.stopGame) {
        this.postRequest(url, this.aliveCons, width, height)
      }
      else {
        this.stopGameOfLive()
      }
    },

    postRequest: function(url, board, width, height) {
      this.visabilityBtnStopGame = true
      this.stopGame = false
      this.$http.post(url,{
        board: board,
        width: width,
        height: height
      }).then(function(Response) {
        console.log(Response)
        setTimeout(()=>{
          this.getNextBoard(url, Response.body.board_next_step, width, height, Response.body.last_step)},
          this.time.value * 1000);
      }).catch(function(error) {
        this.renderError(error.status)
      })
    },

    stopGameOfLive: function() {
      this.stopGame = true
      this.visabilityBtnStopGame = false
    },

    backHome: function() {
      this.$router.push('/')
      this.stopGameOfLive()
    }
  }
}