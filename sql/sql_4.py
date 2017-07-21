# Build select statement for census table: stmt
stmt = 'SELECT * FROM CENSUS'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print Results
print(results)