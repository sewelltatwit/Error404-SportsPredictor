function displayText() {
    var text = document.getElementById("result");
    if (text.style.display === "none") {
      text.style.display = "block";
    }
  }

function clear() {
    var text = document.getElementById("result");
    if (text.style.display === "block") {
      text.style.display = "none";
    }
  }