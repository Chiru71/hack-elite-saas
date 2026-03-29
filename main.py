import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="HACK-eLITE AI SaaS",
    description="The Next Evolution of Elite AI Intelligence",
    version="1.0.0"
)

# Serves static files from the 'hack-elite-site' directory
STATIC_DIR = os.path.join(os.getcwd(), "hack-elite-site")

if os.path.exists(STATIC_DIR):
    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
else:
    @app.get("/")
    async def root():
        return {"message": "Welcome to HACK-eLITE AI SaaS. Static site directory not found.", "status": "initializing"}

# Standard entrypoint for deployment tools
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
