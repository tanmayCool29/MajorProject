from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class allMeds(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(250))
    price = mapped_column(Float)
    Is_discontined = mapped_column(String(250))
    manufacturer_name = mapped_column(String(250))
    type = mapped_column(String(250))
    pack_size_label = mapped_column(String(250))
    short_composition1 = mapped_column(String(250))
    short_composition2 = mapped_column(String(250))