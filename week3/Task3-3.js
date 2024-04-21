fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
.then((response) => {
    //console.log(response);
    return response.text();
})
.then((data) => {
    //console.log(data)

    let str = JSON.parse(data)["data"]["results"];
    //console.log(str)
    //console.log(str["data"]["results"])

    const smlboxes = document.querySelectorAll(".smallbox img") ;
    const smlnames = document.querySelectorAll(".smallbox p") ;
    const boxes = document.querySelectorAll(".box img") ;
    const names = document.querySelectorAll(".box p") ;

    for (let i=0;i<str.length;i++){
        console.log(str[i]["stitle"])   //景點名稱
        //console.log("http"+str[i]["filelist"].split('http')[1])  //第一張照片網址
        link = "http"+str[i]["filelist"].split('http')[1];

        if (i<3){
            smlboxes[i].src = link;
            smlnames[i].textContent = str[i]["stitle"]
        }
        if (i>=3){
            boxes[i-3].src = link;
            names[i-3].textContent = str[i]["stitle"]
        }
        
        
        }
    //return response.text();
})