# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT TITLE, NAME FROM ALBUM INNER JOIN ARTIST ON ALBUM.ARTISTID = ARTIST.ARTISTID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
