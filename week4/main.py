from fastapi import FastAPI, Form, Request, Response, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# 設定 SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="some-random-string")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/",response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/signin",response_class=HTMLResponse)
#async def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#async def signin(username: str = Form(...), password: str = Form(...), agree: bool = Form(...)):
async def signin(request: Request, username: Optional[str] = Form(None), password: Optional[str] = Form(None), agree: bool = Form(...)):
    # 使用從表單中接收到的數據進行後續處理
    # print("Received username:", username)
    # print("Received password:", password)
    if username == "test" and password == "test" and agree == True:
        # 登入成功，將使用者狀態設置為已登入
        request.session['is_logged_in'] = True
        #登入成功，導向到會員頁面
        return RedirectResponse(url="/member")
        # return templates.TemplateResponse("member.html",{"request":Request})
    if username is None or password is None:
        error_msg = "缺少帳號或密碼"
        return RedirectResponse(url=f"/error?msg={error_msg}")
    else:
        # 登入失敗，返回登入頁面
        error_msg = "驗證失敗"
        return RedirectResponse(url=f"/error?msg={error_msg}")

@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    # 檢查使用者是否已登入
    if not request.session.get('is_logged_in'):
        return RedirectResponse(url="/")
    return templates.TemplateResponse("member.html", {"request": request})

@app.post("/member", response_class=HTMLResponse)
async def member(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})


@app.post("/error", response_class=HTMLResponse)
async def member(request: Request):
    return templates.TemplateResponse("retry.html", {"request": request})


@app.post("/error", response_class=HTMLResponse)
async def error(request: Request, msg: str = None):
    return templates.TemplateResponse("retry.html", {"request": request, "msg": msg})


@app.get("/signout",response_class=HTMLResponse)
async def signout(request:Request):
    # 登出時將使用者狀態設置為未登入
    request.session['is_logged_in'] = False
    return RedirectResponse(url="/")




