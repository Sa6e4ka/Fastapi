from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Column, JSON, Table, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column 
import datetime

my_metadata = MetaData()

class Base(DeclarativeBase):
    metadata= my_metadata

class UsersPermissions(Base):
    metadata= my_metadata
    __tablename__ = "UsersPermissions"

    id = Column(
        Integer, primary_key= True, autoincrement=True
    )  

    name = Column(
        String(length=200), nullable=False, unique=True
    )

    pemissions = Column(
        JSON, nullable=False
    )


class Users(Base):
    metadata=my_metadata
    __tablename__ = "users"
    
    id = Column(
        Integer, primary_key= True, autoincrement=True
    )

    name = Column(
        String(length=200), nullable=False, unique=True
    )

    email= Column(
        String(length=320), unique=True, index=True, nullable=False
    )

    register_time = Column(
        TIMESTAMP, default=datetime.datetime.now(datetime.UTC)
    )

    hashed_password = Column(
        String(length=1024), nullable=False
    )
    is_active =  Column(Boolean, default=True, nullable=False)
    is_superuser = Column(
        Boolean, default=False, nullable=False
    )
    is_verified = Column(
        Boolean, default=False, nullable=False
    )

    # permissions = Column(
    #     String, ForeignKey("UsersPermissions.id")
    # )



# UsersPermissions = Table(
#     "UsersPermissions",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("permissions", JSON)

# )
    
# users = Table(
#     "users",
#     metadata, 
#     Column("id", Integer, primary_key=True),
#     Column("hashed_password", String(length=1024), nullable=False),
#     Column("name", String, nullable=False),
#     Column("email", String, nullable=False),
#     Column("register_time", TIMESTAMP, default=datetime.datetime.now(datetime.UTC)),
#     Column("permissions", Integer, ForeignKey(UsersPermissions.c.id)),
#     Column("is_active",Boolean, default=True, nullable=False),

#     Column("is_superuser",
#         Boolean, default=False, nullable=False
#     ),
#     Column("is_verified",
#         Boolean, default=False, nullable=False
#     )
# )   

    
    



