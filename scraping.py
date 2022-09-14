# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # setting up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)
    hemisphere_image_urls = hemisphere_scrape(browser)
    # Run all scraping functions and store results in a dictionary.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemisphere_image_urls
    }

    # Stop webdriver and return data.
    browser.quit()
    return data 

# making function for Mars news site.
def mars_news(browser):
    # Scraping Mars News 
    #Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # to parse html
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Scrape article title
        #slide_elem.find('div', class_='content_title')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    # ending function
    return news_title, news_p

# ## JPL Space Images Featured Image
# creating Function for images
def featured_image(browser):
    # Visit url
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Find and click the full size button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'


    return img_url

# ## Mars Facts
# Creating function for Mars Facts.
def mars_facts():
    # Add try/except for error handling
    try:
        #getting table with pandas into a DataFrame
        df = pd.read_html('https://galaxyfacts-mars.com/')[0]

    except BaseException:
        return None

    # assign columns and set index of database.
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert Dataframe into html, add Bootstrap
    return df.to_html()

# Creating function for Hemisphere scrape.
def hemisphere_scrape(browser):
    # 1. Use browser to visit the URL 

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
   
    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    html = browser.html
    hemis_soup = soup(html, 'html.parser')

    # Get the links for each of the 4 hemispheres
    hemis_four = hemis_soup.find_all('h3')
    # loop through each hemisphere link
    for hemis in hemis_four:
        #click the link of the hemisphere
        img_page = browser.find_by_text(hemis.text)
        img_page.click()
        html= browser.html
        img_soup = soup(html, 'html.parser')
        # Scrape the image 
        img_url = 'https://astrogeology.usgs.gov/' + str(img_soup.find('img', class_='wide-image')['src'])
        # Scrape the title
        title = img_soup.find('h2', class_='title').text
        # Define Dictionary
        hemispheres = {'img_url': img_url,'title': title}
        # Append dictionary
        hemisphere_image_urls.append(hemispheres)
        # Return to beginning for next image
        browser.back()
    return hemisphere_image_urls

# app name

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())



