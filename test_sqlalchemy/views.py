import sqlalchemy
import sqlalchemy.orm
from django.conf import settings
from django.shortcuts import render

from .models import Base, Language


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return sqlalchemy.create_engine(settings.DATABASES["default"]["URL"])


def create_deals_table(engine):
    """"""
    Base.metadata.create_all(engine)


def db_session():
    engine = db_connect()
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    return session


DBSession = db_session()

if __name__ == "__main__":
    engine = db_connect()
    create_deals_table(engine)


def is_empty():
    return len(DBSession.query(Language).all()) <= 0


def populate():
    new_langs = [
        Language("Python", "py"),
        Language("Ruby", "rb"),
        Language("Common Lisp", "lisp"),
        Language("Objective-C", "m"),
    ]
    DBSession.add_all(new_langs)
    DBSession.commit()


def index(request):
    populate()
    if is_empty():
        populate()
    langs = DBSession.query(Language).all()
    return render(request, "test_sqlalchemy/index.html", {"langs": langs})
