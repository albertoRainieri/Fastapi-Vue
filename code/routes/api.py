from fastapi import APIRouter
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from routes import routes, login

router_api = APIRouter()
router_api.include_router(login.router, prefix="/auth", tags=["Authorization"])
router_api.include_router(routes.router, prefix="/users", tags=["Users"])

