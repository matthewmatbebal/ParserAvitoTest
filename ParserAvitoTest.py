import threading
import Parser

all_data = []


def process_ad(ad_link_):
    ad_data = Parser.get_info_from_ad_page(ad_link_)
    all_data.append(ad_data)


def main(link_to_map):
    all_data.clear()
    threads = []

    #link_to_map = "https://www.avito.ru/krasnodar/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?localPriority=0&map=eyJzZWFyY2hBcmVhIjp7ImxhdEJvdHRvbSI6NDUuMDM2NTMwMjM2MjY5ODU0LCJsYXRUb3AiOjQ1LjA0MjMyOTg2MTk2ODIsImxvbkxlZnQiOjM5LjAwOTMxMzYxNjM0ODIxNiwibG9uUmlnaHQiOjM5LjAyNDU0ODU2MzU1Mjh9LCJ6b29tIjoxN30%3D"
    link_to_ads_list = Parser.get_links_from_map_page(link_to_map)

    print("Get links from avito:")
    print(link_to_ads_list)

    for ad_link in link_to_ads_list:
        thread = threading.Thread(target=process_ad, args=(ad_link,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("All data:")
    for data in all_data:
        print(data)

    return all_data


if __name__ == "__main__":
    main()
