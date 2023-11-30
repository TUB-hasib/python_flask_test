from sqlalchemy import create_engine
from models import Base


# engine = create_engine("sqlite:///:memory", echo=True)
engine = create_engine("postgresql://postgres@localhost:5432", echo=True)


Base.metadata.create_all(bind=engine)
print(engine)
# Base.metadata.drop_all(bind=engine)

# print(engine)
