from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Replace 'freebies.db' with the actual path to your SQLite database file
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Seeding logic
# Create instances of Company
company1 = Company(name='Company1', founding_year=2000)
company2 = Company(name='Company2', founding_year=2010)

# Create instances of Dev
dev1 = Dev(name='Dev1')
dev2 = Dev(name='Dev2')

# Create instances of Freebie
freebie1 = Freebie(item_name='Item1', value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name='Item2', value=15, dev=dev2, company=company2)

# Add instances to the session
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])

# Commit the changes to the database
session.commit()

# Close the session
session.close()
