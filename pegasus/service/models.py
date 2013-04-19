from datetime import datetime

from pegasus.service import db

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# IMPORTANT
# This is the current version of the schema. It should be incremented 
# each time a change is made to the schema and a migration script 
# should be created to go from the old version to the new version.
version = 1
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Schema(db.Model):
    __tablename__ = 'schema'
    __table_args__ = {'mysql_engine':'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    def __init__(self, version):
        self.version = version
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Schema %d %s>' % (self.version, self.timestamp)

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_engine':'InnoDB'}
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    hashpass = db.Column(db.String(32))
    email = db.Column(db.String(120), unique=True)
    
    def __repr__(self):
        return '<User %r>' % (self.username)
