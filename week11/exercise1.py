import matplotlib.pyplot as plt
import bs4
from time import sleep
import requests
from selenium import webdriver

browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
url = 'https://www.merchbar.com/search?q=breaking%20benjamin&p=1'

browser.get(url)
browser.implicitly_wait(1)

#Hvor mange produkter kommer frem, 
#når man søger på "breaking benjamin"
#(se URL'en)
def first():
    r = requests.get('https://www.merchbar.com/search?q=breaking%20benjamin')
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    el = soup.find_all('div', class_="d-none d-md-block col-md-3")
    print(el[0].text[:2])

#Hvor mange TRACKs er der i det første produkt, 
#som ligger i kategorien CDs?
def second():
    checkbox = browser.find_elements_by_class_name('ais-RefinementList-labelText')[2]
    checkbox.click()
    sleep(2)
    cd1 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[6]/div[2]/div/div[1]/div')
    cd1.click()
    sleep(2)
    track_list = browser.find_element_by_class_name('track-list')
    tracks = track_list.find_elements_by_class_name('track')
    print(len(tracks))

#Vis et bar chart der viser: 
#- Procentdel af de viste produkter, der rent faktisk 
#   indeholder Breaking Benjamin merch
#- Procentdel af den merch, der er på tilbud
#- Procentdel af den merch, der ikke er på lager
def third():
    all_items = 0
    benja_items = 0
    sale_items = 0
    out_of_stock = 0

    amount_str = '//*[@id="__next"]/div/div[4]/div/div[5]/div[1]/span'

    #Finder alle items
    all_items = int(browser.find_element_by_xpath(amount_str).text[:2])
    print(all_items)
    sleep(2)
    #udvider kategori "Brands/Artists"
    cat1 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[6]/div[1]/button[2]')
    cat1.click()
    #udvider kategori "Avability"
    cat2 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[6]/div[1]/button[6]')
    cat2.click()
    sleep(1)
    #Finder alle checkboxses
    checkbox = browser.find_elements_by_class_name('ais-RefinementList-labelText')
    sleep(1)
    #Checker Breaking Benjamin
    c_benja = checkbox[8]
    c_benja.click()    
    sleep(1)
    benja_items = int(browser.find_element_by_xpath(amount_str).text[:2])
    print(benja_items)
    #Checker On Sale Breaking Benjamin
    c_sale = checkbox[0]
    c_sale.click()
    sleep(1)
    sale_items = int(browser.find_element_by_xpath(amount_str).text[:2])
    print(sale_items)
    #Unchecker On Sale og checker Out of stock
    c_sale.click()
    c_out_of_stock = checkbox[23]
    c_out_of_stock.click()
    sleep(1)
    out_of_stock = int(browser.find_element_by_xpath(amount_str).text[:2])
    print(out_of_stock)

    pct_benja = benja_items/all_items * 100
    pct_on_sale = sale_items/all_items * 100
    pct_out_of_stock = out_of_stock/all_items * 100

    data = {'BB': pct_benja, 'BB sale': pct_on_sale,
            'BB not in stock': pct_out_of_stock}

    plt.bar(data.keys(), data.values(), width=0.35, align='center')
    plt.axis([-1, len(data.values()), 0, 100])
    plt.title('Breaking Benjamin merchandise', fontsize=12)
    plt.ylabel('Percentage', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()



#first()
#second()
third()