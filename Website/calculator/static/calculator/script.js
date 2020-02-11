function Add(x) {
    let equation = document.getElementById("equation");
    let functionDisplay = document.getElementById("functionDisplay");
    equation.value += x;
    functionDisplay.innerHTML += x;
}
function Clear() {
    let equation = document.getElementById("equation");
    let functionDisplay = document.getElementById("functionDisplay");
    equation.value = "";
    functionDisplay.innerHTML = "";
}
