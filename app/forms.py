from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, SubmitField


class DialectForm(FlaskForm):
    dialect = SelectField("dialect",
                          choices=["Centralny", "Południowy"])
    text = TextAreaField("text")


class ContactForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email")
    subject = StringField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
