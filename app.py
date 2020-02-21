import pandas as pd
import sys
import requests



data = pd.read_csv(r"C:\Users\Vsharma6\PycharmProjects\scrapingproject\volatilty.csv")
data.rename(columns={'Current Day Underlying Daily Volatility (E) = Sqrt(0.94*D*D + 0.06*C*C)':"DailyVolatility",
            'Underlying Annualised Volatility (F) = E*Sqrt(365)':"yearly volatility" },inplace = True)
k=data.drop(data[['Date','Underlying Previous Day Close Price (B)', 'Underlying Close Price (A)','Underlying Log Returns (C) = LN(A/B)','Previous Day Underlying Volatility (D)']], axis=1)
k.to_csv('newcsv.csv')
df=pd.read_csv('ind_niftylargemidcap250list.csv')
kp=df.drop(df[['Company Name', 'Industry','Series','ISIN Code']], axis=1)
kp.to_csv("stocksymbol.csv")
listp=[]
with open("stocksymbol.csv", "r") as f:
    r = pd.read_csv(f)
    ages= list(r["Symbol"])
with open("newcsv.csv", "r") as f:
    x = pd.read_csv(f)
for i, age in enumerate(x["Symbol"]):
    # You can't do this without a numpy int64
    if age in ages:
        j= x.loc[i]
        listp.append(j)
df = pd.DataFrame(listp, columns=['Symbol', 'DailyVolatility','yearly volatility'])
print(df)
df.to_csv('OUTPUT.CSV', sep=',', index=False)

read_csv= pd.read_csv('OUTPUT.CSV')
read_csv['daily_perc'] = read_csv['DailyVolatility']*100
read_csv['yearly_perc'] = read_csv['yearly volatility']*100
read_csv.to_csv("percentage.csv")
read_csv1= pd.read_csv('percentage.csv')
c=read_csv1[read_csv1.daily_perc >2]
c.to_csv("greater2.csv")
d=read_csv1[read_csv1.daily_perc>4]
d.to_csv("greater4.csv")
d=read_csv1[read_csv1.daily_perc>3]
d.to_csv("greater3.csv")



#for geeting data from source site 

import requests
import datetime
url = "url"
r = requests.get(url, allow_redirects=True)
open('volatilty.csv', 'wb').write(r.content)





























