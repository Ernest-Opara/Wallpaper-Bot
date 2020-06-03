# picture scraping for the bot

import cfscrape
from bs4 import BeautifulSoup as bs
import os

# website with images
url = 'http://www.ewallpapers.eu/search_size/iPhone1'

scraper = cfscrape.create_scraper()

# download page for parsing
page = scraper.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for images
if not os.path.exists('Images'):
    os.makedirs('Images')

# move to new directory
os.chdir('Images')

# image file name variable
x = 0

# writing images
while True:
    for image in image_tags:
        try:
            url = image['src']
            response = scraper.get(url)
            if response.status_code == 200:
                with open('wallpaperpexels-' + str(x) + '.jpg', 'wb') as f:
                    f.write(scraper.get(url).content)
                    f.close()
                    x += 1

        except:
            pass
