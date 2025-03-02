from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from pathlib import Path
websites = ["https://dealboxapp.in/", "https://www.shopiq.app/"]

website="https://www.startupindia.gov.in/content/sih/en/search.html?industries=5f48ce5f2a9bb065cdfa1744&roles=Startup&page=40"
path='C:/Program Files/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)  # selenium 4
driver = webdriver.Chrome(service=service)
driver.get(website)
#driver.maximize_window()
Company_Name=[]
Company_website=[]
button=driver.find_elements(by="xpath", value='//div[@class="col-md-4 col-sm-6 col-space20"]/div/a')

print(len(button))
drivers = webdriver.Chrome(service=service)
for x in range(len(button)):
    try:
        #button[x].click()
        company=button[x].get_attribute("href")
        print(company)
        drivers.get(company)
        time.sleep(3)
        Company_website.append(drivers.find_elements(by="xpath", value='//a[@class="website"]')[0].text)
        Company_Name.append(drivers.find_elements(by="xpath", value='//p[@class ="pStartupName"]')[0].text)
        print(len(Company_website))
        if len(Company_website)>15:
            #print(len(Company_website))
            break
        print(Company_website)
    except:
        pass
    time.sleep(5)
    #Company_Name = driver.find_elements(by="xpath",value="//h2[(@class='jobTitle css-1psdjh5 eu4oa1w0') or (@class='jobTitle jobTitle-newJob css-1psdjh5 eu4oa1w0')]/a/span")
    #Company_website.append(button[x].find_elements(by="xpath",value='//a[@class="website"]')[0].text)
    #print(Company_website)
    #time.sleep(5)

df=pd.DataFrame({"Company Name":Company_Name,"Company Website":Company_website})
my_file = Path("E:/Web_Scraping/Project_5/Company2.csv")
print(df)
if open(my_file, "a").tell() == 0: # Check if the file is empty
    df.to_csv(my_file, mode="a", index=False)
else:
    df.to_csv(my_file, mode="a", header=False, index=False)
#df.to_csv('Companies.csv', index=False)
time.sleep(10)
driver.quit()
