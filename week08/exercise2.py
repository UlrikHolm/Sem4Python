import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import csv

#2
url = 'FOLk1A.csv'
df = pd.read_csv(url,sep=';')
df['TID'] = df['TID'].map(lambda x:x[:-2]) #cut the last 2 characters
df.to_csv('demografic_cleaned.csv',header=False, index=False)

demo_filename = 'demografic_cleaned.csv'
city_filename = 'BY_KODER_demografics.csv'
#3
demografic = np.loadtxt(demo_filename, delimiter=',', dtype=np.uint)

#4
def get_citycodes():
    citycodes = dict()

    with open(city_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader,None)
        for row in reader:
            citycodes[row[0]] = row[1]
    return citycodes

# print(get_citycodes())

#5
def male_pct_by_city(city_code):
    mask = (demografic[:,0] == city_code) & (demografic[:,3] == 2020)
    total_pop = np.sum(demografic[mask][:,4])
    mask_males = mask & (demografic[:,1] == 1)
    males = np.sum(demografic[mask_males][:,4])
    pct_males = round((males/total_pop)*100,5)

    return pct_males

def higest_pct_males():
    males_pct_city = dict() 
    for i in get_citycodes().keys():
        if (np.isnan(male_pct_by_city(int(i)))):
            continue
        else:
            males_pct_city[get_citycodes().get(i)] = male_pct_by_city(int(i))
    #print(males_pct_city)
    return 'Region with highest percentage of men:'+ max(males_pct_city, key=males_pct_city.get)

print(higest_pct_males())


#6
def summed_by_city(cities):
    for c in cities:
        temp_c = dict()
        for i in range(2008, 2021, 1):
            mask = (demografic[:,0] == c) & (demografic[:,3] == i)
            total_pop = np.sum(demografic[mask][:,4])
            temp_c[i] = total_pop
        print(temp_c)
        plt.plot(list(temp_c.keys()), list(temp_c.values()), label=c)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(list(temp_c.keys()),rotation=90)
    plt.legend()
    plt.show()


cities_codes = [751, 147, 851, 461, 400] #Ikke top5 byer, da der kun er 4 byer & 7 regioner så har valgt Aarhus, Frederiksberg, Aalborg, Odense & Bornholm

summed_by_city(cities_codes)


