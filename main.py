from fastapi import FastAPI
from routes.user import user_router  # Import the user router

# Initialize FastAPI app
app = FastAPI()

# Include the user router
app.include_router(user_router, prefix="/api")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the PlayIn API"}
