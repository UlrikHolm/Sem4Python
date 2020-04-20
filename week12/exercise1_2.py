import pandas as pd
from sqlalchemy import create_engine
import pymysql
import re

con_str = 'mysql+pymysql://dev:ax2@localhost:3307/week12python'

#Download data fra linket og gem det i en dataframe 
#og gem det i en mysql database
def first():
    url = 'http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv'
    df = pd.read_csv(url)
    engine = create_engine(con_str)
    df.to_sql('pythondemo',con=engine, if_exists='append', index = False)
    df
#first()

#Lav en funktion der returnerer en dict med minimum følgende data:
#- Find antallet af crimes mellem to givne datoer i 2006 (givet som parameter til funktionen)
#- Find den totale mængde af "burglary" i januar

def second(day1=None, day2=None):
    engine = create_engine(con_str)

    df = pd.read_sql('SELECT cdatetime,crimedescr FROM pythondemo', con=engine, parse_dates=['cdatetime'], columns=['cdatetime', 'crimedescr'])
    
    if (day1 and day2):
        start_date = '2006-01-' + day1
        end_date = '2006-01-' + day2
        date_crimes = df.loc[(df['cdatetime'] >= start_date) & (df['cdatetime'] <= end_date)]
        return {'date_crimes': len(date_crimes)}

    amount_of_burglaries = df[df['crimedescr'].str.contains('BURGLARY')]
    return {'burglaries in January': len(amount_of_burglaries)}
        
print(second('01','02'))
print(second())