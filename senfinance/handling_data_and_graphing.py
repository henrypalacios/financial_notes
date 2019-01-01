import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web
import pandas as pd


df = web.DataReader('TSLA', 'yahoo', '2018-01-01', '2018-01-05')

exit(df)


