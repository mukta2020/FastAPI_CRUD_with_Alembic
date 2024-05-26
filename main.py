# fastapi
from fastapi import FastAPI
from app.core.modules import init_routers, make_middleware
from app.router.commonRouter import router

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI CRUD operation",
        description="FastAPI basic that is needed for every fastapi project. ",
        version="1.0.0",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    #init_routers(app_=app_)
    #router(app_=app_)
    app_.include_router(router)
    return app_


app = create_app()
