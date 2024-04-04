/*
document.getElementById('popup-btn').addEventListener('click', function() {
    var navUl = document.querySelector('nav ul');
    if (navUl.classList.contains('show')) {
        navUl.classList.remove('show');
    } else {
        navUl.classList.add('show');
    }
});
*/

/*
function myFunction() {
    //var navUl = document.getElementById("popup-btn");
    var menu = document.getElementById("popup-menu");
    var icon = document.getElementById("popup-btn");
    
    if (menu.style.display === "none") {
        menu.style.display = "block";
      //icon.innerText = " + "; // 顯示時切換為 Hide icon
    } else {
        menu.style.display = "none";
      //icon.innerText = " - "; // 隱藏時切換為 Expand icon
    }
  }
*/
  
function myFunctionP() {
    var menu = document.getElementById("sidebar");
    var links = document.querySelectorAll(".popup-menu a");
    var icon = document.getElementById("toggleIcon").src; // 修改此行，將 icon 變數設置為圖片元素的 src 屬性

    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "block";
        //icon.src = "redcross.png"; // 顯示時切換為 X 圖示
        document.getElementById('toggleIcon').src  = 'redcross.png';
        links.forEach(function(link) {
            link.style.display = "block";
        });
    } else {
        menu.style.display = "none";
        //icon.src = "burgericon.png"; // 隱藏時切換為漢堡圖示
        document.getElementById('toggleIcon').src  = 'burgericon.png';
    }
}



/*
function myFunction() {
  document.getElementById('popup-btn').addEventListener('click', function() {
    var menu = document.getElementById("popup-menu");
    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "flex";
    } else {
        menu.style.display = "none";
    }
});
}
*/


/*
// 获取下拉按钮和下拉内容
var dropdownBtn = document.querySelector('.popup-btn');
var dropdownContent = document.querySelector('.popup-menu');

// 点击按钮时显示或隐藏下拉内容
dropdownBtn.addEventListener('click', function() {
    dropdownContent.classList.toggle('show');
});

// 在点击按钮之外的地方点击时隐藏下拉内容
window.addEventListener('click', function(event) {
    if (!event.target.matches('.popup-btn')) {
        var dropdowns = document.getElementsByClassName('popup-menu');
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
});
*/


/*
// 获取下拉按钮和下拉内容
var dropdownBtn = document.querySelector('.popup-btn');
var dropdownContent = document.querySelector('.popup-menu');

// 点击按钮时显示或隐藏下拉内容
dropdownBtn.addEventListener('click', function() {
    dropdownContent.classList.toggle('show');
});

// 在点击按钮之外的地方点击时隐藏下拉内容
window.addEventListener('click', function(event) {
    if (!event.target.matches('.popup-btn')) {
        var dropdowns = document.getElementsByClassName('popup-menu');
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
});
*/


