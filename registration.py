from fastapi import APIRouter, HTTPException, Depends
from authx import AuthX, AuthXConfig
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ---------- Database Setup ----------
DATABASE_URL = "sqlite:///./users.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- AuthX Config ----------
config = AuthXConfig(
    JWT_SECRET_KEY='your_secret_key_here',
    JWT_TOKEN_LOCATION=["cookies"],
    JWT_ACCESS_COOKIE_NAME='authx_access',
)
security = AuthX(config=config)

# ---------- Router ----------
router = APIRouter()

class UserLoginSchema(BaseModel):
    username: str
    password: str

class UserRegisterSchema(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register(data: UserRegisterSchema, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == data.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists.")
    
    new_user = User(username=data.username, password=data.password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully."}

@router.post("/login")
async def login(crsd: UserLoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == crsd.username, User.password == crsd.password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials.")

    token = security.create_access_token(data={"sub": crsd.username})
    response = {"message": f"{crsd.username} login successful", "token": token}
    return response


@router.get("/protected")
async def protected_route(user=Depends(security.get_current_subject)):
    return {"message": f"Welcome {user['sub']}! This is a protected route."}
