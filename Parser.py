import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import const


def create_webdriver():
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("disable-extensions")
    options.add_argument("disable-gpu")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-infobars")
    options.add_argument("disable-features=VizDisplayCompositor")
    options.add_argument("disable-features=IsolateOrigins,site-per-process")
    options.add_argument("blink-settings=imagesEnabled=false")
    return webdriver.Chrome(options=options)


def get_links_from_map_page(link):
    map_page = create_webdriver()
    map_page.get(link)
    ip_locks_map_page = map_page.find_elements(By.CSS_SELECTOR, "html")
    for ip_lock_map in ip_locks_map_page:
        if "Доступ ограничен" in ip_lock_map.text:
            print("Блокировка по IP, открытие новой вкладки")
            time.sleep(5)
            map_page.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")
            map_page.switch_to.window(map_page.window_handles[-1])
            time.sleep(5)
            map_page.get(link)



    time.sleep(2)
    ads_from_map_page_list = map_page.find_elements(By.CLASS_NAME,
                                                    const.ADS_LINK_CLASS)
    print(ads_from_map_page_list)
    link_list = [current_ad.get_attribute("href") for current_ad in ads_from_map_page_list[:12]]
    map_page.quit()
    return link_list

    # link_list = []  # начало нового скрипта
    # ads_count = 0
    # for current_ad in ads_from_map_page_list:
    #     ad_link = current_ad.get_attribute("href")
    #     link_list.append(ad_link)
    #     ads_count += 1
    #     if ads_count >= 12:
    #         break
    #
    # map_page.quit()
    # return link_list  # конец нового скрипта


def get_info_from_ad_page(ad_link):
    driver = create_webdriver()
    driver.get(ad_link)

    ip_locks_ad_page = driver.find_elements(By.CSS_SELECTOR, "html")
    for ip_lock_ad in ip_locks_ad_page:
        if "Доступ ограничен" in ip_lock_ad.text:
            print("Блокировка по IP, открытие новой вкладки")
            time.sleep(5)
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(5)
            driver.get(ad_link)

    data = {"link": ad_link}

    try:
        ad_name_element = driver.find_element(By.CSS_SELECTOR,
                                              '.styles-module-root-TWVKW.styles-module-root-_KFFt.styles-module-size_xxxl-A2qfi.styles-module-size_xxxl-_bK04.stylesMarningNormal-module-root-OSCNq.stylesMarningNormal-module-header-3xl-k0ckc')
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
        image_button = driver.find_element(By.CSS_SELECTOR, "[data-marker='item-phone-button/card']")
        image_button.click()
        time.sleep(3)
        image = driver.find_element(By.CSS_SELECTOR,
                                    ".styles-module-root-SfSd4.styles-module-margin-top_none-urOXk.styles-module-margin-bottom_none-YEOJI.styles-module-root_align_center-Oadab")
        data["phone"] = image.screenshot_as_base64
    except:
        data["phone"] = "N/A"

    try:
        views_count_element = driver.find_element(By.CSS_SELECTOR, "[data-marker='item-view/total-views']")
        data["views_count"] = views_count_element.text
    except:
        data["views_count"] = "N/A"

    driver.quit()
    return data
    # print(data)

# get_info_from_ad_page("https://www.avito.ru/krasnodar/doma_dachi_kottedzhi/dom_500_m_na_uchastke_6_sot._2805001904")
