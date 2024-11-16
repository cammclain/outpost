from __future__ import annotations

from litestar import Litestar



import logging

from ..listener_services import HTTPListener
from ...dashboard.database.models.teamserver import TeamserverAgent

# Create a class of HTTP Listenters that serve up objects to the beacons 
class HTTPAgentServer(HTTPListener, TeamserverAgent):
    def __init__(self, app: Litestar, agent: TeamserverAgent) -> None:
        super().__init__(app)
        self.agent = agent

    async def _http_listener_startup(self) -> None:
        logging.info("HTTP Agent Server Startup")
        pass

    async def _http_listener_shutdown(self) -> None:
        logging.info("HTTP Agent Server Shutdown")
        pass


    async def listener_lifecycle(self) -> None:
        await self._http_listener_startup()
        await self._http_listener_shutdown()
