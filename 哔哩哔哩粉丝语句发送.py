import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
browser.get("https://www.bilibili.com/")
time.sleep(2)
login = browser.find_element_by_class_name("name")
ActionChains(browser).move_to_element(login).click().perform()
window = browser.window_handles
browser.switch_to.window(window[-1])
print("等待登录")
login_page_url = "https://passport.bilibili.com/login"
while True:
    time.sleep(2)
    if browser.current_url != login_page_url:
        break

# 直接跳转到粉丝界面
browser.get("https://space.bilibili.com/32912435/fans/fans")
all_fans_name = WebDriverWait(browser,10).until(lambda browser:browser.find_elements_by_xpath(
    "//li[@class='list-item clearfix']/div[@class='content']//a[@class='title']"))
names = [name.text for name in all_fans_name]
# 获取所有的消息链接
all_links_ele = WebDriverWait(browser,10).until(lambda browser:browser.find_elements_by_xpath("//li[@class='be-dropdown-item']/a"))
all_fans_links = [link.get_attribute('href') for link in all_links_ele]

for i in range(len(all_fans_links)):
    print("{}:昵称:{}".format(i+1,names[i]))
    browser.get(all_fans_links[i])
    browser.refresh()
    text_area = WebDriverWait(browser, 10000).until(lambda browser: browser.find_element_by_css_selector(
        "div.router-view div.card.whisper div.dialog div.send-box div.input-box textarea.textarea"))
    text_area.send_keys("你好哇,小可爱")

