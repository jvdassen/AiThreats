import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from backend.threats_finder import find_threats

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    threats_result = find_threats(content)
    return JSONResponse(content=jsonable_encoder(threats_result))

if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8080, reload=True, log_level="debug")
