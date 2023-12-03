from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import pydantic

class Base(DeclarativeBase):
    pass



class Shopper(Base):
    __tablename__ = 'shoppers'
    id:Mapped[str] = mapped_column(String, primary_key=True)
    name:Mapped[str] = mapped_column(String(20), nullable=False)
    age:Mapped[int] = mapped_column(Integer)
    is_student:Mapped[bool] = mapped_column(Boolean)

    @pydantic.validator("is_student")
    @classmethod
    def is_student_check(cls, value:bool):
        print("Hellllllllllllllllllllllllllllllllllllo")
        if value:
            raise ValueError 
        raise ValueError
        


class Buy(Base):
    __tablename__ = 'buys'
    buy_id:Mapped[int] = mapped_column(Integer , primary_key=True, nullable=False)
    shppoer_id:Mapped[int] = mapped_column(nullable=False)
    item_id:Mapped[int] = mapped_column(nullable=False)
    

class Item(Base):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    price: Mapped[int] = mapped_column(Integer,nullable=False)
    type: Mapped[str] = mapped_column(String(10))
    company: Mapped[str] = mapped_column(String(10), nullable=False)


class Test(Base):
    __tablename__ = 'testconstraint'
    id: Mapped[int] = mapped_column(Integer, autoincrement=True)
    type: Mapped[str] = mapped_column(String(10), nullable=True)
    company: Mapped[str] = mapped_column(String(10), nullable=False)
    name:Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    age:Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_student:Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    
    __table_args__ = (
        # ForeignKeyConstraint(["id"], ["remote_table.id"]),
        UniqueConstraint("type","company", name='uniquetypecompany'),
        PrimaryKeyConstraint("id", name="testconstraint_pk"),
        UniqueConstraint("type", name='uniquetype'),
    )



# class User(Base):
#     __tablename__ = "user_account"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship(
#         back_populates="user", cascade="all, delete-orphan"
#     )
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"