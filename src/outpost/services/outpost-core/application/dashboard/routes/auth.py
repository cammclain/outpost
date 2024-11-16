from __future__ import annotations
from typing import TypedDict    
# this file contains the routes for the auth service
from dataclasses import dataclass
from litestar import Controller, get, post
from litestar.response import Template
from ..database.models.teamserver import TeamserverUser
from litestar.response import Redirect

from litestar.status_codes import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED


# TODO: This is a temporary login route. It needs to be replaced with a proper authentication system.



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
    async def login(self, data: dict) -> Redirect:
        username = data.get("username")
        password = data.get("password")

        # Authenticate user (adjust based on your ORM)
        user = await TeamserverUser.authenticate(username, password)  # Example method
        if user:
            # Save user_id to session
            self.request.session["user_id"] = user.id
            return Redirect(path="/dashboard")

        # Redirect back to login page on failure
        return Redirect(path="/auth/login?error=Invalid credentials")
    
