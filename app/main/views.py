from . import main

@main.route("/")
def index():
    return {"message": "YouTube Clone"}