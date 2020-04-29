import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

#ex 1A
def dk_divorce():
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=000&CIVILSTAND=F%2CTOT&Tid=*'
    response = requests.get(url)

    if response.ok:  # status_code == 200:
        with open('dk-divorce.csv', 'wb') as f:
            f.write(response.content)   

    df = pd.read_csv('dk-divorce.csv', delimiter=";")

    skilt = df.loc[df['CIVILSTAND'] == 'Fraskilt']
    total = df.loc[df['CIVILSTAND'] == 'I alt']



    sklit_val = skilt['INDHOLD'].to_numpy()
    total_val = total['INDHOLD'].to_numpy()

    #print(sklit_val)

    pct = [((sklit_val[i]/total_val[i])*100) for i in range(len(total_val))]


    plt.plot(total['TID'], pct)
    plt.xlabel('Kvartal')
    plt.ylabel('Skilt pct.')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()
#ex 1B
def top5_divorce():
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101%2C851%2C530%2C740%2C657&CIVILSTAND=U%2CTOT'
    response = requests.get(url)

    if response.ok:  # status_code == 200:
        with open('top5-divorce.csv', 'wb') as f:
            f.write(response.content)   

    df = pd.read_csv('top5-divorce.csv', delimiter=";")    

    ugift = df.loc[df['CIVILSTAND'] == 'Ugift']
    total = df.loc[df['CIVILSTAND'] == 'I alt']

    ugift_val = ugift['INDHOLD'].to_numpy()
    total_val = total['INDHOLD'].to_numpy()

    #print(total['OMRÅDE'].reset_index().get('OMRÅDE')[0])

    divorce_pct = dict()

    for i in range(len(total)):
        pct = (ugift_val[i] / total_val[i])*100
        divorce_pct[total['OMRÅDE'].reset_index().get('OMRÅDE')[i]] = pct
    
    #print(divorce_pct)

    plt.bar(list(divorce_pct.keys()), list(divorce_pct.values()))
    plt.xlabel('BY')
    plt.ylabel('Skilt pct.')
    plt.xticks(rotation=90)
    plt.show()
#ex 1C
def marrital():
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=U%2CG%2CE%2CF&Tid=2008K1%2C2009K1%2C2010K1%2C2011K1%2C2012K1%2C2013K1%2C2014K1%2C2015K1%2C2016K1%2C2017K1%2C2018K1%2C2019K1%2C2020K1'
    response = requests.get(url)

    if response.ok:  # status_code == 200:
        with open('marrital.csv', 'wb') as f:
            f.write(response.content)   

    df = pd.read_csv('marrital.csv', delimiter=";")    

    ugift = df.loc[df['CIVILSTAND'] == 'Ugift']
    gift_sep = df.loc[df['CIVILSTAND'] == 'Gift/separeret']
    enke = df.loc[df['CIVILSTAND'] == 'Enke/enkemand']
    skilt = df.loc[df['CIVILSTAND'] == 'Fraskilt']

    #print(ugift['TID'])

    plt.bar(ugift['TID'],ugift['INDHOLD'], label='ugfit')
    plt.bar(gift_sep['TID'],gift_sep['INDHOLD'], label='gift_sep')
    plt.bar(skilt['TID'],skilt['INDHOLD'], label='skilt')
    plt.bar(enke['TID'],enke['INDHOLD'], label='enke')
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()

#ex 1D
def married_status():
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=U%2CG&ALDER=*&Tid=2020K1'
    response = requests.get(url)

    if response.ok:  # status_code == 200:
        with open('dk-married.csv', 'wb') as f:
            f.write(response.content)   

    df = pd.read_csv('dk-married.csv', delimiter=";")    

    ugift = df.loc[df['CIVILSTAND'] == 'Ugift']
    gift = df.loc[df['CIVILSTAND'] == 'Gift/separeret']

    # print(ugift[19:100]['ALDER'][19][:-3])

    plt.bar(ugift[19:100]['ALDER'],ugift[19:100]['INDHOLD'], label='ugfit', alpha=0.5)
    plt.bar(gift[19:100]['ALDER'],gift[19:100]['INDHOLD'], label='gift', alpha=0.5)
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()

married_status()
