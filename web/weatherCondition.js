var button = document.querySelector('.button');
var input = document.querySelector('.inputValue');
var name = document.querySelector('.name');
var desc = document.querySelector('.desc');
var temp = document.querySelector('.temp');

button.addEventListener('click', function() {
    fetch('https://api.openweathermap.org/data/2.5/weather?q='+input.value+'&appid=6c124303bc114d57f819f29aba5e9e9c')
    .then(response => response.json())
    .then(data => {
        var nameValue = data['name'];
        var tempValue = data['main']['temp'];
        var descValue = data['weather'][0]['description'];

        name.innerHTML = nameValue;
        temp.innerHTML = tempValue;
        desc.innerHTML = descValue;
    })

.catch(err => alert("ERROR : Wrong city name!"))
});