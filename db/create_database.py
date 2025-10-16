
from models.test import Test
from models.user import User

from db.database import engine


def create_tables():
    Test.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)