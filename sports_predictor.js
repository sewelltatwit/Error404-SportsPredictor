function displayText() {
    var text = document.getElementById("result");
    if (text.style.display === "none") {
        text.style.display = "block";
    }
}

function clear() {
    document.getElementById("result").style.display = "none";
}