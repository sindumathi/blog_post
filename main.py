from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app=FastAPI()
templates= Jinja2Templates(directory="templates")
posts: list[dict] = [
    {
        "id": 1,
        "author": "Jane Doe",
        "title": "Getting Started with Python",
        "content": "Python is a versatile and beginner-friendly programming language...",
        "date_posted": "2026-09-15"
    },
    {
        "id": 2,
        "author": "John Smith",
        "title": "Understanding Data Structures",
        "content": "Dictionaries and lists are fundamental building blocks in data management...",
        "date_posted": "2026-09-28"
    }
]
@app.get("/",  include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request:Request):
    return templates.TemplateResponse(request, "home.html",{"posts":posts} )

@app.get("/api/posts")
def get_posts():
    return posts