import numpy as np
import matplotlib.pyplot as plt

filename = './befkbhalderstatkode.csv'
#2
statkode = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
#3
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

pop_per_neighb = {}

for n in neighb.keys():
    mask = (statkode[:,1] == n) & (statkode[:,0] == 2015)
    pop_per_neighb[neighb.get(n)] = np.sum(statkode[mask][:,4])

pop_sorted = {k: v for k, v in sorted(pop_per_neighb.items(), key=lambda item: item[1])}
#4
plt.bar(pop_sorted.keys(), pop_sorted.values(), width=0.8, align='center')
plt.ylabel('NeighB Sum')
plt.xticks(rotation=90)
plt.xlabel('NeighB')
plt.title('Population per neighborhood')
plt.show()
#5
mask65 = (statkode[:,2] > 65) & (statkode[:,0] == 2015)
ppl_over_65 = np.sum(statkode[mask65][:,4])

print(ppl_over_65)
#6
mask65_not_dk = mask65 & (statkode[:,3] != 5100)
ppl_o_65_nok_dk = np.sum(statkode[mask65_not_dk][:,4])

print(ppl_o_65_nok_dk)


vest_pop = dict()
ost_pop = dict()

for i in range(1992, 2016, 1):
    mask = (statkode[:,1] == 4) & (statkode[:,0] == i)
    # print(np.sum(statkode[mask][:,4]))
    vest_pop[i] = np.sum(statkode[mask][:,4])

# print(vest_pop)

for i in range(1992, 2016, 1):
    mask = (statkode[:,1] == 2) & (statkode[:,0] == i)
    # print(np.sum(statkode[mask][:,4]))
    ost_pop[i] = np.sum(statkode[mask][:,4])

# print(ost_pop)
#7
plt.plot(list(ost_pop.keys()), list(ost_pop.values()), color='g', label='Østerbro')
plt.plot(list(vest_pop.keys()), list(vest_pop.values()), color='orange', label='Vesterbro')
plt.xlabel('Year')
plt.ylabel('Population')
plt.xticks(list(ost_pop.keys()),rotation=90)
plt.legend()
plt.show()