import pandas as pd
import datetime
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2022, 12, 1)
end_date = datetime.date.today()

df = pd.DataFrame()
for single_date in daterange(start_date, end_date):
    dfs = pd.read_html(f'https://www.xe.com/currencytables/?from=USD&date={single_date.strftime("%Y-%m-%d")}')[0]
    dfs['Date'] = single_date.strftime("%Y-%m-%d")
    df = pd.concat((df,dfs), axis=0)
    
df.columns = ['Currency code', 'Currency name', 'Units per USD', 'USD per Unit', 'Date']
h = df.head()
h

 # Choose Euro as sample currency

df[df['Currency code'] == 'EUR'].plot(x='Date',y='USD per Unit',kind = 'line')

