from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Money
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        RoneHundred = int(request.form.get('oneHundred'))
        Rfifty = int(request.form.get('fifty'))
        Rtwenty = int(request.form.get('twenty'))
        Rten = int(request.form.get('ten'))
        Rtotal = (RoneHundred*100)+(Rfifty*50)+(Rtwenty*20)+(Rten*10)
        moneyRecord = Money(oneHundred=RoneHundred, fifty=Rfifty, twenty=Rtwenty, ten=Rten, total=Rtotal, user_id=current_user.id)
        db.session.add(moneyRecord)
        db.session.commit()

    return render_template("home.html", user=current_user)


    return jsonify({})