from __future__ import annotations
from typing import TypedDict    
# this file contains the routes for the auth service
from dataclasses import dataclass
from litestar import Controller, get, post
from litestar.response import Template
from ..database.models.teamserver import TeamserverUser

from litestar.status_codes import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED

@dataclass
class LoginData:
    username: str
    password: str

@dataclass
class LoginResponse:
    status_code: int
    message: str

class AuthController(Controller):
    path = "/auth"

    @get("/login")
    async def login_page(self) -> Template:
        return Template(template_name="views/auth/login.html")
    
    @post("/login")
    async def login(self, data: LoginData) -> LoginResponse:
        # TODO: Implement login logic
        # ch
        print(data)

        return LoginResponse(
            status_code=HTTP_401_UNAUTHORIZED,
            message="Invalid credentials"

        )


