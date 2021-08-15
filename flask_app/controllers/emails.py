from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route("/")
def index():
    
    return render_template("index.html")


@app.route("/email/success")
def all_emails():
    emails = Email.get_all()
    print(emails)
    return render_template("read.html", all_emails = emails)



@app.route('/validate_email', methods=["POST"])
def validate_email():

    if not Email.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things

    return redirect('/email/success')
