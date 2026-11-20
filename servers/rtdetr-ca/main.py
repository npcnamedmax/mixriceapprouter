import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ultralytics import RTDETR

app = FastAPI()

model = RTDETR('./rtdetrsingle.pt')


class InferenceRequest(BaseModel):
    imgUrl: str
    model: str


@app.post("/")
async def root(req: InferenceRequest):
    print(req)
    if(req.model == 'RT-DETR_CA'):
        conf = 0.734
        

    res = model.predict(source=req.imgUrl, verbose=True, plots=True, conf=conf) 
    return res[0].to_json()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8004)
    