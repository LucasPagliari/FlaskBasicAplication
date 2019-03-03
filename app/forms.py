from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):

	title = StringField('title', validators=[DataRequired(),Length(min=8, max=50)])
	text = TextAreaField('text', validators=[DataRequired(),Length(max=200)])
	author = StringField('author', validators=[DataRequired(),Length(min=5, max=32)])
