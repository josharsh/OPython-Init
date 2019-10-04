# Import model base
from orator import Model


class posts(Model):
    __table__ = 'posts'
    pass


class drafts(Model):
    __table__ = 'drafts'


class users(Model):
    __table__ = 'users'
    pass


class notes(Model):
    __table__ = 'notes'
    pass
