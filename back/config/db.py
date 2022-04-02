from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql+psycopg2://postgres:Password@localhost:5432/stocker")

meta = MetaData()

conn = engine.connect() 