from flask import (
    Flask,
    Blueprint,
    current_app,
    redirect,
    render_template,
    request,
    url_for
)

import os


import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


bp = Blueprint('portfolio', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')
    

@bp.route('/mail', methods=['POST', 'GET'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')

    return redirect(url_for('portfolio.index'))


def send_email(name, email, message):
    mi_email= 'WGSIGLO21SERVICIOS@GMAIL.COM'
    sg = SendGridAPIClient(os.environ.get('SENDGRID_KEY'))

    from_email = Email(mi_email)
    to_email = To(mi_email, substitutions={
        "-name-": name,
        "-email-": email,
        "-message-": message,
    })

    html_content = """
        <p> "Winston tienes un nuevo contacto desde el portfolio realizado con Python: </p>
        <p> Nombre: -name- </p>
        <p> Correo: -email- </p>
        <p> Mensaje: -message- </p>
    """
    mail = Mail(mi_email, to_email, 'Nuevo contacto desde la web', html_content=html_content)
    
    response = sg.client.mail.send.post(request_body=mail.get())



