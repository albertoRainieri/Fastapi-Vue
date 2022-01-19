from fastapi import APIRouter
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from routes import UserRoute, LoginRoute

router_api = APIRouter()
router_api.include_router(LoginRoute.router, prefix="/auth", tags=["Authorization"])
router_api.include_router(UserRoute.router, prefix="/users", tags=["Users"])

