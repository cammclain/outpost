from __future__ import annotations


from litestar.middleware.session import SessionMiddleware
from litestar.middleware.session.server_side import ServerSideSessionBackend, ServerSideSessionConfig
from ...config.config import settings

session_middleware = ServerSideSessionBackend(config=ServerSideSessionConfig(key=settings.SESSION_SECRET_KEY, max_age=3600))
