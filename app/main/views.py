from flask import render_template
from . import main
from .forms import NameForm

@main.route("/")
def index():
    return {"message": "YouTube Clone"}

@main.route("/form")
def form():
    form = NameForm()
    return render_template("form.html", form=form)