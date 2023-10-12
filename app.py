from selenium import webdriver
from selenium.webdriver.commonkeys import Keys
# pip install selenium
import time

driver = webdriver.Chrome('chromedriver.exe') # 압축푼 파일 경로 및 파일 이름
driver.get('https://instagram.com') # 페이지 이동

time.sleep(4) # 페이지 이동 시간 등에 필요한 시간으로 정지

e = driver.find_elements_by_class_name('아이디에 input 클래스명')[0]
e.send_keys('아이디') # 아이디

e = driver.find_elements_by_class_name('패스워드에 input 클래스명') #[1]
e.send_keys('패스워드') # 패스워드
e.send_keys(Keys.ENTER)

time.sleep(3)

e = driver.find_elements_by_class_name('')[0].text

time.implicitly_wait(5)

e = driver.find_elements_by_class_name('')[0].get_attribute('src')
