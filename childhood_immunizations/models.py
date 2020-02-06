from .app import db

class Measles(db.Model):
    __tablename__ = 'Measles Data'

    id = db.Column(db.Integer, primary_key=True)
    States = db.Column(db.String(15))
    Counts = db.Column(db.Integer)

    def __repr__(self):
        return '<State %r>' % (self.States)
    
    # def serialize(self):
    #     return {
    #         'id': self.id
    #         'States': self.States, 
    #         'Counts': self.Counts,
    #     }

class Vaccines(db.Model):
    __tablename__ = 'Vaccines'

    id = db.Column(db.Integer, primary_key=True)
    States = db.Column(db.String(15))
    Measles_cases = db.Column(db.Integer)
    Mumps_cases = db.Column(db.Integer)
    Pertussis_cases = db.Column(db.Integer)
    Religious_Exemption = db.Column(db.String(10))
    Philosophical_Exemption = db.Column(db.String(10))