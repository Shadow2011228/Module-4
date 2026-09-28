from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint, REAL
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property


database_file = "database.db"
engine = create_engine(f"sqlite:///{database_file}")
Session = sessionmaker(engine)
s = Session()
Base = declarative_base()

class Tastes(Base):
    __tablename__ = "Tastes"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))
    weight = Column(REAL)


class IceCream(Base):
    __tablename__ = 'IceCream'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250))
    cone = Column(String(10))
    taste_id = Column(Integer, nullable=False)
    @hybrid_property
    def taste(self):
        return s.query(Tastes).filter_by(id=self.taste_id).first().name
    @hybrid_property
    def rem_weight(self):
        return s.query(Tastes).filter_by(id=self.taste_id).first().weight
        __table_args__ = (
            CheckConstraint(cone.in_(['Большой', 'Средний', 'Маленький']),
                            name='check_cone_type'),
        )

