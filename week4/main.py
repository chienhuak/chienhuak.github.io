from fastapi import FastAPI, Form, Request, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/",response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/signin",response_class=HTMLResponse)
#async def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
async def signin(username: str = Form(...), password: str = Form(...), agree: bool = Form(...)):
    # 使用從表單中接收到的數據進行後續處理
    print("xxxxxx")
    print("Received username:", username)
    print("Received password:", password)
    if username == "admin" and password == "password" and agree == True:
        #登入成功，導向到會員頁面
        return RedirectResponse(url="/member")
        # return templates.TemplateResponse("member.html",{"request":Request})
    else:
        # 登入失敗，返回登入頁面
        print("bbbbbb")
        return RedirectResponse(url="/error")
        # return templates.TemplateResponse("index.html", {"request": Request, "msg": "登入失敗，請檢查帳號、密碼和同意條款"})


@app.post("/member", response_class=HTMLResponse)
async def member(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})


@app.post("/error/{msgnote}", response_class=HTMLResponse)
async def member(request: Request):
    return templates.TemplateResponse("retry.html", {"request": request})




