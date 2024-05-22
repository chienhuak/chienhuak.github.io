from fastapi import FastAPI, Form, Request, Response, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
import os
from datetime import datetime
from fastapi.responses import JSONResponse
import json

# PS C:\Users\User\Documents\GitHub\chienhuak.github.io\week6> python -m uvicorn main:app --port 8001 --reload
# python -m uvicorn main:app --reload

app = FastAPI(debug=True)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# 設定 SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="some-random-string")

# 從環境變數中讀取 MySQL 密碼
mysql_password = os.environ.get("MYSQL_PASSWORD")
print(mysql_password)
# 建立 MySQL 連接
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=mysql_password,
    database="website"
    )


@app.get("/api/user", response_class=JSONResponse)
async def member(request: Request):
    print(request.session['SIGNED-IN'])
    if request.session['SIGNED-IN'] == True:
        return {"data":{"name":request.session['NAME'],"id":request.session['USERID']}}
    else:
        return {"error":True}



# 修改姓名
@app.patch("/api/member", response_class=JSONResponse)
async def update_name(request: Request, me:dict):
    if not request.session['SIGNED-IN']:
        return {"error": True}

    print(me)
    try:
        with mydb.cursor(buffered=True,dictionary=True) as mycursor :
            query = """
                UPDATE member
                SET name = %s
                WHERE id = %s
                """
            
            mycursor.execute(query, (me['name'],request.session['USERID']))
            mydb.commit()
            return {"ok":True}

    except error as e:
        return {"error": True}
    


# 查詢會員功能
@app.get("/api/member", response_class=JSONResponse)
async def search_name(request: Request, username:Optional[str]):
    if not request.session['SIGNED-IN']:
        return {"data": None}  # 沒有登入

    print(username)
    if not username:
        return {"data": None}  # 沒有輸入資料

    try:
        with mydb.cursor(buffered=True,dictionary=True) as mycursor :
            query = """
                SELECT name, username, id
                FROM member 
                WHERE username LIKE %s 
                """
            search_pattern = f"%{username}%"
            mycursor.execute(query, (search_pattern,))
            result = mycursor.fetchone()
            print(result)
            if result:
                return {"data": result}
            else:
                return {"data": None}  # 搜尋不到結果

    except error as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/",response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/signin",response_class=HTMLResponse)
async def signin(request: Request, username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    with mydb.cursor() as mycursor :
        query = "SELECT * FROM member where username = %s AND password = %s"
        inputs = (username,password)
        mycursor.execute(query, inputs)
        result = mycursor.fetchall()
    if result:
        # 登入成功，將使用者狀態設置為已登入
        request.session['SIGNED-IN'] = True
        request.session['NAME'] = result[0][1]
        request.session['USERID'] = result[0][0]
        #登入成功，導向到會員頁面
        #如果沒有提供 status_code 參數，則 FastAPI 將使用默認的狀態碼，但這可能不是你想要的。因此，你需要明確指定。 
        return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)
        # return templates.TemplateResponse("member.html",{"request":Request})
    if username is None or password is None:
        # error_msg = "缺少帳號或密碼"
        return RedirectResponse(url="/error?msg=no_username_or_password", status_code=status.HTTP_303_SEE_OTHER)
    else:
        # 登入失敗，返回登入頁面
        # error_msg = "驗證失敗"
        # return RedirectResponse(url=f"/error?msg={error_msg}", status_code=status.HTTP_303_SEE_OTHER)
        return RedirectResponse(url="/error?msg=user_not_exist", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/signup",response_class=HTMLResponse)
async def signup(request: Request, name: Optional[str] = Form(None), username0: Optional[str] = Form(None), password0: Optional[str] = Form(None), agree: bool = Form(...)):
    if username0 and password0 and agree :
        # 建立 cursor 對象
        with mydb.cursor() as mycursor :
            query = "SELECT * FROM member where username = %s"
            inputs = (username0,)
            mycursor.execute(query, inputs)
            result = mycursor.fetchall()
        
            if result:
                return RedirectResponse(url="/error?msg=repeated_username", status_code=status.HTTP_303_SEE_OTHER)
        
            else:
                # 執行 SQL 插入語句
                query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
                inputs = (name, username0, password0)
                mycursor.execute(query, inputs)

                # 提交事務
                mydb.commit()
                # 登入成功，將使用者狀態設置為已登入
                request.session['SIGNED-IN'] = True 
                return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)

    if username0 is None or password0 is None:
        # error_msg = "缺少帳號或密碼"
        return RedirectResponse(url="/error?msg=no_username_or_password", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/error?msg=user_not_exist", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/createMessage", response_class=HTMLResponse)
async def createMessage(request: Request, say: Optional[str] = Form(None)):
    if not say:
        return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)

    with mydb.cursor() as mycursor :
        query = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
        inputs = (request.session['USERID'], say )
        mycursor.execute(query, inputs)

        # 提交事務
        mydb.commit()

    return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/deleteMessage/{message_id}", response_class=HTMLResponse)
async def deleteMessage(message_id: int):
    try:
        print(message_id)
        with mydb.cursor() as mycursor :
            query = "DELETE FROM message WHERE id =%s"
            inputs = (message_id,)
            mycursor.execute(query, inputs)

            # 提交事務
            mydb.commit()

        return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    # 檢查使用者是否已登入
    if not request.session.get('SIGNED-IN'):
        return RedirectResponse(url="/")
    else:
        name = request.session['NAME']
        return templates.TemplateResponse("member.html", {"request": request, "show_name":name})


@app.get("/loadmsg", response_class=JSONResponse)
async def loadmsg(request: Request, offset:Optional[int]=0):
    
    # 檢查使用者是否已登入
    if not request.session.get('SIGNED-IN'):
        return {"error":"session timeout"}
    else:
        name = request.session['NAME']

        with mydb.cursor(buffered=True,dictionary=True) as mycursor :

            # 每頁顯示10條留言
            page_size = 10

            query = """
            WITH board AS(
                SELECT member.name, message.content, message.time, message.id, parent_id, LPAD(ifnull(parent_id,message.id), 3, '0') AS level
                FROM message 
                JOIN member ON message.member_id = member.id 
            )
            SELECT * FROM board 
            ORDER BY level,id
            LIMIT %s OFFSET %s
            """
            mycursor.execute(query, (page_size, offset))
            result = mycursor.fetchall()
            return result

            # 返回字串
            # def json_serial(obj):
            #     """JSON serializer for objects not serializable by default json encoder."""
            #     if isinstance(obj, datetime):
            #         return obj.isoformat()
            #     raise TypeError(f"Type {type(obj)} not serializable")


@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, msg : Optional[str]=""):
    return templates.TemplateResponse("retry.html", {"request": request,"show_msg": msg }) 


@app.get("/signout",response_class=HTMLResponse)
async def signout(request:Request):
    # 登出時將使用者狀態設置為未登入
    # request.session['SIGNED-IN'] = False
    # 清空 session 以登出
    request.session.clear()
    return RedirectResponse(url="/")




