# Mixed Rice Inference API
Inference backend of the Automated Mixed Rice Detection and Pricing System, implemented using FastAPI. A router receives request, and forwards it to the appropriate model server that hosts the requested model.

## Request and Result format:
### Exanple Request:
```json
{ "imgUrl": "https://.../xxx.png", "model": "RT-DETR_CA" }
```

### Example Response:
```json
[
  {
    "name": "rice",
    "class": 11,
    "confidence": 0.94,
    "box": { "x1": 120.0, "y1": 80.0, "x2": 340.0, "y2": 260.0 },
    "mass": [152.3]
  },
  ...
]
```
Note that `mass` is an array, with one mass value for **channel-agnostic model** and one mass value **per-class** for **channel-specific models**.

## How to run
**Router:**
```bash
cd router
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --port 8000
```

**Model servers:**
```bash
cd servers/rtdetr-ca
python -m venv .venv && source .venv/bin/activate
pip install "ultralytics @ git+https://github.com/npcnamedmax/mixed-rice-detection-models@rtdetrsinglechannel"
pip install fastapi uvicorn
python main.py        
```
Repeat the above with other models, replacing "rtdetrsinglechannel" with other branches for different models. Then put the model weights in the same directory as main.py.

## Limitations
- This is supposed to be a minimal working example that is meant to be paired with the main web app running only locally, as it does not have any authentication or rate limiting, and does not do request validation, and images are saved locally.
- The addresses and ports are hardcoded.
- Difficult to set up, as you need a different virtual environment for each server since each model variant has its own branch. A better design would be to make the head type configurable in one library (one branch), so a single server can load every model.

## License
AGPL-3.0. See [mixed-rice-detection-models](https://github.com/npcnamedmax/mixed-rice-detection-models).