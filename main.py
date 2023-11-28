from sqlalchemy import create_engine
from models import Base


# engine = create_engine("sqlite:///:memory", echo=True)
engine = create_engine("sqlite:///sample.db", echo=True)



Base.metadata.create_all(bind=engine)
print(engine)
