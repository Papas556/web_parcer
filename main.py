from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os,time


path = os.getcwd()
chromedriver_path = os.path.join(path,"chrome_driver","chromedriver.exe")
service = Service(chromedriver_path)
service.start()
driver = webdriver.Remote(service.service_url)
driver.implicitly_wait(10)


def get_links(url,selector):
    driver.get(url)
    time.sleep(5) # Let the user actually see something!
    shops_links = driver.find_elements_by_class_name(selector)
    list_links = []
    for shop in shops_links:
        link = shop.get_attribute("href")
        list_links.append(link)
    return list_links


page_num = "b-button__root"
retailers_selector = "p-retailers__retailer"
retailers_url = "https://edadeal.ru/moskva/retailers"
button_selector = "b-button__root"
retailers_links = get_links(url=retailers_url, selector=retailers_selector)
print(retailers_links)
def find_max(link,page_num,):
    magazine1 = get_links(url=link, selector=page_num)
    print(magazine1)
    numbers = []
    for link in magazine1:
        if link != None:
            #print(link)
            if "=" in link:
                link = link.split("=")
                start = link[0]
                number = int(link[-1])
                numbers.append(number)
    print(start)
    print(numbers)
    max_number = max(numbers)
    print (max_number)
    return start, max_number
start,max_number = find_max(retailers_links[1],page_num)
def links_for_pages (start, max_number):
    num = 2
    page_links = []
    while num <= max_number:
        combiner = start + "="+str(num)
        num = num + 1
        page_links.append(combiner)
        print(combiner)
    return page_links
page_links = links_for_pages(start,max_number)
good_selector = "p-retailer__offer"
goods_links = get_links(url=page_links[1], selector=good_selector)
print(retailers_links)
def get_info(goodlink):
    driver.get(goodlink)
    retailer = driver.find_element_by_class_name("p-offer__retailer-title")
    print(retailer.text)
    description = driver.find_element_by_class_name("p-offer__description")
    print(description.text)
get_info(goods_links[0])
time.sleep(10)


driver.quit()