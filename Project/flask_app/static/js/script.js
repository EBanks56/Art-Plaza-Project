function request() {
    alert("Your Purchase Request Has Been Sent.")
}

function notavailable(){
    alert("Sorry this function is not available at the moment. Try again later.")
}

function toggleP(){
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function toggleC(){
    var x = document.getElementById("confirmPassword");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}