from fastapi import FastAPI , Depends
from database import Base, engine , get_db
from models import User
from pydantic import BaseModel
app = FastAPI()


class fatch(BaseModel):
    name: str
class UserCreate(BaseModel):
    name:str
    phone: int
@app.get('/')
async def test():
    return "Working "


@app.post("/add_user")
async def create_user(user: UserCreate, db = Depends(get_db)):
    db_user = User(
        name=user.name,
        phone=user.phone,
    )
    print(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@app.post("/get_user")
async def getuser(username: fatch , db= Depends(get_db)):
    db_user = db.query(User).filter_by(name=username.name).first()

    return db_user

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
