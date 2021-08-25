from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
from bs4 import BeautifulSoup
import pandas as pd
import dask.dataframe as dd
from time import sleep

driver=webdriver.Chrome("/usr/bin/chromedriver")
driver.get("https://www.worldometers.info/coronavirus/")
print(driver.title)

driver.implicitly_wait(5)

# Step 2: Parse HTML code and grab tables with Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')
soup.prettify()



# Search for the table and extracting it
table = soup.find('table', attrs={'id': 'main_table_countries_today'})
#print(table)


rows = table.find_all("tr", attrs={"style": ""})

data = []
for i,item in enumerate(rows):
    
    if i == 0:
        
        data.append(item.text.strip().split("\n")[:13])
        
    else:
        data.append(item.text.strip().split("\n")[:12])


#print(data)

dt = pd.DataFrame(data)
dt = pd.DataFrame(data[1:], columns=data[1][:12]) #Formatting the header
df = dd.from_pandas(dt,npartitions=1)

print(df.head())
df.to_csv('data-2.csv',index="False")



driver.quit()





# driver.maximize_window()

# pageSource = driver.page_source
# fileToWrite = open("page_source.html", "w")
# fileToWrite.write(pageSource)
# fileToWrite.close()
# fileToRead = open("page_source.html", "r")
# print(fileToRead.read())
# fileToRead.close()

# # to identify the table rows
# r = driver.find_elements_by_id("//table[@id= 'main_table_countries_today']/tbody/tr")
# # to identify table columns
# c = driver.find_elements_by_xpath ("//*[@id= 'main_table_countries_today']/tbody/tr/td")
# # to get row count with len method
# rc = len (r)
# # to get column count with len method
# cc = len (c)
# # to traverse through the table rows excluding headers
# for i in range (2, rc + 1) :
# # to traverse through the table column 
#     for j in range (1, cc + 1) :
# # to get all the cell data with text method
#         d = driver.find_element_by_xpath ("//tr["+str(i)+"]/td["+str(j)+"]").text
# print (d)




# wait = WebDriverWait(driver,10)

# while True:
#     try:
#         item = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@id,"main_table_countries_today")]/a')))
        
#     except Exception:break

# for table in wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[contains(@id,"main_table_countries_today")]//tr'))):
#     data = [item.text for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
#     print(data)


  
# # Printing the URL

# # print(driver.find_element_by_xpath("/html/body").text)