from db import Base, engine
import Model
from Model  import Passenger

Base.metadata.drop_all(bind=engine)

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created.")

