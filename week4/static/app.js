function inputcheck(){
    if (!document.getElementById("agree").checked){
        document.getElementById("msg").style.display = "flex"
    }
    else{
        document.forms[0].submit()
    }
    
}

// window.onload = function () {
//     const urlParams = new URLSearchParams(window.location.search);
//     const errorMessage = urlParams.get('error');
//     if (errorMessage) {
//         document.getElementById('errormsg').textContent = errorMessage;
//     }
// };