from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField



class DialectForm(FlaskForm):
    dialect = SelectField("dialect",
                          choices=["Centralny", "Południowy"])
    text = TextAreaField("text")





