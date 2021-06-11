
import numpy as np
import pandas as pd
import stock
def test1():
    assert callable(stock.mean2020)
    assert callable(stock.March2020Increase)
    assert callable(stock.March2020Closing)
test1()
def test2():
    assert stock.mean2020('zm')['Open'].iloc[0] == 98.8189680311415
    assert len(stock.March2020Increase('zm')) == 14
    assert stock.March2020Closing('zm') != None
test2()
def test3():
    assert stock.mean2020('nflx')['Open'].iloc[0] == 352.9669824024988
    assert len(stock.March2020Increase('nflx')) == 12
    assert stock.March2020Closing('nflx') != None
test3()
