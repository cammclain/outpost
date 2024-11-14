from __future__ import annotations

# this file contains the routes for the auth service

from litestar import Controller, get, post
from litestar.template.base import Template
from ..database.models.teamserver import TeamserverUser

from litestar.status_codes import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED


class AuthController(Controller):
    path = "/auth"

    @get("/login")
    async def login_page(self) -> Template:
        return Template(name="login.html")

    @post("/login")
    async def login(self, data: LoginData) -> LoginResponse:
        pass
