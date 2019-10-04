# # Local imports (relative)
# from database.manager import db

# Local imports (absolute)
from Examples.sample_oo_api.database.manager import db


# City calls
def get_city(name: str) -> dict:
    """
    API Controlled method to retrieve city details for specified city
    Arguements:
    - name <str> name of the city

    Returns a dict with information about the requested city
    """
    return db.City.where('Name', '=', name.capitalize()).get().serialize()


def get_city_all():
    """
    API Controlled method to retrieve city details for all available cities

    Returns a dict with information about all available cities
    """
    return db.City.all().serialize()


def get_country(name: str) -> dict:
    """
    API Controlled method to retrieve country details for specified country
    Arguements:
    - name <str> name of the country

    Returns a dict with information about the requested city
    """
    return db.Country.where('Name', '=',  name.capitalize()).get().serialize()


def get_country_all() -> dict:
    """
    API Controlled method to retrieve country details for
    all available countries

    Returns a dict with information about all available countries
    """
    return db.Country.all().serialize()


# Country info calls
def get_countryinfo(id: str):
    """
    API Controlled method to retrieve:
    Arguements:
    - id <str> ID code of a specific country

    Returns a dict with detailed information about the requested country
    """
    return db.CountryInfo.where('_id', '=', id.upper()).get().serialize()


# Country language calls
def get_countrylanguage(language: str):
    """
    API Controlled method to retrieve:
    Arguements:
    - language <str> language of the country to retrieve

    Returns a dict with requested data
    """
    return db.CountryLanguage.where('Language', '=', language.capitalize()) \
             .get() \
             .serialize()


def get_countrylanguage_all():
    """
    API Controlled method to retrieve:
    Arguements:
    -

    Returns a dict with requested data
    """
    return db.CountryLanguage.all().get().serialize()
