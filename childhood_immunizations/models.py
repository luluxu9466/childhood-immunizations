from app import db

class Measles(db.Model):
    __tablename__ = 'Measles Data'

    id = db.Column(db.Integer, primary_key=True)
    States = db.Column(db.String(15))
    Counts = db.Column(db.Integer)

    def __repr__(self):
        return '<State %r>' % (self.States)
    
    def serialize(self):
        return {
            'id': self.id
            'States': self.States, 
            'Counts': self.Counts,
        }

class Vaccines(db.Model):
    __tablename__ = 'Vaccines'

    id = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String(15))
    'Measles cases (2019)' = db.Column(db.Integer)
    'Mumps cases (2019)' = db.Column(db.Integer)
    'Pertussis cases (2018)' = db.Column(db.Integer)
    'Religious Exemption' = db.Column(db.String(10))
    'Philosophical Exemption' = db.Column(db.String(10))

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())

    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'published':self.published
        }