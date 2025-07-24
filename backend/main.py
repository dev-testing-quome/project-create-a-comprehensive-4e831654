import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from sqlalchemy.orm import Session

from backend.database import SessionLocal, engine
from backend.routers import users, cases #Import your routers here
from backend.models import Base # Import your database models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Legal Case Management System", description="A comprehensive legal case management system.", version="1.0.0")

# CORS configuration
origins = ["*"] # Replace with your allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Dependency injection for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routers
app.include_router(users.router)
app.include_router(cases.router)

# Health check
@app.get('/health')
def health_check():
    return {"status": "ok"}

#Error Handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.detail})

#Static files serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{file_path:path}")
    async def serve_frontend(file_path: str):
        if file_path.startswith("api"):
            return None
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")

#Main
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
