from selenium import webdriver
from selenium.webdriver.common.by import By

import const


def create_webdriver():
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(options=options)


def get_links_from_map_page(link):
    map_page = create_webdriver()
    map_page.get(link)

    # get links from map page
    ads_from_map_page_list = map_page.find_elements(By.CLASS_NAME,
                                                    const.ADS_LINK_CLASS)  # TODO аналогично делаем для других классов / id
    # TODO should check count of ads_from_map_page_list. If more 12 -> skip

    link_list = [current_ad.get_attribute("href") for current_ad in ads_from_map_page_list]

    map_page.quit()
    return link_list


def get_info_from_ad_page(ad_link):
    driver = create_webdriver()
    driver.get(ad_link)

    data = {"link": ad_link}

    try:
        price_element = driver.find_element(By.CLASS_NAME, "styles-module-size_xxxl-A2qfi")
        data["price"] = price_element.text
    except:
        data["price"] = "N/A"

    try:
        name_element = driver.find_element(By.CSS_SELECTOR, "[itemprop='name']")
        data["name"] = name_element.text
    except:
        data["name"] = "N/A"

    driver.quit()
    return data