from fastapi import APIRouter, Depends, HTTPException, status
from models import User, UserIn
from database import get_db
from sqlalchemy.orm import Session
import hashing

router = APIRouter(prefix='/auth', tags=['Auth'])

#test
@router.get('/users')
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post('/registrate')
def get_credentials(creds: UserIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == creds.username).first()
    if user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with that name already exists ')
    hashed_psw = hashing.hash_psw(creds.password)
    user_creds = User(username=creds.username, password=hashed_psw)
    db.add(user_creds)
    db.commit()
    db.refresh(user_creds)
    return {'Registered': creds.username}

@router.post('/login')
def verify_credentials(creds: UserIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == creds.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not exist')
    if not hashing.verify_psw(creds.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong password')
    return {'login': 'success'}