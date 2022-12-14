from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options as EdgeOptions
import time 

options = EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = Edge(options=options)
url = 'https://emias.info/appointment/create'
driver.get(url)
# <div class="Fkj7oZ f1y1sl b4SQ_y"><input size="1" type="tel" name="policy" placeholder="Например, 7100 0000 0000 0000" class="P8KZKM" value=""></div>
data = {'day': '03', 'month': '03', 'year': '1998', 'policy': '3656 1008 9600 0147'}
for key in data.keys():
    driver.find_element(By.NAME, f'{key}').click()
    driver.find_element(By.NAME, f'{key}').clear()
    driver.find_element(By.NAME, f'{key}').send_keys(data[key])
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.zhplzA.TW_Q0E.zP2XPk.M50fgr').click()
# driver.switch_to(driver.window_handles[1])
# print(help(driver))
# <button type="submit" class="zhplzA TW_Q0E zP2XPk M50fgr"><span class="sXdASz"><span class="AuEX2H">Записаться</span></span><div class="v5Rdd4 JX7z9X"><svg class="vNdVC3 d27STn"><use xlink:href="#loader"></use></svg></div></button>
# <div class="Fkj7oZ ThvYXi f1y1sl"><input type="text" name="day" placeholder="День" class="P8KZKM" value=""><input type="text" name="month" placeholder="Месяц" class="P8KZKM" value=""><input type="text" name="year" placeholder="Год" class="P8KZKM" value=""></div>


