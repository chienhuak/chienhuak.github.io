function inputcheck(){
    if (!document.getElementById("agree").checked){
        document.getElementById("msg").style.display = "flex"
    }
    else{
        document.forms[0].submit()
    }
    
}

function signin(){
    document.forms[1].submit()

}

// function calculate(num){
//     document.forms[1].submit()

// }