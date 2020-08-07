from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.select import Select
Options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webdriver_path = 'C:\\chromedriver.exe'
options = Options()
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
driver.get("http://ftp.pcsh.ntpc.edu.tw/libmoodle/login/index.php")

search_input = driver.find_element_by_name("username")
search_input.send_keys('')
search_input = driver.find_element_by_name("password")
search_input.send_keys('')
driver.find_element_by_id('loginbtn').click()
'''
driver.find_element_by_id('expandable_branch_0_mycourses').click()
driver.find_element_by_id('expandable_branch_20_231').click()
driver.find_element_by_id('expandable_branch_30_2476').click()
driver.find_element_by_id('expandable_branch_0_mycourses').click()
driver.find_element_by_id('yui_3_17_2_1_1596773503824_382').click()
'''
driver.get("http://ftp.pcsh.ntpc.edu.tw/libmoodle/mod/quiz/report.php?id=3203&mode=overview")
download = Select(driver.find_element_by_id('downloadtype_download'))
download.select_by_value('excel')
download = Select(driver.find_element_by_id('downloadtype_download'))
download.select_by_value('excel')

driver.find_element_by_class_name("dataformatselector").submit()
#driver.close()
