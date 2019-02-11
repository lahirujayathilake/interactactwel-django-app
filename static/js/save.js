$(document).ready(function () {

    function saveStep1(){
    var inputEmail= document.getElementsByName("step1-0");
    localStorage.setItem("step1-0", inputEmail.value);
    }

    var storedValue = localStorage.getItem("step1-0");
    console.log(storedValue);

});