from flask import jsonify, session, abort
from app.student import student_bp
from app.exts import db
import os

from ..sc.models import Sc

current_path = os.path.dirname(__file__)
ttf_file_path = os.path.join(current_path, "static", "ttf", "ziti.ttf")
from .models import User  # 假设 models.py 中有 User 类定义
from .forms import LoginForm, RegisterForm, AddUserForm, DeleteUserForm, EditUserForm


# 假设 app 是你创建的 Flask 实例
@student_bp.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 在这里处理登录逻辑，例如验证用户输入的用户名和密码是否正确
        # 如果验证成功，可以设置用户登录状态，并重定向到其他页面
        user = User.query.filter_by(no=form.data['no']).first()
        if user and user.check_password(form.data['password']):
            session['user_id'] = user.id  # 设置用户登录状态
            response_data = {"msg": "登录成功", "user_info": {
                "no": user.no,
                "name": user.name,
                "title": user.title,
                "dept": user.dept,
                "major": user.major,
                "grade": user.grade,
                "sex": user.sex
            }}
        else:
            response_data = {"msg": "用户名或密码错误"}

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "登录失败", "errors": form.errors}

    return jsonify(response_data)


@student_bp.route('/add', methods=['POST'])
def add_user():
    form = AddUserForm()
    if form.validate_on_submit():
        # 在这里处理添加用户逻辑，例如将表单提交的数据保存到数据库中
        validate_data = form.data
        user = User(**validate_data)
        db.session.add(user)
        db.session.commit()
        session.clear()

        response_data = {"msg": "添加成功"}


    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "添加失败"}
        response_data.update(form.errors)

    return jsonify(response_data)


@student_bp.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    form = DeleteUserForm(csrf_enabled=False)
    if form.validate_on_submit():
        # 在这里处理删除课程逻辑，例如将表单提交的数据保存到数据库中
        id = user_id
        user = User.query.filter_by(id=id).first()
        if user is None:
            abort(404, "删除失败，用户不存在")
        else:
            student_id = user.no
            sc = Sc.query.filter_by(student_id=student_id).all()
            if sc:
                for s in sc:
                    db.session.delete(s)
                db.session.commit()
            db.session.delete(user)
            db.session.commit()
            session.clear()
            response_data = {"msg": "删除成功"}
    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "删除失败"}
        response_data.update(form.errors)
    return jsonify(response_data)


@student_bp.route('/update', methods=['POST'])
def update_user():
    form = EditUserForm()
    if form.validate_on_submit():
        no = form.no.data
        user = User.query.filter_by(no=no).first()
        if user:
            form.populate_obj(user)
            db.session.commit()
            response_data = {"msg": "用户信息更新成功"}
            response_data["no"] = user.no
            response_data["name"] = user.name
            response_data["title"] = user.title
            response_data["dept"] = user.dept
            response_data["major"] = user.major
            response_data["grade"] = user.grade
        else:
            response_data = {"msg": "用户不存在"}
    else:
        response_data = {"msg": "表单验证失败"}
        response_data.update(form.errors)

    return jsonify(response_data)


@student_bp.route('/search_all', methods=['POST'])
def search_all():
    # 在这里处理查看所有课程信息逻辑，例如将表单提交的数据保存到数据库中
    users = User.query.all()
    if users is None:
        return jsonify({"msg": "查看失败，用户不存在"})
    else:
        response_data = {"msg": "查看成功"}
        response_data["users"] = []
        for user in users:
            response_data["users"].append({
                "id": user.id,
                "no": user.no,
                "name": user.name,
                "password": user.password,
                "sex": user.sex,
                "grade": user.grade,
                "dept": user.dept,
                "major": user.major,
                "title": user.title,

            })

    return jsonify(response_data)


@student_bp.route('/search_user/<string:user_no>', methods=['POST'])
def search_user(user_no):
    users = User.query.filter_by(no=user_no)
    if users is None:
        return jsonify({"msg": "查看失败，用户不存在"})
    else:
        response_data = {"msg": "查看成功"}
        response_data["users"] = []
        for user in users:
            response_data["users"].append({
                "id": user.id,
                "no": user.no,
                "name": user.name,
                "password": user.password,
                "sex": user.sex,
                "grade": user.grade,
                "dept": user.dept,
                "major": user.major,
                "title": user.title,
            })

    return jsonify(response_data)
