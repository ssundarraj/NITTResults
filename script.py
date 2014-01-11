from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def setDriver():
	url="http://www.nitt.edu/prm/nitreg/ShowRes.aspx"
	driver = webdriver.Firefox()
	driver.get(url)
	return driver

def closeDriver(driver):
	driver.close()

def latestSem(rno, driver):
	elem = driver.find_element_by_name("TextBox1")
	elem.send_keys(Keys.CONTROL, 'a')
	elem.send_keys("\b")
	elem.send_keys(rno)
	elem.send_keys(Keys.RETURN)
	el = driver.find_element_by_id('Dt1')
	sem_id_value_ini=0
	for option in el.find_elements_by_tag_name('option'):
		sem_id_value_ini=option.get_attribute('value')

	elem = driver.find_element_by_name("TextBox1")
	elem.send_keys(Keys.CONTROL, 'a')
	elem.send_keys("\b")
	elem.send_keys(int(rno)+1)
	elem.send_keys(Keys.RETURN)
	el = driver.find_element_by_id('Dt1')
	sem_id_value_alt=0
	for option in el.find_elements_by_tag_name('option'):
		sem_id_value_alt=option.get_attribute('value')

	elem = driver.find_element_by_name("TextBox1")
	elem.send_keys(Keys.CONTROL, 'a')
	elem.send_keys("\b")
	elem.send_keys(int(rno)+2)
	elem.send_keys(Keys.RETURN)
	el = driver.find_element_by_id('Dt1')
	sem_id_value_alt1=0
	for option in el.find_elements_by_tag_name('option'):
		sem_id_value_alt1=option.get_attribute('value')

	sem_id_value=min(sem_id_value_ini, sem_id_value_alt, sem_id_value_alt1)
	return sem_id_value

def getGPA(rno, sem_id_value):
	elem = driver.find_element_by_name("TextBox1")
	elem.send_keys(Keys.CONTROL, 'a')
	elem.send_keys("\b")
	elem.send_keys(rno)
	elem.send_keys(Keys.RETURN)
	el = driver.find_element_by_id('Dt1')
	for option in el.find_elements_by_tag_name('option'):
		if option.get_attribute('value')==sem_id_value:
			option.click()
	name=driver.find_element_by_id('LblName').text
	gpa=driver.find_element_by_id('LblGPA').text
	print str(rno) + "\t" + name + "\t" +  gpa


if __name__=="__main__":
	driver = setDriver()
	start_rno=sys.argv[1]
	end_rno=0
	end_rno=sys.argv[2]
	if(end_rno==0):
		getGPA(start_rno, latestSem(rno, driver))
	else:
		sem_id=latestSem(start_rno, driver)
		for i in range(int(end_rno) - int(start_rno)+1):
			try:
				getGPA(int(start_rno)+i, sem_id)
			except:
				pass
	closeDriver(driver)