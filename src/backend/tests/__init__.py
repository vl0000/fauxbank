from database.tables import meta
from tests.data import engine

meta.create_all(engine)