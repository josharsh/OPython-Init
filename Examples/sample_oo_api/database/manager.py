# Python core imports
import os

# Third-party imports
from orator import DatabaseManager
from orator import Model

# Importing local models
from models.city import city
from models.country import country
from models.countryinfo import countryinfo
from models.countrylanguage import countrylanguage


class Database:
    """
    Contains database methods
    """

    db = None
    config = {}

    City = None
    Country = None
    CountryInfo = None
    CountryLanguage = None

    # Config
    config = {}

    def __init__(self):
        """
        Initializes a database instance and binds the models to it.

        Arguement(s)
        - self

        """
        # Bind Models to local variables
        self.City = city
        self.Country = country
        self.CountryInfo = countryinfo
        self.CountryLanguage = countrylanguage

        # Set config
        self.config = {
            'mysql': {
                'driver': 'mysql',
                'host': os.getenv('DB_HOST'),
                'database': os.getenv('DB_NAME'),
                'user': os.getenv('DB_USER'),
                'password': os.getenv('DB_PASSWORD'),
                'prefix': ''
            }
        }

        # Create database from config
        self.db = DatabaseManager(self.config)

        # Auto-resolve connection
        Model.set_connection_resolver(self.db)


# Create public instance
db = Database()
