from flask import render_template, flash, redirect
from service import app
from service.forms import UserAccountForm

@app.route('/')
@app.route('/account-creation', methods=['GET', 'POST'])
def placeholder():
	form = UserAccountForm()
	return render_template('account-creation.html', form=form)
