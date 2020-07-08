function displayText() {
    var text = document.getElementById("txtResult");
    if (text.style.display === "none") {
        text.style.display = "block";
    }
}

function clear() {
<<<<<<< HEAD
    var text = document.getElementById("result");
    if (text.style.display === "block") {
      text.style.display = "none";
    }
  }


 function populateSecond() {
    var firstDropdown = document.getElementById("ddlTeamOne");
    var firstTeam = firstDropdown.options[e.selectedIndex].text;
    var secondDropdown = document.getElementById("ddlTeamTwo");
    const { spawn } = require('child_process');
    const sensor = spawn('python', ['sensor.py']);
    sensor.stdout.on('data', function(data) {

    // convert Buffer object to Float
    temperatures.push(parseFloat(data));
    console.log(temperatures);
});
 }
=======
    document.getElementById("result").style.display = "none";
}
>>>>>>> c3becaa095ac7f305d5fd42f0b2820e2a9b25dc2
