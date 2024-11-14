from __future__ import annotations

 
from litestar import Litestar, Router

def listener_startup(app: Litestar) -> None:
    pass

def listener_services(apps: list[Litestar]) -> None:
    for app in apps:
        
        app.on_startup.append(listener_startup)

        # add the router to the app
        app.routes.append(router)



