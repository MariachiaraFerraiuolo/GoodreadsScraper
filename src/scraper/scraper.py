import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import tqdm
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from scraper.chrome_options import CustomChromeOptions
from scraper.text_cleaning import clean_text


class GoodreadsScraper():
    def __init__(self, base_url):
        self.base_url = base_url
        driver = CustomChromeOptions()
        self.driver = driver.create_driver()

    def parse_books(self,book):
        url = book.find_elements(By.CSS_SELECTOR, "a")[0].get_attribute("href")  #initialiting variables to store information about the book
        title = ""
        writer = ""
        avg_rating = ""
        score = ""
        n_voters = ""

        title_elements = book.find_elements(By.CSS_SELECTOR, '[aria-level="4"]')  #extracting the book title
        if len(title_elements) > 0:
            title = title_elements[0].text

        writer_elements = book.find_elements(By.CSS_SELECTOR, 'a.authorName')  #extracting the writer
        if len(writer_elements) > 0:
            writer = writer_elements[0].text

        rating_elements = book.find_elements(By.CSS_SELECTOR, 'span.minirating')  #extracting the rating
        if len(rating_elements) > 0:
            avg_rating = rating_elements[0].text

        score_elements = book.find_elements(By.CSS_SELECTOR, "div > span > a[href='#'][onclick=\"Lightbox.showBoxByID('score_explanation', 300); return false;\"]") #extracting the score
        if len(score_elements) > 0:
            score = score_elements[0].text

        voters_elements = book.find_elements(By.XPATH, "//a[contains(@onclick, 'new Ajax.Request') and "  #extracting the number of voters
                    "contains(@onclick, 'list_book/') and "
                    "contains(@onclick, 'authenticity_token')]")
        if len(voters_elements) > 0:
            n_voters = voters_elements[0].text

        return {
            'url': url,
            'title': title,
            'writer': writer,
            'avg_rating': avg_rating,
            'score': score,
            'n_voters': n_voters
        }

    def extract_books(self, start_year, end_year, num_pages):
        list_of_best_books_y = [] # Initializing an empty list
        wd = self.driver
        for year in tqdm.tqdm(range(start_year, end_year + 1)):  #Looping over 20 years
            year_url = f'{self.base_url}{year}'
            #base_url = f'https://www.goodreads.com/list/best_of_year/{year}'
            

            for num in tqdm.tqdm(range(1, num_pages + 1)):
                url = f"{year_url}?page={num}"
                print(f"Downloading data from {url}")  # which page is being scraped?
                try:
                    self.driver.get(url)

                    # Waiting for the presence of all elements
                    wait = WebDriverWait(self.driver, 10)
                    list_of_books = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#all_votes > table > tbody > tr')))

                    book_details = []  # Initializing an empty list to store book details

                    # Iterate through each book card element
                    for book in list_of_books:
                        book_details.append(self.parse_books(book))

                    list_of_best_books_y.append({
                        'year': year,
                        'books': book_details
                    })

                except TimeoutException as e:
                    print(f"TimeoutException: {e}")
                    break
                except NoSuchElementException as e:
                    print(f"NoSuchElementException: {e}")
                    break

# iterating through the collected book details to extract genres and plots
        for year_data in tqdm.tqdm(list_of_best_books_y):
            for book in tqdm.tqdm(year_data['books']):
                self.driver.get(book['url'])
                try:
                    # Wait until the genre elements are present
                    genre_elements = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BookPageMetadataSection__genres > ul > span:nth-child(1) > span'))
                    )
                    genres = [clean_text(el.text) for el in genre_elements]
                    book['genres'] = genres



                    plot_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.BookPageMetadataSection__description > div > div.TruncatedContent__text--large > div > div > span')
                    plot_text = ' '.join([clean_text(e.text) for e in plot_elements])
                    book['plot'] = plot_text
                except TimeoutException as e:
                    print(f"TimeoutException while fetching genres/plots: {e}")
                except NoSuchElementException as e:
                    print(f"NoSuchElementException while fetching genres/plots: {e}")
        return list_of_best_books_y



    def data_completion(self,list_of_best_books_y):
        data = []
        for year_data in list_of_best_books_y:
            year = year_data['year']
            for book in year_data['books']:
                data.append({
                    'year': year,
                    'url': book.get('url'),
                    'title': book.get('title'),
                    'writer': book.get('writer'),
                    'avg_rating': book.get('avg_rating'),
                    'score': book.get('score'),
                    'n_voters': book.get('n_voters'),
                    'genres': ', '.join(book.get('genres', [])),  # Join list of genres into a single string
                    'plot': book.get('plot')  # Use abstract as it was collected
                })
        return data
 
    def save_file(self, data, filename):
        df = pd.DataFrame(data)
        df.to_csv(f'{filename}.csv',sep='|', encoding='utf-8', index=False)
        df.to_excel(f'{filename}.xlsx', index=False)
        print(f"Data saved to {filename}")


    def quit(self):
        self.driver.quit()



