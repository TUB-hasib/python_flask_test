from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Shopper

# an Engine, which the Session will use for connection
# resources
# engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/")
engine = create_engine("postgresql://postgres@localhost:5432", echo=True)


shopper1= Shopper(id=1,name='milon',age='25',is_student=False)
shopper2= Shopper(id=2,name='mirfath',age='22',is_student=True)

    
# create session and add objects
with Session(engine) as session:
    session.add(shopper1)
    session.add(shopper2)
    # session.bulk_save_objects()  used to save lots of object together
    #shoppers = session.query(Shopper).all()  show all rows

    for shopper in session.query(Shopper):
        print(shopper)
    session.commit()
