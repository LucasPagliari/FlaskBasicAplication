from app import db


class Posts(db.Model):
	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(60), nullable=False)
	author = db.Column(db.String(40), nullable=False)
	text = db.Column(db.String(200), nullable=False)

	def __init__(self, title, author, text):
		self.title = title
		self.author = author
		self.text = text
