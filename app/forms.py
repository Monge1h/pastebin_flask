from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PasteBinForm(FlaskForm):
    paste = TextAreaField(validators=[DataRequired()])
    submit = SubmitField(label='Create New Paste')
