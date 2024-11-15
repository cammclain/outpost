from __future__ import annotations
from litestar import Litestar
from application import app
import asyncio
import uvicorn
from config.config import settings
import logging
import threading
    



def main() -> None:
    # load the environment variables
   
    # run the client application. This is the main dashboard application that clients will connect to, in order to interact with the outpost team server.
    client_application: Litestar = app.app
    threading.Thread(target=uvicorn.run, args=(client_application, host="127.0.0.1", port=8000)).start()

    # TODO: Launch Listeners
    # TODO: Read from the database for any active campaigns and launch the associated listeners


if __name__ == "__main__":
    asyncio.run(main())
