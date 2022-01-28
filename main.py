
import uvicorn
from fastapi import FastAPI, HTTPException
from model import LoginRequest

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
        return 'Success'
    else:
        raise HTTPException(status_code=404, detail="User not found")
