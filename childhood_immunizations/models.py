from .app import db


class Measles(db.Model):
    __tablename__ = 'Measles Data'

    id = db.Column(db.Integer, primary_key=True)
    States = db.Column(db.String(15))
    Counts = db.Column(db.Integer)

    def __repr__(self):
        return '<Immunization %r>' % (self.States)

class Vaccines(db.Model):
    __tablename__ = 'Vaccines'

    id = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String(15))
    'Measles cases (2019)' = db.Column(db.Integer)
    'Mumps cases (2019)' = db.Column(db.Integer)
    'Pertussis cases (2018)' = db.Column(db.Integer)
    'Religious Exemption' = db.Column(db.String(10))
    'Philosophical Exemption' = db.Column(db.String(10))
