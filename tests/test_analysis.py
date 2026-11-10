import pytest
from app.analysis import sma,rsi,sentiment,analyze
def test_sma(): assert sma([1,2,3,4],3)==3
def test_rsi_rises_to_100(): assert rsi(list(range(1,17)))==100
def test_sentiment_is_explainable(): assert sentiment(["Strong growth and profit"])["label"]=="positive"
def test_requires_multiple_closes():
    with pytest.raises(ValueError): analyze([{"close":10}],[])
