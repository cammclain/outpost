from __future__ import annotations
import logging

 
from litestar import Litestar, Router

class HTTPListener:
    def __init__(self, app: Litestar) -> None:
        self.app = app

    async def _http_listener_startup(self) -> None:
        logging.info("HTTP Listener Startup")
        pass


    async def _http_listener_shutdown(self) -> None:
        logging.info("HTTP Listener Shutdown")
        # TODO: Make sure agents are shutdown, or have been alerted to the change in state
        ## The agents still online will need to be shutdown gracefully
        ## The agents that are offline will need to be alerted to the change in state before the listener is shutdown
        pass

#  Create a class of HTTP Listenters that serve up objects to the beacons 
class HTTPObjectServer(HTTPListener, beacon_object: BeaconObject):
    def __init__(self, app: Litestar, beacon_object: BeaconObject) -> None:
        super().__init__(app)
        self.beacon_object = beacon_object


        

