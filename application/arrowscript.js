function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }
  
function myFunction() {
    var x = document.getElementById("myDIV");
    var icon = document.getElementById("toggleIcon");
    
    if (x.style.display === "none") {
      x.style.display = "block";
      icon.innerText = " ▲(Click to hide)"; // 顯示時切換為 Hide icon
    } else {
      x.style.display = "none";
      icon.innerText = " ▼(Click to expand)"; // 隱藏時切換為 Expand icon
    }
}
















  function myFunction() {
    var x = document.getElementById("myDIV");
    var icon = document.getElementById("toggleIcon");
    
    if (x.style.display === "none") {
      x.style.display = "block";
      icon.innerText = " ▲(Click to hide)"; // 顯示時切換為 Hide icon
    } else {
      x.style.display = "none";
      icon.innerText = " ▼(Click to expand)"; // 隱藏時切換為 Expand icon
    }
  }