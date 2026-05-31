from typing import Annotated
from fastapi import Cookie, status, APIRouter
from datetime import datetime, UTC
from pydantic import BaseModel
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db = [
    {"title": f"Criando uma aplicação django", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app FastApi", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app Flask", "date": datetime.now(UTC), "published": True},
    {"title": f"Internacionalizando uma app Starlett", "date": datetime.now(UTC), "published": False}
]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post: PostIn):
    fake_db.append(post.model_dump())
    return post

@router.get("/", response_model=list[PostOut])
def read_posts(published: bool, limit: int, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None):
    tail = skip + limit
    return [post for post in fake_db[skip:tail] if post["published"]is published]

    # print(f"Cookie: ")
    # posts = []
    # for post in fake_db:
    #     if len(posts) == limit:
    #         break
    #     if post["published"] is published:
    #         posts.append(post)
    # return posts

@router.get("/{framework}")
def read_framework_posts(framework: str, response_model=PostOut):
    return {
        "posts": [
            {"title": f"Criando uma aplicação {framework}", "date": datetime.now(UTC)},
            {
                "title": f"Internacionalizando uma app {framework}",
                "date": datetime.now(UTC),
            },
        ]
    }
