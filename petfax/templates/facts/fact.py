from flask import ( Blueprint, render_template, request ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods=['POST'])
def index():
    print(request.form)
    return 'Thanks for submitting a fun fact!'
