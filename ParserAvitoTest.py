from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
# Функция для создания веб-драйвера и открытия страницы
def create_webdriver():
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(options=options)


# Функция для получения ссылок на объявления с главной страницы
def get_links_from_map_page(link):
    driver = create_webdriver()
    driver.get(link)
    ads_list = driver.find_elements(By.CLASS_NAME, "styles-link-cQMwi")
    link_list = [ad.get_attribute("href") for ad in ads_list]
    driver.quit()
    return link_list


# Функция для получения информации об объявлении
def get_info_from_ad_page(ad_link):
    driver = create_webdriver()
    driver.get(ad_link)

    data = {"link": ad_link}

    # Попытка получить информацию о цене и названии объявления
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


# Основная функция для выполнения запросов в несколько потоков
def main():
    # Ссылка на страницу с объявлениями
    link_to_map = "https://www.avito.ru/krasnodar/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?localPriority=0&map=eyJzZWFyY2hBcmVhIjp7ImxhdEJvdHRvbSI6NDUuMDM2NTMwMjM2MjY5ODU0LCJsYXRUb3AiOjQ1LjA0MjMyOTg2MTk2ODIsImxvbkxlZnQiOjM5LjAwOTMxMzYxNjM0ODIxNiwibG9uUmlnaHQiOjM5LjAyNDU0ODU2MzU1Mjh9LCJ6b29tIjoxN30%3D"

    # Получаем список ссылок на объявления
    link_to_ads_list = get_links_from_map_page(link_to_map)
    print("Get links from avito:")
    print(link_to_ads_list)

    # Создаем список для хранения результатов
    all_data = []

    # Функция для обработки объявлений в отдельном потоке
    def process_ad(ad_link):
        ad_data = get_info_from_ad_page(ad_link)
        all_data.append(ad_data)

    # Создаем потоки для обработки каждого объявления
    threads = []
    for ad_link in link_to_ads_list:
        thread = threading.Thread(target=process_ad, args=(ad_link,))
        thread.start()
        threads.append(thread)

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    # Выводим результат
    print("All data:")
    for data in all_data:
        print(data)

    return all_data



if __name__ == "__main__":
    main()
