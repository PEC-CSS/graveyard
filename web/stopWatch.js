var seconds = 00;
var tens = 00;
var appendTens = document.getElementById("tens");
var appendSeconds = document.getElementById("seconds");
var buttonStart = document.getElementById("button-start");
var buttonStop = document.getElementById("button-stop");
var buttonReset = document.getElementById("button-reset");
var interval;

function startTimer() {
    tens ++;

    if (tens < 10) {
        appendTens.innerHTML = "0" + tens;
    }
    
    else {
        appendTens.innerHTML = tens;
    }

    if (tens > 99) {
        tens = 0;
        seconds ++;

        if (seconds < 10) {
            appendSeconds.innerHTML = "0" + seconds;
        }

        else {
            appendSeconds.innerHTML = seconds;
        }

        appendTens.innerHTML = "0" + 0;
    }

    if (seconds > 9) {
        appendSeconds.seconds.innerHTML = seconds;
    }
}

buttonStart.onclick = function() {
    interval = setInterval(startTimer, 10);
};

buttonStop.onclick = function() {
    clearInterval(interval);
};

buttonReset.onclick = function() {
    clearInterval(interval);
    tens = "00";
    seconds = "00";
    appendSeconds.innerHTML = seconds;
    appendTens.innerHTML = tens;
};