# Mission-to-Mars
## Purpose 
### Objective
This project was done to create a web app that keeps updated information about the "Red planet", Mars, with a push of a button. In order to complete this, the project was done in two phases, Original and Challenge.
#### The Original Phase included:
1. Scraping for the latest mars article, a featured image, and a facts table.
2. Designing a on HTML index to layout the web app.
3. Connecting to Mongo with PyMongo and Flask to display all scraped information on the Mars web app. 

#### The Challenge Phase included:
1. Scraping images and titles of the hemispheres of Mars.
2. Updating the HTML index to loop through the images found and        displaying them using Mongo, Flask, and PyMongo.
3. Adding new design elements with BootStrap and CSS.

### Data Environment
Here are some to of the tools use for this project:
- BeautifulSoup
- Mongo
- Splinter
- Flask 
- Bootstrap
- Jupyter Notebook
- Python

## Results
### Original phase
The image below shows a succesful run of the original phase code. The Web app is fucntioning.
##### Original web app run.
![orig](https://user-images.githubusercontent.com/105830665/190166316-e81154b2-7772-49a7-9158-92c4cf639783.png)

### Challenge Phase
Here are the 3 additions to the Original Phase.

#### 1. **Scraping for Hemisphere images and titles**

![deliv1](https://user-images.githubusercontent.com/105830665/190167111-d6901de8-d8de-46a9-b2ae-81a67018bc0f.png)

This is the list holding the dictionary of images and titles.

#### 2. **Update the Web App with the Hemisphere images and titles**

![deliv2](https://user-images.githubusercontent.com/105830665/190167726-1d4ddb33-1c2a-4a98-b831-9297f3ab9da7.png)

The Web App now has a new section for the Hemispheres.

#### 3. **Adding additional Bootstrap Elements**

![Deliv3 4](https://user-images.githubusercontent.com/105830665/190168231-f2eb03a1-f173-444e-938f-41fd41bf017a.png)

There are 4 additional elements
      1. The color of the Jumbotron changed to orange.
      2. The Button is now activate.
      3. The Featured image is a thumdnail.
      4. The Hemisphere images are thumbnails side by side.

## Summary
The Mars News Web App is a functioning app. The app has been tested several times. With each new test the code pulls the latest article from the Nasa website. All Bootstrap additions and the updated HTML code work with each new scrape. The web app is sized to work on any device from a cell phone to large desktop. 