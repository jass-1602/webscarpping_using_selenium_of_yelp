from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
import pandas as pd
driver = webdriver.Firefox()
driver = webdriver.Firefox()
# driver = webdriver.Chrome(ChromeDriverManager().install())
import pandas as pd
import time
import os

Phone = []
links = []
Name=[]
for page in range(0, 240, 10):


    page_url="https://www.yelp.com/search?find_desc=Restaurants&find_loc=paris"+ str(page)
    driver = webdriver.Firefox()
    driver.get(page_url)

            # elements = driver.find_elements(By.CLASS_NAME,'css-1422juy')
    elements = driver.find_elements(By.XPATH,'/html/body/yelp-react-root/div[1]/div[4]/div[2]/div/div[1]/div/main/div/ul/li/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/h3/span/a')

            # elements = driver.find_elements(By.CLASS_NAME,'css-uvzfg9') yeh wala nhichl rha

    for i in range(len(elements)):
        links.append(elements[i].get_attribute('href'))
        # print(len(links))
        # print(links)
    for link in links:
        print('navigating to:',link)
            # driver.implicitly_wait(3)
        #     # c=driver.find_element(By.XPATH,'/html/body/yelp-react-root/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/h1')
        #     driver.implicitly_wait(3)
        #     # Name.append(c.text)
        driver.get(link)
            # driver.implicitly_wait(2)
            # time.sleep(10)
        # if driver.find_element(By.XPATH, '/html/body/yelp-react-root/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/h1') and driver.find_element(By.XPATH,'/html/body/yelp-react-root/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div//div/div[2]/div/div[1]/p[2]'):
        phone= driver.find_element(By.XPATH, '/html/body/yelp-react-root/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/h1')

        c=driver.find_element(By.XPATH,'/html/body/yelp-react-root/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div//div/div[2]/div/div[1]/p[2]')
        Phone.append(phone.text)
        Name.append(c.text)

        # f=open("yelp_data.csv",'w')

            # f = open('yelp_data.csv', 'a')
        data={"Name":Name,"Phone":Phone}
                    # writer = csv.writer(f)
                    # writer.writerow(Name)
                    # writer.writerow(Phone)
        df = pd.DataFrame(data)
        df.columns = ['Phone','Name']
        # with open("yelp_data.csv", "r+") as file:
        #     for line in file:
        #         if df in line:
        #             break
        #
        #         else:
        df.rename(columns={0:'Name',1:'Phone'},inplace=True)
        df.to_csv('paris_data.csv',index=False)


        # f.close()
    driver.back()

print(Name)
print(Phone)
