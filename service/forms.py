from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class UserAccountForm(Form):
	title = StringField('title', validators=[DataRequired()])
	forname = StringField('forname', validators=[DataRequired()])
	surname = StringField('surname', validators=[DataRequired()])
	business = StringField('business')
	postcode = StringField('postcode', validators=[DataRequired()])
	address1 = StringField('address1', validators=[DataRequired()])
	address2 = StringField('address2')
	address3 = StringField('address3')
	address4 = StringField('address4')
	city = StringField('city', validators=[DataRequired()])
	county = StringField('county')
	country = StringField('country', validators=[DataRequired()])
	payment_address = BooleanField('payment_address', default=True)
	email1 = StringField('email1', validators=[DataRequired()])
	email2 = StringField('email2', validators=[DataRequired()])
	telephone = StringField('telephone')
	preference_email = BooleanField('preference_email', default=True)
	preference_phone = BooleanField('preference_phone', default=True)
	preference_post = BooleanField('preference_post', default=True)
	login_username = StringField('login_username', validators=[DataRequired()])
	login_password1 = StringField('login_password1', validators=[DataRequired()])
	login_password2 = StringField('login_password2', validators=[DataRequired()])
