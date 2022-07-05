from fastapi import FastAPI
import scraper as _scraper

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to this API to get live data about the world population."}

@app.get("/get_world_population")
async def get_world_population():
    return _scraper.get_world_population()

@app.get("/get_todays_births")
async def get_todays_births():
    return _scraper.get_births_today()

@app.get("/get_todays_dea1hs")
async def get_todays_dea1hs():
    return _scraper.get_deaths_today()

@app.get("/get_todays_pop_growth")
async def get_todays_pop_growth():
    return _scraper.get_population_growth_today()

@app.get("/get_years_births")
async def get_years_births():
    return _scraper.get_births_thisyear()

@app.get("/get_years_dea1hs")
async def get_years_dea1hs():
    return _scraper.get_deaths_thisyear()

@app.get("/get_years_pop_growth")
async def get_years_pop_growth():
    return _scraper.get_population_growth_thisyear()

@app.get("/get_country_data")
async def get_country_data(name: str):
    return _scraper.get_country(name)