function username() {
    const unm = document.getElementById("username").value
    const name_result = document.getElementById("name_result")
    // 發送請求到後端，加載初始數據
    fetch("/api/member?username="+unm)  //fetch("http://127.0.0.1:8001/member")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if (data.data) {            
            name_result.innerText = `${data.data.name} (${data.data.username})`; //加到頁面上
        }
        else {
            name_result.innerHTML = "找不到 &#128517;"
        }

    })
    .catch(error => console.error("Error loading initial messages: ", error));
}


function update_name() {
    const unm = document.getElementById("update_name").value
    const name_result = document.getElementById("update_result")
    // 發送請求到後端，加載初始數據
    fetch("/api/member", {
        method: "PATCH" ,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "name":unm })
    })
    .then(response => response.json())
    .then(data => {
        if (data.ok) {            
            name_result.innerText = "Updated"; 
        }
        else {
            name_result.innerHTML = "Update Fail";
        }
    })
}


let rowCount = 0; 


document.addEventListener("DOMContentLoaded", function() {
    // 頁面加載完成時，加載初始數據
    loadInitialMessages();
});


function loadInitialMessages() {
    // 發送請求到後端，加載初始數據
    fetch("/loadmsg") //fetch("http://127.0.0.1:8001/loadmsg")
    .then(response => response.json())
    .then(data => {
        // 解析JSON字符串為JavaScript對象
        console.log(data)
        //const messages = JSON.parse(data);
        
        // 確保 messages 是一個陣列
        if (Array.isArray(data)) {
            // 將初始數據附加到頁面上
            appendMessagesToPage(data);
            rowCount += data.length
        } else {
            console.error("Data is not an array:", data);
        }
    })
    .catch(error => console.error("Error loading initial messages: ", error));
}


// 滾動加載
window.addEventListener('scroll', () => {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100) {
        loadMoreMessages();
    }
});



function loadMoreMessages() {
    // 發送請求到後端，獲取下一頁的留言
    // 可以使用 AJAX 或其他前端框架來實現
    fetch("/loadmsg?offset=" + rowCount)
        .then(response => response.json())
        .then(data => {
            // 將新獲取的留言附加到當前頁面上
            console.log(data)
            appendMessagesToPage(data);
            rowCount += data.length
        })
        .catch(error => console.error("Error loading more messages: ", error));
    }


function appendMessagesToPage(messages) {
    // 將新獲取的留言附加到當前頁面上的留言列表中
    // 這裡可以使用 DOM 操作或前端框架提供的功能來實現
    const messageList = document.querySelector('#message-list'); // 假設留言列表的容器有一個 ID 為 message-list

    messages.forEach(message => {
        const li = document.createElement('li');
        li.textContent = `${message.name} : ${message.content}`;

        // if (message.name === show_name) {
        //     const deleteBtn = document.createElement('a');
        //     deleteBtn.className = 'delete_btn';
        //     deleteBtn.href = `/deleteMessage/${message.id}`;
        //     deleteBtn.textContent = 'x';
        //     li.appendChild(deleteBtn);
        // }

        messageList.appendChild(li);
    });
}
