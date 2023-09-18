from . import auth


@auth.route("/login")
def login():
    return "{'message': 'Login Page'}"

@auth.route("/signup")
def signup():
    return "{'message: 'Sign Up Page'}"