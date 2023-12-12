from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Length


class LoginForm(FlaskForm):
    """登录表单验证"""
    no = StringField("no", validators=[DataRequired("学号\工号不能为空"), Length(max=255)])
    password = StringField("password", validators=[DataRequired("密码不能为空"), Length(max=255)])

    def validate_name(self, field):
        """检查用户名是否存在"""
        from .models import User
        user = User.query.filter_by(no=field.data).first()
        if not user:
            raise ValidationError("学号\工号不存在")

    def validate_password(self, field):
        """检查密码是否正确"""
        from .models import User
        user = User.query.filter_by(no=self.no.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError("密码错误")




class RegisterForm(FlaskForm):
    no = StringField("学号/工号", validators=[DataRequired("学号/工号不能为空"), Length(max=255)])
    name = StringField("用户名", validators=[DataRequired("用户名不能为空"), Length(max=255)])
    password = StringField("密码", validators=[DataRequired("密码不能为空"), Length(max=255)])
    sex = StringField("性别", validators=[DataRequired("性别不能为空"), Length(max=255)])
    grade = StringField("入学（职）年份", validators=[DataRequired("入学（职）年份不能为空"), Length(max=255)])
    dept = StringField("院系", validators=[DataRequired("院系不能为空"), Length(max=255)])
    major = StringField("专业", validators=[Length(max=255)])
    title = StringField("职称", validators=[Length(max=255)])

    def validate_no(self, field):
        """检查学号/工号是否存在"""
        from .models import User
        user = User.query.filter_by(no=field.data).first()
        if user:
            raise ValidationError("学号/工号已存在")


class AddUserForm(FlaskForm):
    """添加用户表单验证"""
    no = StringField("学号/工号", validators=[DataRequired("学号/工号不能为空"), Length(max=255)])
    name = StringField("用户名", validators=[DataRequired("用户名不能为空"), Length(max=255)])
    sex = StringField("性别", validators=[DataRequired("性别不能为空"), Length(max=255)])
    grade = StringField("入学（职）年份", validators=[DataRequired("入学（职）年份不能为空"), Length(max=255)])
    dept = StringField("院系", validators=[DataRequired("院系不能为空"), Length(max=255)])
    major = StringField("专业", validators=[Length(max=255)])
    title = StringField("职称", validators=[Length(max=255)])
    password = StringField("密码", validators=[DataRequired("密码不能为空"), Length(max=255)])

    def validate_no(self, field):
        """检查学号/工号是否存在"""
        from .models import User
        user = User.query.filter_by(no=field.data).first()
        if user:
            raise ValidationError("学号/工号已存在")

class DeleteUserForm(FlaskForm):
    """删除用户表单验证"""
    no = StringField("学号/工号", validators=[DataRequired("学号/工号不能为空"), Length(max=255)])

    def validate_no(self, field):
        """检查学号/工号是否存在"""
        from .models import User
        user = User.query.filter_by(no=field.data).first()
        if not user:
            raise ValidationError("学号/工号不存在")

class EditUserForm(FlaskForm):
    """编辑用户表单验证"""
    no = StringField("学号/工号", validators=[DataRequired("学号\工号不能为空"),Length(max=255)])
    name = StringField("用户名", validators=[Length(max=255)])
    password = StringField("密码", validators=[Length(max=255)])
    sex = StringField("性别", validators=[Length(max=255)])
    grade = StringField("入学（职）年份", validators=[Length(max=255)])
    dept = StringField("院系", validators=[Length(max=255)])
    major = StringField("专业", validators=[Length(max=255)])
    title = StringField("职称", validators=[Length(max=255)])

    def validate_no(self, field):
        """检查学号/工号是否存在"""
        from .models import User
        user = User.query.filter_by(no=field.data).first()
        if not user:
            raise ValidationError("学号/工号不存在")