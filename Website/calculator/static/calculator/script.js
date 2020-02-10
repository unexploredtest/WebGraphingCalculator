function Add(x) {
    let equation = document.getElementById("equation");
    return equation.value += x;
}
function Clear() {
    let equation = document.getElementById("equation");
    return equation.value = "";
}