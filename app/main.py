from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from app.analysis import analyze
app=FastAPI(title="Market Analysis Agent",version="0.1.0")
class Candle(BaseModel): close:float
class Request(BaseModel): candles:list[Candle]=Field(min_length=2); headlines:list[str]=[]
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/analyze")
def analysis(req:Request):
    try: return analyze([x.model_dump() for x in req.candles],req.headlines)
    except ValueError as e: raise HTTPException(400,str(e)) from e
