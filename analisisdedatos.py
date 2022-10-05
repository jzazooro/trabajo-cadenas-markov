import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib

DATABASE_PATH = "club.csv"

class DataBase:
     
    df = pd.read_csv(DATABASE_PATH)
    print(df)
    price=[]
    price=df['Market Value Of Club In Millions(£)'].tolist()
    print(price)
    players=df['Average Age Of Players'].tolist()
    print(players)

