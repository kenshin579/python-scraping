from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())

savedCookies = driver.get_cookies()

driver2 = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver2.get("http://pythonscraping.com")
driver2.delete_all_cookies()
for cookie in savedCookies:
    driver2.add_cookie(cookie)

driver2.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver2.get_cookies())

'''
warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless 
- 이제 phantomjs 대신 chrome의 headless를 사용함

참고
- https://beomi.github.io/2017/09/28/HowToMakeWebCrawler-Headless-Chrome/

'''