# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')


# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM EMPLOYEE ORDER BY BIRTHDATE')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    # Set the DataFrame's column names


# Print head of DataFrame
print(df.head())
