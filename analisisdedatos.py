import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib

DATABASE_PATH = "club.csv"


def calcula_prob(a,b):
    a=a[1]
    b=b[1]
    a_gana=float(a/(a+b+2))
    b_gana=float(b/(a+b+2))
    empate= 1-(a_gana)-(b_gana)
    
df = pd.read_csv(DATABASE_PATH)
price=df['Market Value Of Club In Millions(£)'].tolist()
clubes=df['Club Name'].tolist()
players=df['Average Age Of Players'].tolist()
div=[]

for i in range(len(price)):
    x=price[i]/players[i]
    div.append(x)
print(div)

lista_cb=[]

for i in range(len(price)):
    lista_cb.append([clubes[i],div[i]])
print(lista_cb)

print(lista_cb[0][1])