from models.test import Test

from db.database import engine


def create_tables():
    Test.metadata.create_all(bind=engine)