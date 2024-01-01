from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# 选课关系表单
class ScForm(FlaskForm):
    student_no = StringField('学生学号', validators=[DataRequired("学生学号不能为空")])
    course_no = StringField('课程编号', validators=[DataRequired("课程编号不能为空")])
    grade = IntegerField('成绩', validators=[DataRequired("成绩不能为空"), NumberRange(min=0, max=100)])

class SearchByStudentNoForm(FlaskForm):
    no = StringField('学生学号', validators=[DataRequired("学生学号不能为空")])

class SearchByCourseNoForm(FlaskForm):
    no = StringField('课程编号', validators=[DataRequired("课程编号不能为空")])

class DeleteScForm(FlaskForm):
    student_no = StringField('学生学号', validators=[DataRequired("学生学号不能为空")])
    course_no = StringField('课程编号', validators=[DataRequired("课程编号不能为空")])

class UpdateScForm(ScForm):
    student_no = StringField('学生学号', validators=[DataRequired("学生学号不能为空")])
    course_no = StringField('课程编号', validators=[DataRequired("课程编号不能为空")])
    grade = IntegerField('成绩', validators=[DataRequired("成绩不能为空"), NumberRange(min=0, max=100)])