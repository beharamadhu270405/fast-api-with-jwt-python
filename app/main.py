
import uvicorn
from app.models.model import LoginRequest
from app.utils.utils import verify_password, get_usa_population_yearwise
from fastapi import Depends, FastAPI, HTTPException
from app.auth.auth import validate_token, generate_token


app = FastAPI(
    title='FastAPI JWT', openapi_url='/openapi.json', docs_url='/docs',
    description='fastapi jwt')


@app.post('/login')
def login(request_data: LoginRequest):
    print(f'[x] request_data: {request_data.__dict__}')
    if verify_password(username=request_data.username, password=request_data.password):
        token = generate_token(request_data.username)
        return {'token': token}
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.get('/get_usa_data', dependencies=[Depends(validate_token)])
def get_usa_data():
    return get_usa_population_yearwise()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
