import requests
import json
import time

from pathlib import Path 
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

btc = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey="

r = requests.get(btc)

if r.status_code == 200:
   response = json.loads(r.text)


indexes = []
ohlcv = []

for k,v in response['Time Series (Digital Currency Daily)'].items():
    indexes.append(k)
    filtered = {'open': v.get('1a. open (USD)'), 'high': v.get('2a. high (USD)'), 'low': v.get('3a. low (USD)'), 
                'close': v.get('4a. close (USD)'), 'volume': v.get('5. volume')}
    ohlcv.append(filtered)
    
    
data = pd.DataFrame(data=ohlcv)
data['date'] = indexes


data.set_index('date', inplace=True)

data.to_csv()