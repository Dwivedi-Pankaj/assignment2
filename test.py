from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://gateoverflow.in/")
search = driver.find_element_by_name("q")

#enter scraping criteria:
search.send_keys("sofrware engineering")
search.send_keys(Keys.ENTER)
file1 = open("Pankaj.txt","w") 
for vari in range(1,8):
    title = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div[1]/form/div[1]/div["+str(vari)+"]/div[2]/div/a/span")
    file1.write(title.text) 
    file1.write("\n")
    print(title.text)

file1.close() 

