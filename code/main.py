import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi import Depends, status, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from routes import routes, login, api


def get_application():
    app = FastAPI()

    # CORSを回避するために設定
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(api.router_api)
    return app

app = get_application()
