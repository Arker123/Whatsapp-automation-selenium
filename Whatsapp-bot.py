
#Standard Definations--------------------------

group = "My group"

#--------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
import wikipedia
import pyjokes

#profile_path = r'/home/ark/.mozilla/firefox/s1pio4sk.whatsapp'


options = Options()
options.add_argument("-profile")
options.add_argument("/home/ark/.mozilla/firefox/s1pio4sk.whatsapp")
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=firefox_capabilities, options=options)

#driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get("https://web.whatsapp.com")
 
search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

search_box = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, search_xpath)))

search_box.send_keys(group)

time.sleep(1)

group_xpath = '//span[@title="{g}"]'.format(g=group)

group_title = driver.find_element_by_xpath(group_xpath)

print("Group-title: ",group_title)

group_title.click()

time.sleep(1)
#scroll_xpath = '//div[@data-tab=8][@role="region"]'
#scroll = driver.find_element_by_xpath(scroll_xpath)

#scroll = driver.find_elements_by_xpath('//span[@class="ldL67 _3sh5K"]')

prev_msg = []

while True:
	#scroll = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_2wUmf _21bY5 message-out focusable-list-item"]')))
	scroll = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, '_2wUmf')))
	#print(scroll)
	scroll.send_keys(Keys.END)

	time.sleep(1)

	msg = driver.find_elements_by_class_name("i0jNr")
	
	'''
	print()
	print(msg)
	print()

	for i in range(0,len(msg)):
		print(msg[i].get_attribute("innerHTML"))
	'''
	
	
	if(msg != prev_msg):
		
		prev_msg = msg
		
		print(msg[len(msg)-1].get_attribute("innerHTML"))

		last_msg = msg[len(msg)-1].get_attribute("innerHTML")

		string = last_msg[6:-7]

		print(string)

		L = string.split()
		print(L)
		if (L[0] == '!flag'):
			if(L[1] == '-wiki'):
				if(len(L)>2):
					print(L[2])
					try:
						out = wikipedia.summary(L[2],sentences=3)
						print("Out: ",out)
						send_msg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_13NKt copyable-text selectable-text"][@title="Type a message"]')))
						send_msg.click()
						send_msg.send_keys(out)
						send_msg.send_keys(Keys.ENTER)
					except Exception as e:
						try:
							data = wikipedia.suggest(L[2])
							print("Data",data)
							out = wikipedia.summary(data,sentences=3)
							print("Out: ",out)
							send_msg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_13NKt copyable-text selectable-text"][@title="Type a message"]')))
							send_msg.click()
							send_msg.send_keys(out)
							send_msg.send_keys(Keys.ENTER)
						except:
							print("Exception: ",e)
							out = 'Error'
							send_msg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_13NKt copyable-text selectable-text"][@title="Type a message"]')))
							send_msg.click()
							send_msg.send_keys(out)
							send_msg.send_keys(Keys.ENTER)
			elif(L[1] == '-joke'):
				out = pyjokes.get_joke()
				print(out)
				
				send_msg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_13NKt copyable-text selectable-text"][@title="Type a message"]')))
				send_msg.click()
				send_msg.send_keys(out)
				send_msg.send_keys(Keys.ENTER)
			else:
				out = '*Help Menu*\n -help Display this menu \n -jokes Display a joke \n -wiki Know info about a topic'
				send_msg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_13NKt copyable-text selectable-text"][@title="Type a message"]')))
				send_msg.click()
				send_msg.send_keys(out)
				send_msg.send_keys(Keys.ENTER)


































