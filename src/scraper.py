import bs4 as _bs4
import requests as _requests
from typing import List, Dict
import time
from selenium import webdriver

driver = webdriver.Safari()


def _get_page(url: str) -> _bs4.BeautifulSoup:
    # page = _requests.get(url)
    driver.get(url)
    page = driver.page_source
    soup = _bs4.BeautifulSoup(page, "html.parser")
    return soup

def get_world_population() -> Dict:
    url = "https://www.worldometers.info/world-population/"
    page = _get_page(url)
    billions = page.find_all(class_="maincounter-number")
    population = [billion.text for billion in billions]
    output = {"world population":int("".join(population[0].split(",")))}
    return output

def get_births_today() -> Dict:
    url = "https://www.worldometers.info/world-population/"
    page = _get_page(url)
    births = page.find_all(rel="births_today")
    births_today = [birth.text for birth in births]
    output = {"births today":int("".join(births_today[0].split(",")))}
    return output

def get_deaths_today() -> Dict:
    url = "https://www.worldometers.info/world-population/"
    page = _get_page(url)
    deaths = page.find_all(rel="dth1s_today")
    deaths_today = [death.text for death in deaths]
    output = {"deaths today":int("".join(deaths_today[0].split(",")))}
    return output

def get_population_growth_today() -> Dict:
    url = "https://www.worldometers.info/world-population/"
    page = _get_page(url)
    growths = page.find_all(rel="absolute_growth")
    population_growth_today = [growth.text for growth in growths]
    output = {"population growth today":int("".join(population_growth_today[0].split(",")))}
    return output

def get_births_thisyear() -> Dict:
    url = "https://www.worldometers.info/world-population/"
    page = _get_page(url)
    births = page.find_all(rel="births_this_year")
    births_thisyear = [birth.text for birth in births]
    output = {"births this year":int("".join(births_thisyear[0].split(",")))}
    return output

def get_deaths_thisyear() -> Dict:
    url = "https://www.worldometers.info/world-population/"
    page = _get_page(url)
    deaths = page.find_all(rel="dth1s_this_year")
    deaths_thisyear = [death.text for death in deaths]
    output = {"deaths this year":int("".join(deaths_thisyear[0].split(",")))}
    return output

def get_population_growth_thisyear() -> Dict:
    url = "https://www.worldometers.info/world-population/"
    page = _get_page(url)
    growths = page.find_all(rel="absolute_growth_year")
    population_growth_thisyear = [growth.text for growth in growths]
    output = {"population growth this year":int("".join(population_growth_thisyear[0].split(",")))}
    return output
