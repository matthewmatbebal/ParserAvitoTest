import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import const


def create_webdriver():
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(options=options)


def get_links_from_map_page(link):
    map_page = create_webdriver()
    map_page.get(link)


    time.sleep(2)
    # get links from map page
    ads_from_map_page_list = map_page.find_elements(By.CLASS_NAME,
                                                    const.ADS_LINK_CLASS)  # TODO аналогично делаем для других классов / id
    # TODO should check count of ads_from_map_page_list. If more 12 -> skip
    print(ads_from_map_page_list)
    link_list = []  # начало нового скрипта
    ads_count = 0
    for current_ad in ads_from_map_page_list:
        ad_link = current_ad.get_attribute("href")
        link_list.append(ad_link)
        ads_count += 1
        if ads_count >= 12:
            break

    map_page.quit()
    return link_list  # конец нового скрипта

    # link_list = [current_ad.get_attribute("href") for current_ad in ads_from_map_page_list]
    #
    # map_page.quit()
    # return link_list


def get_info_from_ad_page(ad_link):
    driver = create_webdriver()
    driver.get(ad_link)

    data = {"link": ad_link}


    try:
        ad_name_element = driver.find_element(By.CSS_SELECTOR, '.styles-module-root-TWVKW.styles-module-root-_KFFt.styles-module-size_xxxl-A2qfi.styles-module-size_xxxl-_bK04.stylesMarningNormal-module-root-OSCNq.stylesMarningNormal-module-header-3xl-k0ckc')
        data["ad_name"] = ad_name_element.text
    except:
        data["ad_name"] = "N/A"

    try:
        square_field_elements = driver.find_elements(By.CSS_SELECTOR, ".params-paramsList__item-_2Y2O")
        for square_field_element in square_field_elements:
            square_field_element_text = square_field_element.text
            if "сот." in square_field_element_text:
                splited_square_field = square_field_element_text.split(":")[1].strip()
                data["square_field"] = splited_square_field

    except:
        data["square_field"] = "N/A"

    try:
        square_house_elements = driver.find_elements(By.CLASS_NAME, "params-paramsList__item-_2Y2O")
        for square_house_element in square_house_elements:
            square_house_element_text = square_house_element.text
            if "м²" in square_house_element_text:
                splited_square_house = square_house_element_text.split(":")[1].strip()
                data["square_house"] = splited_square_house
    except:
        data["square_house"] = "N/A"

    try:
        price_element = driver.find_element(By.CSS_SELECTOR, "[itemprop='price']")
        price_content = price_element.get_attribute("content")
        data["price"] = price_content
    except:
        data["price"] = "N/A"

    try:
        price_per_meter_element = driver.find_element(By.CSS_SELECTOR,
                                                      ".styles-module-root-_KFFt.styles-module-size_s-awPvv.styles-module-size_s-_P6ZA.stylesMarningNormal-module-root-OSCNq.stylesMarningNormal-module-paragraph-s-_c6vD.styles-module-root_top-HYzCt.styles-module-margin-top_8-pY2CC")
        data["price_per_meter"] = price_per_meter_element.text
    except:
        data["price_per_meter"] = "N/A"

    try:
        views_count_element = driver.find_element(By.CSS_SELECTOR, "[data-marker='item-view/total-views']")
        data["views_count"] = views_count_element.text
    except:
        data["views_count"] = "N/A"

    driver.quit()
    #return data
    print(data)


get_info_from_ad_page("https://www.avito.ru/krasnodar/doma_dachi_kottedzhi/dom_500_m_na_uchastke_6_sot._2805001904")
