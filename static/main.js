//review classes in js
class BoggleGame {
    constructor() {
    this.score = 0;
    this.timer = 60;
    this.words = new Set();
    this.setTimer = setInterval(this.tick.bind(this), 1000)
    this.showTimer() 
//theris: this.board = $("#" + boardId);

//calls method handleEvent from immediately below
//theirs:     $(".add-word", this.board).on("submit", this.handleSubmit.bind(this));
    $('form').on('submit', this.handleEvent);
    }
//don't need 'function' after async
    async handleEvent(event) {
        event.preventDefault();
//review method calls in class
//--select the word guessed; first select input element
        let input = $('input');
        //--assign value from input element
        let inputValue = input.val();
        if(!inputValue) {
            return
        }
        if(inputvalue.in(this.words)) {
            $('.msg').text(`Already found this ${inputValue}`)
        }
//-- check server for validity; uses route /handle_quess
//--wny not post?
        const response = await axios.get('/handle_guess', {params: {inputValue : inputValue}});
//their code:
        if (response.data.result === "not-word") {
            $('.msg').empty()
            $('.msg').text(`${inputValue} is not a valid English word`);
//--if server response has 'not-on'board, use showMessage method
        } else if (response.data.result === "not-on-board") {
            $('.msg').empty()
            $('.msg').text(`${inputValue} is not a valid word on this board`);
//--if not one of the first two, then the word is valid
        } else {
//has the object already been instantiated and this stores a new value for the this.score attribute?
            this.score += inputValue.length;
            this.words.add(inputValue);
            $('div').innerHTML('')
            $('div').append(`Added ${inputValue}`)
            $('div').append(`${this.score} is your score`)

            msg.text("Well done!")
            input.val('')
        }
    }    

    showTimer() {
        // Implement your logic to display the timer in the UI
        $('.timer').text(this.secs)
        console.log(`Seconds Left: ${this.timer}`);
    }

    async tick() {
        this.secs -= 1;
        this.showTimer();
    
        if (this.secs === 0) {
            clearInterval(this.timer);
            await this.scoreGame();
        }
    }
    
      /* end of game: score and update message. */
    //
    async scoreGame() {
    //.add-word is form class; so hide form
        $(".add-word").hide();
    //--post-score end path returns jsonify; post with info 'score'; will pass to score = request.json["score"]
        const response = await axios.post("/gameover", { score: this.score });
        // if (respsonse.data.brokeRecord) {
        //     this.showMessage(`New record: ${this.score}`, "ok");
        $('div').innerHTML('')
        $('div').append(`Final score: ${score}`);
        
    }
}
