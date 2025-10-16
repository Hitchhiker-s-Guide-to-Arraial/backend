
from models.test import Test
from models.user import User
from models.travel import Travel

from db.database import engine


def create_tables():
    Test.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)
    Travel.metadata.create_all(bind=engine)