from app import app, db
from app.forms import PostForm
from app.models import *
from flask import render_template, request, redirect

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/blog')
def blog():
	# all the posts will be here
	content = Posts.query.all()
	content.reverse()
	return render_template('blog.html', content=content)

@app.route('/post', methods=('GET', 'POST'))
def post():
	form = PostForm()
	if form.validate_on_submit():
		post = Posts(request.form['title'], request.form['author'],
					request.form['text'])
		db.session.add(post)
		db.session.commit()
		return redirect('/blog')
	return render_template('post.html', form=form)



@app.route('/contact')
def contact():
	return render_template('contact.html')
'''

		# '''