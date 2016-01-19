from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class UserAccountForm(Form):
	title = StringField('title', validators=[DataRequired()])
	forname = StringField('forname', validators=[DataRequired()])
	surname = StringField('surname', validators=[DataRequired()])
	business = StringField('business')
	postcode = StringField('postcode', validators=[DataRequired()])
	address1 = StringField('address1', validators=[DataRequired()])
	address2 = StringField('address2', validators=[DataRequired()])
	city = StringField('city', validators=[DataRequired()])
	county = StringField('county')
	country = StringField('country', validators=[DataRequired()])
	payment_address = BooleanField('payment_address', default=True)
	ppostcode = StringField('ppostcode', validators=[DataRequired()])
	paddress1 = StringField('paddress1', validators=[DataRequired()])
	paddress2 = StringField('paddress2', validators=[DataRequired()])
	pcity = StringField('pcity', validators=[DataRequired()])
	pcountry = StringField('pcity', validators=[DataRequired()])
	email1 = StringField('email1', validators=[DataRequired()])
	email2 = StringField('email2', validators=[DataRequired()])
	telephone = StringField('telephone')
	preference_email = BooleanField('preference_email', default=True)
	preference_phone = BooleanField('preference_phone', default=True)
	preference_post = BooleanField('preference_post', default=True)
	login_username = StringField('login_username', validators=[DataRequired()])
	login_password1 = PasswordField('login_password1', validators=[DataRequired()])
	login_password2 = PasswordField('login_password2', validators=[DataRequired()])
