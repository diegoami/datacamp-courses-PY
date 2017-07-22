
from sqlalchemy import *
# Reflect census table from the engine: census


# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://'+
'student:datacamp'+
'@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com'+
':5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())


connection = engine.connect()
metadata = MetaData()
census = Table('census',metadata  , autoload=True, autoload_with=engine)
stmt = select([census])

# Add a where clause to filter the results to only those for New York
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2008
for result in results:
    print(result.age, result.sex, result.pop2008)
