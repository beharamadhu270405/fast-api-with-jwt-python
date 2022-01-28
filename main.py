

import uvicorn
from auth.auth import validate_token, generate_token
from models.model import LoginRequest
from fastapi import Depends, FastAPI, HTTPException


app = FastAPI(
    title='FastAPI JWT', openapi_url='/openapi.json', docs_url='/docs',
    description='fastapi jwt'
)


def verify_password(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False


@app.post('/login')
def login(request_data: LoginRequest):
    print(f'[x] request_data: {request_data.__dict__}')
    if verify_password(username=request_data.username, password=request_data.password):
        token = generate_token(request_data.username)
        return {'token': token}
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.get('/books', dependencies=[Depends(validate_token)])
def list_books():
    return {'data': ['Sherlock Homes', 'Harry Potter', 'Rich Dad Poor Dad']}
