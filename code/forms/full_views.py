import datetime
from flask import render_template, redirect, request, flash, url_for
from application import app, db
from models import User
from forms import RegistrationForm


@app.template_filter('datetimeformat')
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/manual', methods=('GET', 'POST'))
def register_manual():
    if request.method == 'POST':
        add_user_from_form(request.form['name'], request.form['email_address'], request.form['birthday'])
        return redirect(url_for('index'))
    return render_template('register_manual.html')


@app.route('/minimal', methods=('GET', 'POST'))
def register_minimal():
    form = RegistrationForm()
    if form.validate_on_submit():
        add_user_from_form(_form.name.data, _form.email_address.data, _form.birthday.data)
        return redirect(url_for('index'))
    return render_template('register_minimal.html', form=form)


@app.route('/with_placeholders', methods=('GET', 'POST'))
def register_with_placeholders():
    form = RegistrationForm()
    if form.validate_on_submit():
        add_user_from_form(_form.name.data, _form.email_address.data, _form.birthday.data)
        return redirect(url_for('index'))
    return render_template('register_with_placeholders.html', form=form)


@app.route('/with_errors', methods=('GET', 'POST'))
def register_with_errors():
    form = RegistrationForm()
    if form.validate_on_submit():
        add_user_from_form(_form.name.data, _form.email_address.data, _form.birthday.data)
        return redirect(url_for('index'))
    return render_template('register_with_errors.html', form=form)


@app.route('/full', methods=('GET', 'POST'))
def register_full():
    form = RegistrationForm()
    if form.validate_on_submit():
        add_user_from_form(_form.name.data, _form.email_address.data, _form.birthday.data)
        return redirect(url_for('index'))
    return render_template('register_full.html', form=form)


def add_user_from_form(_name, _email_address, _birthday=None):
    new_user = User()
    new_user.name = _name
    new_user.email_address = _email_address
    if _birthday:
        new_user.birthday = _birthday
    new_user.registered_at = datetime.datetime.today()
    db.session.add(new_user)
    db.session.commit()
    flash('User ' + _name + ' has been registered!')
