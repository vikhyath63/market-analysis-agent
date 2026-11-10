POSITIVE={"beat","growth","strong","upgrade","profit","surge","bullish","record","positive"}
NEGATIVE={"miss","decline","weak","downgrade","loss","drop","bearish","risk","negative"}
def sma(values:list[float],window:int):
    if len(values)<window: return None
    return sum(values[-window:])/window
def rsi(values:list[float],window:int=14):
    if len(values)<=window: return None
    changes=[values[i]-values[i-1] for i in range(1,len(values))]
    gains=[max(x,0) for x in changes[-window:]]; losses=[max(-x,0) for x in changes[-window:]]
    avg_gain=sum(gains)/window; avg_loss=sum(losses)/window
    if avg_loss==0: return 100.0
    rs=avg_gain/avg_loss
    return 100-(100/(1+rs))
def sentiment(headlines:list[str]):
    score=0; hits=[]
    for line in headlines:
        words={w.strip(".,:;!?()[]").lower() for w in line.split()}
        pos=words & POSITIVE; neg=words & NEGATIVE; score+=len(pos)-len(neg)
        if pos or neg: hits.append({"headline":line,"positive_terms":sorted(pos),"negative_terms":sorted(neg)})
    label="positive" if score>0 else "negative" if score<0 else "neutral"
    return {"score":score,"label":label,"matched_headlines":hits,"method":"simple keyword baseline; not a financial sentiment model"}
def analyze(candles:list[dict],headlines:list[str]):
    closes=[float(x["close"]) for x in candles]
    if len(closes)<2: raise ValueError("At least two candles with close values are required")
    latest=closes[-1]; ma20=sma(closes,20); ma50=sma(closes,50)
    return {"latest_close":latest,"sma_20":ma20,"sma_50":ma50,"rsi_14":rsi(closes),"sentiment":sentiment(headlines),"signals":{"above_sma20":latest>ma20 if ma20 is not None else None,"above_sma50":latest>ma50 if ma50 is not None else None},"disclaimer":"Educational analytics only; not investment advice or a trade recommendation."}
