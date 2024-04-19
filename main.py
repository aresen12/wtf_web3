from flask import Flask, render_template, redirect, request, make_response, session
from data import db_session, news_api
from data.users import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from data.jobs import Jobs

app = Flask('213.87.139.94')

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count:
        res = make_response(f'Вы посетили страницу {visit_count + 1} раз')
        res.set_cookie('visit_count', str(visit_count + 1),
                       max_age=0)
    else:
        res = make_response(f'Вы посетили страницу первый раз за последний год')
        res.set_cookie('visit_count', '1', max_age=0)
    return res


@app.route('/session_test')
def session_test():
    visit_count = session.get('visit_count', 0)
    session['visit_count'] = visit_count + 1
    return make_response(f'Вы посетили эту страницу {visit_count + 1} раз')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Домашняя страница')


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof)


@app.route("/list_prof/<sp>")
def list_prof(sp):
    file = open("conf.txt", encoding="utf-8")
    data = file.readlines()
    file.close()

    return render_template("list_prof.html", sp=sp, data=data)


def main():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    app.run()


if __name__ == '__main__':
    main()
