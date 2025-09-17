from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from login_users import (
    LoginRequest,
    SignupRequest,
    get_user_by_email,
    create_user,
    hash_password,
    verify_password,
    create_access_token
)

app = FastAPI(title="ToDo-List")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def welcome_message():
    return "Welcome to the ToDo List application!!!"

@app.post("/login",
          status_code=status.HTTP_202_ACCEPTED,
          tags=["Login"])
async def login_user(request: LoginRequest):
    user = await get_user_by_email(request.user_email)

    if user and verify_password(request.password, user["password"]):
        token = create_access_token(data={"sub": user["user_email"]})
        return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(status_code=401, detail="Incorrect email or password")

@app.post("/signup",
          status_code=status.HTTP_201_CREATED,
          tags=["Signup"])
async def signup_user(request: SignupRequest):
    existing_user = await get_user_by_email(request.user_email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # ✅ Correct: Hash the password BEFORE saving
    hashed = hash_password(request.password)

    new_user = {
        "user_email": request.user_email,
        "password": hashed  # store hashed password
    }

    await create_user(new_user)

    return {"message": "Signup successful"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8989, reload=True)
