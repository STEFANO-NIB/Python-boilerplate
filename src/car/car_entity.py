from src.database.baseModel import BaseModel, db


class Car(db.model):
    __tablename__ = 'cars'
    __table_arg__ = ({
        'schema': 'client',
        'autoload': True,
        'autoload_with': db.engine,
        'extend_existing': True}
    )

    cars = db.relationship(

    )

    def __init__(self):
        pass
