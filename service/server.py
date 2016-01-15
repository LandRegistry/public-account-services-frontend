from flask import render_template, flash, redirect
from service import app
from service.forms import UserAccountForm
from werkzeug.wrappers import Request, Response

@app.route('/')
@app.route('/account-creation', methods=['GET', 'POST'])
def placeholder():
	form = UserAccountForm()
	return render_template('account-creation.html', form=form)

	if __name__ == '__main__':
		from werkzeug.serving import run_simple
		run_simple('localhost', 8011, application)
