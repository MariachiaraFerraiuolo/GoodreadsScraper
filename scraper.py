from chrome_options import get_chrome_options, create_driver
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def scraper():
    wd = create_driver(headless=False)
    wd.get("https://www.goodreads.com/list/best_of_year/2014")
    wd.save_screenshot('screenshot.png')
    img = mpimg.imread('/content/screenshot.png')
    plt.figure(figsize=(20, 10))
    imgplot = plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()

scraper()