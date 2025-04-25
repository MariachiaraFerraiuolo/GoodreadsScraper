from src.scraper.scraper import GoodreadsScraper


if __name__ == '__main__':
    scraper = GoodreadsScraper(base_url='https://www.goodreads.com/list/best_of_year/')
    books_data = scraper.extract_books(start_year=2004, end_year=2025, num_pages=5)
    data = scraper.data_completion(books_data)
    scraper.save_to_excel(data, r'output\goodreads_best_books_2004_2025.xlsx')
    scraper.quit()
