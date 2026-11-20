import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ultralytics import YOLO

app = FastAPI()

model11 = YOLO('./11.pt')
model12 = YOLO('./12.pt')

class InferenceRequest(BaseModel):
    imgUrl: str
    model: str


@app.post("/")
async def root(req: InferenceRequest):
    print(req)
    conf = 0.6 #def
    if(req.model == 'YOLOv11_CS'):
        model = model11
        conf = 0.769
        
    elif(req.model == 'YOLOv12_CS'):
        model = model12
        conf = 0.722
        

    res = model.predict(source=req.imgUrl, verbose=True, plots=True, conf=conf) 
    return res[0].to_json()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
    