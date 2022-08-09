#!/usr/bin/python3
"""New engine DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


class DBStorage:
    """class to store in MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method"""
        from models.base_model import Base
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        url = f'mysql+mysqldb://{user}:{passwd}@{host}/{db}'
        self.__engine = create_engine(url, pool_pre_ping=True)
        if (env is not None and env == 'test'):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        from models.state import State
        from models.city import City
        from models.base_model import Base
        tables = {
#                    'user': User,
#                    'place': Place,
                    'states': State,
                    'cities': City,
#                    'amenity': Amenity,
#                    'Review': Review
                  }
        dict_entries = {}
        if cls is None:
            for base_class in tables.values():
                for row in self.__session.query(base_class).all():
                    dict_entries[f'{base_class.__name__}.{row.id}'] = row
        else:
            for row in self.__session.query(cls):
                dict_entries[f'{cls.__name__}.{row.id}'] = row
        return dict_entries

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
