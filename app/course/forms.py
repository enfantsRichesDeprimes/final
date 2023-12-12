from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# 课程表单
class CourseForm(FlaskForm):
    name = StringField('课程名称', validators=[DataRequired("课程名称不能为空")])
    credit = IntegerField('学分', validators=[DataRequired("学分不能为空"), NumberRange(min=0)])
    class_hour = IntegerField('学时', validators=[DataRequired("课时不能为空"), NumberRange(min=0)])
    teacher = StringField('授课教师', validators=[DataRequired("授课教师不能为空")])
    dept = StringField('开课院系', validators=[DataRequired("开课院系不能为空")])
    major = StringField('开课专业', validators=[DataRequired("开课专业不能为空")])
    grade = StringField('开课年级', validators=[DataRequired("开课年级不能为空")])
    semester = StringField('开课学期', validators=[DataRequired("开课学期不能为空")])
    time = StringField('上课时间', validators=[DataRequired("上课时间不能为空")])
    place = StringField('上课地点', validators=[DataRequired("上课地点不能为空")])
    number = IntegerField('选课人数', validators=[DataRequired("选课人数不能为空"), NumberRange(min=0)])
    max_number = IntegerField('最大选课人数', validators=[DataRequired("最大选课人数不能为空"), NumberRange(min=0)])


# 根据教师名字查看课程信息表单
class SearchByTeacherNoForm(FlaskForm):
    no = StringField('教师名字', validators=[DataRequired("教师名字不能为空")])

# 根据课程编号查看课程信息表单
class SearchByCourseNoForm(FlaskForm):
    no = StringField('课程编号', validators=[DataRequired("课程编号不能为空")])


# 删除课程表单
class DeleteCourseForm(FlaskForm):
    no = StringField('课程编号', validators=[DataRequired("课程编号不能为空")])


# 更新课程表单
class UpdateCourseForm(CourseForm):
    no = StringField('课程编号', validators=[DataRequired("课程编号不能为空")])
    name = StringField('课程名称', validators=[DataRequired("课程名称不能为空")])
    credit = IntegerField('学分', validators=[DataRequired("学分不能为空"), NumberRange(min=0)])
    class_hour = IntegerField('学时', validators=[DataRequired("课时不能为空"), NumberRange(min=0)])
    teacher = StringField('授课教师', validators=[DataRequired("授课教师不能为空")])
    dept = StringField('开课院系', validators=[DataRequired("开课院系不能为空")])
    major = StringField('开课专业', validators=[DataRequired("开课专业不能为空")])
    grade = StringField('开课年级', validators=[DataRequired("开课年级不能为空")])
    semester = StringField('开课学期', validators=[DataRequired("开课学期不能为空")])
    time = StringField('上课时间', validators=[DataRequired("上课时间不能为空")])
    place = StringField('上课地点', validators=[DataRequired("上课地点不能为空")])
    number = IntegerField('选课人数', validators=[DataRequired("选课人数不能为空"), NumberRange(min=0)])
    max_number = IntegerField('最大选课人数', validators=[DataRequired("最大选课人数不能为空"), NumberRange(min=0)])
