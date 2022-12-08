from bs4 import BeautifulSoup as bs
import requests
from selenium.webdriver import Edge


driver = Edge()
url = 'https://emias.info/appointment/create'
driver.get(url)
driver.find_element_by_xpath("//div[@class='Fkj7oZ f1y1sl b4SQ_y']/input[@class='P8KZKM' and @type='tel' and @value='' and @size='1' and @placeholder='Например, 7100 0000 0000 0000']").click()
driver.find_element_by_xpath("//div[@class='Fkj7oZ f1y1sl b4SQ_y']/input[@class='P8KZKM' and @type='tel' and @value='' and @size='1' and @placeholder='Например, 7100 0000 0000 0000']").clear()
driver.find_element_by_xpath("//div[@class='Fkj7oZ f1y1sl b4SQ_y']/input[@class='P8KZKM' and @type='tel' and @value='' and @size='1' and @placeholder='Например, 7100 0000 0000 0000']").send_keys("1111 1111 1111 1111")
# <div class="Fkj7oZ f1y1sl b4SQ_y"><input size="1" type="tel" name="policy" placeholder="Например, 7100 0000 0000 0000" class="P8KZKM" value=""></div>
bdate = {
    'day': '01',
    'month': '01',
    'year': '1999'
}
for data in bdate:
    driver.find_element_by_xpath(f"//div[@class='Fkj7oZ ThvYXi f1y1sl']/input[@class='P8KZKM' and @type={data.key} and @value='']").click()
    driver.find_element_by_xpath(f"//div[@class='Fkj7oZ ThvYXi f1y1sl']/input[@class='P8KZKM' and @type={data.key} and @value='']").clear()
    driver.find_element_by_xpath(f"//div[@class='Fkj7oZ ThvYXi f1y1sl']/input[@class='P8KZKM' and @type={data.key} and @value='']").send_keys(data.value)
# <div class="Fkj7oZ ThvYXi f1y1sl"><input type="text" name="day" placeholder="День" class="P8KZKM" value=""><input type="text" name="month" placeholder="Месяц" class="P8KZKM" value=""><input type="text" name="year" placeholder="Год" class="P8KZKM" value=""></div>

