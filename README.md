# World-Population-API
An API to get the popular quotes from the site [worldometers.info](https://www.worldometers.info/world-population/).

---

As of right know I'm using Seleniums webdriver to get the page's data, because it takes a second to load all the data which requests is too fast for. So I worked with Selenium to wait out this time, but if you have any way to make the code better/cleaner let me know!

* [Features](#Features)
* [Setup](#Setup)
   * [Virtual Environment](#Virtual-Environment)
   * [Uvicorn](#Uvicorn)
* [Need to know](#Need-to-know)
## Features
You can get:
* Get the live world population
    * All:
    ![world population](/images/get_world_population.gif)
    * Today:
    ![world population today](/images/world_population_today.gif)
    * This year:
    ![world population this year](/images/world_population_year.gif)
* Get the live birth count of...
    * ...today:
    ![todays births](/images/todays_births.gif)
    * ...this year:
    ![this years births](/images/this_years_births.gif)
* Get the live death count of...
    * ...today:
    ![todays births](/images/todays_deaths.gif)
    * ...this year:
    ![this years deaths](/images/this_years_births.gif)
## Setup
### Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
Or use any virtual environment you like.

### Uvicorn
To show the UI I used in the Introduction, we use uvicorn.
You do this as such:
```
uvicorn main:app --reload
```
It should know look like this in your terminal and a browser Window with the API UI should show up.

![Uvicorn Setup](/images/uvicorn_setup.png)

## Need To Know
This API is not to be used neither is being used for commercial use exists to hurt the [worldometers.info](https://www.worldometers.info/) site. 
The API was created because I want to practice my API developing and web scraping skills!
