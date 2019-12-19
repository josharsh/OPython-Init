# Python core imports
import os

# Third-party imports
from orator import DatabaseManager
from orator import Model

# Local imports (relative)
# from database.models import posts
# from database.models import drafts
# from database.models import users
# from database.models import notes

# Local imports (relative)
from Examples.sample_oo_dashboard.database.models import posts
from Examples.sample_oo_dashboard.database.models import drafts
from Examples.sample_oo_dashboard.database.models import users
from Examples.sample_oo_dashboard.database.models import notes


class Database:
    """
    Provides database methods
    """

    db = None
    Posts = None
    Drafts = None
    Users = None
    Notes = None

    config: dict

    # Config
    config = {}

    def __init__(self):
        """
        Initializes a database instance and binds the models to it.

        Arguement(s)
        - self

        """

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

        # Bind Models to local variables
        self.Posts = posts
        self.Drafts = drafts
        self.Users = users
        self.Notes = notes

        # Create database from config
        self.db = DatabaseManager(self.config)

        # Auto-resolve connection
        Model.set_connection_resolver(self.db)


# Create public instance
db = Database()
