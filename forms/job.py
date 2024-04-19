from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerRangeField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader = StringField('team_leader', validators=[DataRequired()])
    job = StringField('job_name', validators=[DataRequired()])
    work_size = IntegerField("work_size", validators=[DataRequired()])
    collaborators = StringField('collaborators', validators=[DataRequired()])
    start_date = DateField("start_date")
    end_date = DateField("end_date", validators=[DataRequired()])
    is_finished = IntegerRangeField("is_finished", validators=[DataRequired()])
