

# pulls everything together for the the full outpost core application

from __future__ import annotations
from pathlib import Path
from litestar import Litestar
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
from litestar.static_files import StaticFilesConfig
from .middleware.auth import AuthenticationMiddleware

from litestar.middleware.session.server_side import ServerSideSessionBackend, ServerSideSessionConfig
from config.config import settings
from redis.asyncio import Redis

ASSETS_DIR = Path("static")


def create_app() -> Litestar:

    # create the redis client
    redis_host = settings.REDIS_HOST
    redis_port = settings.REDIS_PORT
    redis: Redis = Redis(host=redis_host, port=redis_port)

    # create the session backend
    session_backend = ServerSideSessionBackend(config=ServerSideSessionConfig(secret_key=settings.SESSION_SECRET_KEY, max_age=3600))

    ## the main application object
    app = Litestar(
        # add the routes
        route_handlers=[
        ],

        # add the authentication middleware
        middleware=[
            AuthenticationMiddleware,
            session_backend
        ],

        # add the static files config
        static_files_config=[
            StaticFilesConfig(path="/static", directories=[ASSETS_DIR], html_mode=True)
        ],

        # add the template config
        template_config=TemplateConfig(
            engine=JinjaTemplateEngine(),
            directory=Path("templates"),
        ),

    )
    return app

app = create_app()