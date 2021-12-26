import smtplib
import math
import random
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_cors import CORS

PORT = int(os.environ.get('PORT', 33507))
HOST = 'https://otp--flask-api.herokuapp.com'
# HOST = '127.0.0.1'
# PORT = 8000
# --------------------------------------------------------------------------------------------------------------
sender_email = 'qliodev@gmail.com'
password = 'famousguy'
# --------------------------------------------------------------------------------------------------------------
# function to generate OTP


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

# send mail


def mail(email, OTP):
    global sender_email, password
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, password)
    s.send
    s.sendmail(sender_email, email,str(OTP) )
    s.quit()

def reqMail(email,sender):
    global sender_email, password
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, password)
    em = sender
    st = "Hi. I would like us to work together. Ping me at "+em
    print(st)
    s.sendmail(sender_email, email, st )
    s.quit()


app = Flask(__name__)
CORS(app)


@app.route('/OTP', methods=["GET", "POST"])
def home():
    email_ = request.args.get('id')
    OTP_ = generateOTP()
    mail(email_, OTP_)
    return jsonify(OTP=OTP_, email=email_)

@app.route('/request', methods=['GET', 'POST'])
def send():
    res = request.args.get('res')
    sender = request.args.get('sender')

    reqMail(res, sender)
    return jsonify(res = res, sender = sender)

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
