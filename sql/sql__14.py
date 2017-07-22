# Build a query to count the distinct states values: stmt
stmt = select([func.distinct(census.columns.state)])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)
