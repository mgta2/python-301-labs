# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import sqlalchemy
import os
from pprint import pprint

password = os.environ["DATABASEPASSWORD"]
my_url = f"mysql+pymysql://root:{password}@localhost/sakila"

# If wrong password we get a RuntimeError.
# If no database of the given name exists we get a SQLAlchemy 'OperationalError'.

try:

    engine = sqlalchemy.create_engine(my_url)
    connection = engine.connect()

except Exception as e:
    
    print(type(e))
    print(f"Could not establish connection to database: {e}")

else:

    metadata = sqlalchemy.MetaData()
    film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
    query = sqlalchemy.select([film])
    
    result = connection.execute(query).fetchall()
    
    pprint(result)