//Task 1

const stations = [
    {"n":'Xindian',"idx":0}, {"n":'Xindian City Hall',"idx":1}, {"n":'Qizhang',"idx":2}, {"n":'Dapinglin',"idx":3},
    {"n":'Xiaobitan',"idx":1, "branch":"Qizhang"}, {"n":'Jingmei',"idx":4},{"n":'Wanlong',"idx":5}, {"n":'Gongguan',"idx":6},
    {"n":'Taipower Building',"idx":7}, {"n":'Guting',"idx":8}, {"n":'Chiang Kai-Shek Memorial Hall',"idx":9},
    {"n":'Xiaonanmen',"idx":10}, {"n":'Ximen',"idx":11}, {"n":'Beimen',"idx":12}, {"n":'Zhongshan',"idx":13},
    {"n":'Songjiang Nanjing',"idx":14}, {"n":'Nanjing Fuxing',"idx":15}, {"n":'Taipei Arena',"idx":16},
    {"n":'Nanjing Sanmin',"idx":17}, {"n":'Songshan',"idx":18}]


function distance(start, end){

    sb = false;
    eb = false;

    if ("branch" in start){
        for (const station of stations){
            if (station["n"] == start["branch"]){
                sb = station;    //找出主線上的分支位置
                break;
            }
        }
    }

    if ("branch" in end){
        for (const station of stations){
            if (station["n"] == end["branch"]){
                eb = station;
                break;
            }
        }
    }

    // console.log(start)
    // console.log(end)
    // console.log("sb "+sb.toString())
    // console.log("tb "+eb.toString())

    if (sb == false){
        if (eb == false){
            //console.log(start["idx"]);
            return Math.abs(start["idx"]-end["idx"])   //都不在支線
        }
        else{
            return Math.abs(start["idx"]-eb["idx"])+Math.abs(end["idx"])   //末站 在支線
        }
    }
    else{
        if (eb == false){
            return Math.abs(sb["idx"]-end["idx"])+Math.abs(start["idx"])   //起站 在支線
        }
        else if (sb["n"] != eb["n"]){            
            return Math.abs(sb["idx"]-destbranch["idx"])+Math.abs(start["idx"])+Math.abs(dest["idx"])   //兩點都在支線上
        }
        else{
            return Math.abs(sb["idx"]-eb["idx"])
        }
    }


    
}


function findAndPrint(messages, currentStation){
    // your code here

    //擷取訊息
    const extractedMessages = [];

    for (const [name, message] of Object.entries(messages)) {   // 每個 messages 物件中的鍵值對
        for ( const station of stations) {    // 每個站名，使用正則表達式來匹配站名
            const regex = new RegExp(station["n"], 'gi'); // 不區分大小寫、全域匹配
            if (regex.test(message)) {
                let obj = {};
                obj["name"] = name;
                obj["at"] = station;
                extractedMessages.push(obj)
            }
        }
    }
    //console.log(extractedMessages);   //檢查擷取的訊息
    
    myloc = ""

    //算出我的位置
    for (const station of stations){
        if (currentStation == station["n"]){
            myloc = station
        }
    };
    //console.log(myloc);   //{ n: 'Jingmei', idx: 4 }


    //找最近的距離
    let minSta = {"msg":null,"d":9999};
    for (const msg of extractedMessages){
        //console.log(distance(msg["at"],myloc))
        let d=distance(msg["at"],myloc);
        if(minSta["d"]>d) {
            minSta["d"]=d;
            minSta["msg"]=msg;
        }

    }

    console.log(minSta["msg"]["name"])
}

const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
    //,"John": "I'm at Xindian City Hall waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian
findAndPrint(messages, "Dapinglin"); // print Mary


// function findAndPrint(messages, currentStation){
//     // your code here

//     const stations = ['Xindian','Xindian City Hall','Qizhang','Xiaobitan','Dapinglin','Jingmei','Wanlong','Gongguan','Taipower Building','Guting','Chiang Kai-Shek Memorial Hall','Xiaonanmen','Ximen','Beimen','Zhongshan','Songjiang Nanjing','Nanjing Fuxing','Taipei Arena','Nanjing Sanmin','Songshan'];

//     //擷取訊息
//     const extractedMessages = {};

//     for (const [name, message] of Object.entries(messages)) {   // 每個 messages 物件中的鍵值對
//         for (const station of stations) {    // 每個站名，使用正則表達式來匹配站名
//             const regex = new RegExp(station, 'gi'); // 不區分大小寫、全域匹配
//             if (regex.test(message)) {
//                 extractedMessages[name] = station;
//             }
//         }
//     }
//     //console.log(extractedMessages);   //檢查擷取的訊息
//     //console.log(extractedMessages.Vivian);   //取得Vivian的車站


//     //算出我的位置
//     for (let i=0;i<stations.length;i++){
//         if (currentStation.includes(stations[i])){
//             myloc = i;
//         }
//     };
//     //console.log(myloc);
//     //console.log("我的車站："+stations[myloc]+"我的索引："+myloc);

//     //計算最近的距離
//     descS = []

//     //字典不能用forEach
//     // extractedMessages.forEach(element => {
//     //     desc = Math.abs(stations.indexOf(extractedMessages.element)-myloc)
//     //     descS.push(desc)      
//     // });

//     const keys = Object.keys(extractedMessages);

//     descS = []
//     for (i=0;i<keys.length;i++){
//         desc = Math.abs(stations.indexOf(extractedMessages[keys[i]])-myloc)   //不能寫stations.indexOf(extractedMessages.keys[i])
//         descS.push(desc)
//     }
//     //console.log(Math.min(...descS))
//     console.log(keys[descS.indexOf(Math.min(...descS))])   //距離最近的人

// }
//     const messages={
//     "Bob":"I'm at Ximen MRT station.",
//     "Mary":"I have a drink near Jingmei MRT station.",
//     "Copper":"I just saw a concert at Taipei Arena.",
//     "Leslie":"I'm at home near Xiaobitan station.",
//     "Vivian":"I'm at Xindian station waiting for you."
//     //,"John": "I'm at Xindian City Hall waiting for you."
//     };
//     findAndPrint(messages, "Wanlong"); // print Mary
//     findAndPrint(messages, "Songshan"); // print Copper
//     findAndPrint(messages, "Qizhang"); // print Leslie
//     findAndPrint(messages, "Ximen"); // print Bob
//     findAndPrint(messages, "Xindian City Hall"); // print Vivian



console.log()
//Task 2:

// your code here, maybe
function book(consultants, hour, duration, criteria){
    // your code here
    consultants.forEach(element => {
        if (!element.hasOwnProperty('time')){
            element['time']= [];
            //console.log(element)
        }
    });

    let avaliables = []
    consultants.forEach(element => {
        avaliables.push(element['name'])}    ) //所有顧問清單
    //console.log(avaliable)

    //找到有空顧問
    for (t=hour;t<hour+duration;t++){
        consultants.forEach(consultant => {
            if (consultant.time.includes(t)){    //不能用in檢查
                const index = avaliables.indexOf(consultant.name);
                if (index !== -1) {
                    avaliables.splice(index, 1); // 使用 splice() 方法刪除指定索引的元素 (修正:avaliables.pop(consultant)注意:pop()只能移除最後一項，無法指定移除的東西)
                }
            }
        });
    }
    //console.log(avaliables)  //檢查：

    //沒有顧問的情況
    if (avaliables.length === 0){     //使用 avaliables == [] 比較，不會產生預期的結果 (因為是比較 "存儲在變數中的記憶體位置")
        console.log("No Service")
        return;
    }

    

    //判斷價格條件
    if (criteria="price"){
        //尋找有空顧問最低價格
        let avaPrices = []
        avaliables.forEach(element1 => {
            consultants.forEach(element2 =>{
                if (element1 == element2.name){
                    avaPrices.push(element2.price) 
                    //console.log(element2.price) //檢查：新增正確的值
                }
            }
        )
        }
        )
        //console.log(avaPrices)
        //console.log(Math.min(...avaPrices))  //檢查min值：因為Math.mim()的參數必須是數字，將展開運算符傳給Math.mim()
        minPrice = Math.min(...avaPrices) //找到最低價格

        consultants.forEach(element => {
            if (element.price == minPrice){    //依最低價格推算出顧問名稱，將該顧問時間預定
                console.log(element.name)
                element.time.push(hour)
                if (duration >1 ){
                    for (t=1;t<duration;t++){
                        hour += 1
                        element.time.push(hour)
                    }
                }           
            }
        })
        
    }

    //判斷評分條件
    if (criteria="rate"){
        //尋找有空顧問最高分
        let avaRates = []
        avaliables.forEach(element1 => {
            consultants.forEach(element2 =>{
                if (element1 == element2.name){
                    avaRates.push(element2.price) 
                }
            }
        )
        }
        )

        maxRate = Math.max(...avaRates) 

        consultants.forEach(element => {
            if (element.rate == maxRate){    
                console.log(element.name)
                element.time.push(hour)
                if (duration >1 ){
                    for (t=1;t<duration;t++){
                        hour += 1
                        element.time.push(hour)
                    }
                }           
            }
        })
        
    }


    //console.log(consultants)

    }
    const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
    ];
    book(consultants, 15, 1, "price"); // Jenny
    book(consultants, 11, 2, "price"); // Jenny
    book(consultants, 10, 2, "price"); // John
    book(consultants, 20, 2, "rate"); // John
    book(consultants, 11, 1, "rate"); // Bob
    book(consultants, 11, 2, "rate"); // No Service
    book(consultants, 14, 3, "price"); // John

    console.log()
//Task 3:

function func(...data){
    // your code here
    rule = {2:1,3:1,4:2,5:2}; //名字字數與索引
    
    let words = [];
    for (i=0;i<data.length;i++){
        digit = data[i].length;  //名字長度
        middle = rule[digit];  //中間位置index
        words.push(data[i][middle]); //將中間字存到新的陣列
        
        //console.log(word);
    }
    //console.log(words);
    
    let freq = {};      //計算每個元素的出現次數
    words.forEach(element => {
        if (element in freq){
            freq[element] +=1;
        }
        else {
            freq[element] = 1;
        }
        
    });
    
    //console.log(freq)

    let check = false;
    words.forEach(word => {
        if (freq[word]==1){
            index = words.indexOf(word)
            console.log(data[index])  //印出"中間名"特別的人
            check = true;
        }
    })

    if (check == false){
        console.log("沒有")
    }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

console.log()
//Task 4:尋找數列規則 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, ...

function getNumber(index){
    // your code here
    let sum = 0;
    for (let i=1;i<index+1;i++){
        if ((i)%3==0){
            sum=sum-1; 
        }
        else {
            sum=sum+4;  
        }
    
    }
    console.log(sum);    
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70

// //Task 5 (Optional):

// function find(spaces, stat, n){
//     // your code here
//     }
//     find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
//     find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
//     find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2