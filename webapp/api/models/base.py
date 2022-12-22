from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

Base = declarative_base()


class BaseMixin(object):
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
