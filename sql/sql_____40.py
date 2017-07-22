# Import create_engine, MetaData
from sqlalchemy import MetaData, create_engine

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()
