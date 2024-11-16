from __future__ import annotations

from litestar import Litestar


from ...dashboard.database.models.teamserver import TeamserverBeaconObject

import logging

from .routes import ObjectServerController

#  Create a class of HTTP Listenters that serve up objects to the beacons 
class HTTPObjectServer(TeamserverBeaconObject):
    def __init__(self, beacon_object: TeamserverBeaconObject) -> None:
        self.listener_app = Litestar(
            route_handlers=[ObjectServerController]
        )
        self.beacon_object = beacon_object

    async def _http_listener_startup(self) -> None:
        logging.info("HTTP Object Server Startup")
        
        # TODO: Add the object to the HTTP Server
        # TODO: query the seaweedfs cluster for the object data
        logging.info(f"Adding object to HTTP Server: {self.beacon_object.name}")
        logging.info(f"Object Data: {self.beacon_object.object_data}")
        logging.info(f"Object URL Location: {self.beacon_object.seaweedfs_url_location}")
        # TODO: Add the object to the HTTP Server



        pass


    async def _http_listener_shutdown(self) -> None:
        logging.info("HTTP Object Server Shutdown")
        # TODO: Remove the object from the HTTP Server
        pass



    async def listener_lifecycle(self) -> None:
        await self._http_listener_startup()
        await self._http_listener_shutdown()


