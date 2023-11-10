import uvicorn

from config.settings import config


if __name__ == "__main__":
    uvicorn.run(
        app="config.server:app",
        reload=True if config.ENVIRONMENT != "production" else False,
        workers=1,
    )
