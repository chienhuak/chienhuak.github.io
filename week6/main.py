from fastapi import FastAPI, Form, Request, Response, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
import os

# PS C:\Users\User\Documents\GitHub\chienhuak.github.io\week6> python -m uvicorn main:app --port 8001 --reload

app = FastAPI()
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

@app.get("/",response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/signin",response_class=HTMLResponse)
async def signin(request: Request, username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    if username == "test" and password == "test":
        # 登入成功，將使用者狀態設置為已登入
        request.session['SIGNED-IN'] = True
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
            mycursor.execute(f"SELECT * FROM member where username = '{username0}'")
            result = mycursor.fetchall()
        
            if result:
                return RedirectResponse(url="/error?msg=user_exist", status_code=status.HTTP_303_SEE_OTHER)
        
            else:
                # 執行 SQL 插入語句
                mycursor.execute(f"INSERT INTO member (name, username, password) VALUES ('{name}', '{username0}', '{password0}')")

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


# @app.post("/signin",response_class=HTMLResponse)
# #async def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
# #async def signin(username: str = Form(...), password: str = Form(...), agree: bool = Form(...)):
# async def signin(request: Request, username: Optional[str] = Form(None), password: Optional[str] = Form(None), agree: bool = Form(...)):
#     # 使用從表單中接收到的數據進行後續處理
#     # print("Received username:", username)
#     # print("Received password:", password)
#     if username == "test" and password == "test" and agree == True:
#         # 登入成功，將使用者狀態設置為已登入
#         request.session['SIGNED-IN'] = True
#         #登入成功，導向到會員頁面
#         #如果沒有提供 status_code 參數，則 FastAPI 將使用默認的狀態碼，但這可能不是你想要的。因此，你需要明確指定。 
#         return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)
#         # return templates.TemplateResponse("member.html",{"request":Request})
#     if username is None or password is None:
#         # error_msg = "缺少帳號或密碼"
#         return RedirectResponse(url="/error?msg=no_username_or_password", status_code=status.HTTP_303_SEE_OTHER)
#     else:
#         # 登入失敗，返回登入頁面
#         # error_msg = "驗證失敗"
#         # return RedirectResponse(url=f"/error?msg={error_msg}", status_code=status.HTTP_303_SEE_OTHER)
#         return RedirectResponse(url="/error?msg=user_not_exist", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/math",response_class=HTMLResponse)
async def math(request: Request, num: str):   #GET不會返回Form的值，會顯示在URL參數上面
    if num.isdigit():
         return RedirectResponse(url="/square/"+num)
    else:
        return RedirectResponse(url="/error?msg=not_positive_number", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/square/{num}", response_class=HTMLResponse)
async def square(request: Request, num: Optional[int]=None):
    return templates.TemplateResponse("square.html", {"request": request, "show_msg":num*num})


@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    # 檢查使用者是否已登入
    if not request.session.get('SIGNED-IN'):
        return RedirectResponse(url="/")
    return templates.TemplateResponse("member.html", {"request": request})


@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, msg : Optional[str]=""):
    return templates.TemplateResponse("retry.html", {"request": request,"show_msg": msg })


@app.get("/signout",response_class=HTMLResponse)
async def signout(request:Request):
    # 登出時將使用者狀態設置為未登入
    request.session['SIGNED-IN'] = False
    return RedirectResponse(url="/")




