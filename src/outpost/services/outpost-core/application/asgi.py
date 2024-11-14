from __future__ import annotations
from litestar import Litestar
from application import app


application: Litestar = app.app

