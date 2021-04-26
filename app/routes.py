from flask import render_template, request
from app import app
from app.forms import DialectForm
from app.models_Cracow import transcribe_text_Cracow
from app.models_Warsaw import transcribe_text_Warsaw



@app.route('/', methods=["GET", "POST"])
def index():
    form = DialectForm()
    res = ''
    if request.method == "POST":
        dialect = form.data["dialect"]
        text = form.data["text"]
        if dialect in ["Wschodni", "Północne dialekty mieszane", "Centralny"]:
            data = {"trans_text": transcribe_text_Warsaw(text)}
            res = transcribe_text_Warsaw(text)
            return render_template("homepage_2.html", form=form, data=data, res=res)

        elif dialect in ["Wielkopolski", "Południowy"]:
            data = {"dialect": dialect, "text": transcribe_text_Cracow(text)}
            res = transcribe_text_Cracow(text)
            return render_template("homepage_2.html", form=form, data=data, res=res)

    return render_template("homepage_2.html", form=form, res=res)


