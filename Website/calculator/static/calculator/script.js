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
function loginPage(y){
    let element = document.getElementById("login");
    if(y == 'o'){
        element.style.visibility = "visible";
    }
    else{
        element.style.visibility = "hidden";        
    }
}
