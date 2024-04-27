function inputcheck(){
    if (!document.getElementById("agree").checked){
        document.getElementById("msg").style.display = "flex"
    }
    else{
        document.forms[0].submit()
    }
    
}