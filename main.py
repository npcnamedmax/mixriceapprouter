from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class InferenceRequest(BaseModel):
    imgUrl: str
    model: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/inference")
async def infer(req: InferenceRequest):
    print(req)
    if(req.model == 'YOLOv11_CS' or req.model == 'YOLOv12_CS'):
        res = httpx.post('http://127.0.0.1:8001', json=req.model_dump(), timeout=None)
        
    elif(req.model == 'YOLOv11_CA' or req.model == 'YOLOv12_CA'):
        res = httpx.post('http://127.0.0.1:8002', json=req.model_dump(), timeout=None)
    elif(req.model == 'RT-DETR_CS'):
        res = httpx.post('http://127.0.0.1:8003', json=req.model_dump(), timeout=None)
    elif(req.model == 'RT-DETR_CA'):
        res = httpx.post('http://127.0.0.1:8004', json=req.model_dump(), timeout=None)
    
    print(res.json())
    return res.json()
    
    