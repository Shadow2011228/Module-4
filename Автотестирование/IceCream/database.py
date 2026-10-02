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

Base.metadata.create_all(engine)

# new_taste = Tastes(name="Клубника", weight=1.5, id=1)
# s.merge(new_taste)
# new_taste2 = Tastes(name="Банан", weight=3, id=2)
# s.merge(new_taste2)
# new_taste3 = Tastes(name="Малина", weight=1, id=3)
# s.merge(new_taste3)
# new_taste4 = Tastes(name="Шоколад", weight=5, id=4)
# s.merge(new_taste4)
# new_taste5 = Tastes(name="Фисташка", weight=0.5, id=5)
# s.merge(new_taste5)
#
#
# s.commit()


if __name__ == '__main__':
    ice = s.get(IceCream, 1)
    print(
        ice.__dict__
    )
    print(ice.taste)
    print(ice.rem_weight)

