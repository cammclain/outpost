#! /bin/bash



uvicorn application.asgi:application --reload --host 127.0.0.1 --port 8000