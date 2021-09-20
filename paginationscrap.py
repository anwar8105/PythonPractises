# Goal collecting all books with 2 star ratings
# from books.scrape.com
import requests, bs4

# gathered_books
gathered_books = []

def build_books(gathered_books):
    # base_URI - 'https://books.toscrape.com/catalogue/page-.html'
    list_URI = []
    book_store = {}
    
    # there are total 50 pages in website
    for num in range(1,51):
        list_URI.append(f'https://books.toscrape.com/catalogue/page-{num}.html')
        
    for index, data in enumerate(list_URI):
        content = bs4.BeautifulSoup(requests.get(data).text, 'lxml')
        
        for data in content.select('.product_pod'):
            if data.select('.star-rating.Two'):
                gathered_books.append(data.select('a')[1]['title'])
                
    return gathered_books
        
build_books(gathered_books)