from typing import Optional
from pydantic import Field
from sqlmodel import create_engine, Session, SQLModel, PrimaryKeyConstraint, select, insert
import sqlalchemy as sm
import config

from faker import Faker
import random



class MemberInfo(SQLModel, table=True):
    __tablename__ = 'MemberInfo'
    __table_args__ = (PrimaryKeyConstraint('Id'),)
    Id: Optional[int] = Field(default=None, primary_key=True)
    MemberId: str
    MemberName: str
    MemberAge: int
    IsActive: bool


class MemberOrderInfo(SQLModel, table=True):
    __tablename__ = 'MemberOrderInfo'
    __table_args__ = (PrimaryKeyConstraint('OrderId'),)
    OrderId: Optional[int] = Field(default=None, primary_key=True)
    MemberId: str
    ProductName: int




connection_url = sm.URL.create("mysql"
                               , username=config.DB_USERNAME
                               , password=config.DB_PASSWORD
                               , host=config.DB_HOST
                               , port=config.DB_PORT
                               , database=config.DB_SCHEMA
                               )

engine = create_engine(connection_url, echo = True)
# SQLModel.metadata.create_all(engine)
fake = Faker()

members = []

for i in range(1,20):
    member = {
        "MemberId": f"M{i:03}",
        "MemberName": fake.name(),
        "MemberAge": random.randint(18, 80),
        "IsActive": fake.boolean()
    }
    members.append(member)

print(members)

member_info_obj_list= []

with Session(engine) as session:
    for row in members:
        member_info_obj_list.append(MemberInfo(**row))
    session.bulk_save_objects(member_info_obj_list)
    session.commit()




