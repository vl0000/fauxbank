import argparse
from database.tables import meta, engine

parser = argparse.ArgumentParser(description="Commands that will help you manage the db!")
parser.add_argument("-tables", type=str, help="Creates or drops all tables")

args = parser.parse_args()

match args.tables:
    case "drop":
        meta.drop_all(engine)
    case "create":
        meta.create_all(engine)