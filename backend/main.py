import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/", response_model=str, status_code=200)
async def asset_inputs(request: Request, ) -> JSONResponse:
    response = {"message": "Hello World"}
    return JSONResponse(content=jsonable_encoder(response))


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True, log_level="debug")
