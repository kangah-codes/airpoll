from app import db, flask_bcrypt
import uuid

	
class Data(db.Model):
	__tablename__ = "data"

	id = db.Column(db.String(), primary_key=True)
	city = db.Column(db.String())
	state = db.Column(db.String())
	country = db.Column(db.String())
	lat = db.Column(db.Float())
	lon = db.Column(db.Float())
	date = db.Column(db.DateTime())

	def __init__(self, city, state, country, lat, lon, date):
		self.id = uuid.uuid1()
		self.city = city
		self.state = state
		self.country = country
		self.lat = lat
		self.lon = lon
		self.date = date