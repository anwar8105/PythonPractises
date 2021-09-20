# Goal collecting all books title's with 2 star ratings
# sourcesite : books.scrape.com

import requests, bs4

# list of collected titles
collected_titles = []

def build_books(collected_titles):
    # base_URI - 'https://books.toscrape.com/catalogue/page-.html'
    list_URI = []
    
    # there are total 50 pages in website
    for num in range(1,51):
        list_URI.append(f'https://books.toscrape.com/catalogue/page-{num}.html')
        
    for index, data in enumerate(list_URI):
        content = bs4.BeautifulSoup(requests.get(data).text, 'lxml')
        
        for data in content.select('.product_pod'):
            if data.select('.star-rating.Two'):
                collected_titles.append(data.select('a')[1]['title'])
                
    return collected_titles
        
build_books(collected_titles)