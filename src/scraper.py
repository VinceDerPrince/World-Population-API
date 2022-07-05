from typing import Dict, List

import bs4 as _bs4

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import re



url = "https://www.worldometers.info/world-population/"

def _get_page(url: str) -> _bs4.BeautifulSoup:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path="/Users/vince/Downloads/geckodriver")
    driver.get(url)
    page = driver.page_source
    driver.close()
    soup = _bs4.BeautifulSoup(page, "html.parser")
    return soup

def get_world_population() -> Dict:
    page = _get_page(url)
    billions = page.find_all(class_="maincounter-number")
    population = [billion.text for billion in billions]
    output = {"world population":int("".join(population[0].split(",")))}
    return output

def get_births_today() -> Dict:
    page = _get_page(url)
    births = page.find_all(rel="births_today")
    births_today = [birth.text for birth in births]
    output = {"births today":int("".join(births_today[0].split(",")))}
    return output

def get_deaths_today() -> Dict:
    page = _get_page(url)
    deaths = page.find_all(rel="dth1s_today")
    deaths_today = [death.text for death in deaths]
    output = {"deaths today":int("".join(deaths_today[0].split(",")))}
    return output

def get_population_growth_today() -> Dict:
    page = _get_page(url)
    growths = page.find_all(rel="absolute_growth")
    population_growth_today = [growth.text for growth in growths]
    output = {"population growth today":int("".join(population_growth_today[0].split(",")))}
    return output

def get_births_thisyear() -> Dict:
    page = _get_page(url)
    births = page.find_all(rel="births_this_year")
    births_thisyear = [birth.text for birth in births]
    output = {"births this year":int("".join(births_thisyear[0].split(",")))}
    return output

def get_deaths_thisyear() -> Dict:
    page = _get_page(url)
    deaths = page.find_all(rel="dth1s_this_year")
    deaths_thisyear = [death.text for death in deaths]
    output = {"deaths this year":int("".join(deaths_thisyear[0].split(",")))}
    return output

def get_population_growth_thisyear() -> Dict:
    page = _get_page(url)
    growths = page.find_all(rel="absolute_growth_year")
    population_growth_thisyear = [growth.text for growth in growths]
    output = {"population growth this year":int("".join(population_growth_thisyear[0].split(",")))}
    return output

def get_country(name: str) -> List:
    page = _get_page("https://www.worldometers.info/world-population/population-by-country/")
    countries = page.find_all(role="row")
    country_man = []
    for country in countries:
        wacka = []
        for i in country:
            if i.get_text() != " ":
                wacka.append(i.get_text())
        country_man.append(wacka)

    quotes = dict()
    for page in range(1,236):
        if page not in quotes:
            quotes[page] = dict()
        for j in range(11):
            quotes[page][country_man[0][j]] = country_man[page][j]
    result = []
    for i in range(1,236):
        print(f"{i}: ",quotes[i]["Country (or dependency)"].lower())
        if quotes[i]["Country (or dependency)"].lower() == name.lower():
            result.append(quotes[i])
    return result