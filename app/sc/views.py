from flask import jsonify,session
from app.sc import sc_bp
from app.sc.models import Sc
from app.exts import db
import os
current_path = os.path.dirname(__file__)
ttf_file_path = os.path.join(current_path, "static", "ttf", "ziti.ttf")
from .forms import ScForm, DeleteScForm, UpdateScForm, SearchByStudentNoForm, SearchByCourseNoForm

@sc_bp.route('/add', methods=['POST'])
def add_sc():
    form = ScForm()
    if form.validate_on_submit():
        # 在这里处理添加选课关系逻辑，例如将表单提交的数据保存到数据库中
        validate_data = form.data
        sc = Sc(**validate_data)
        db.session.add(sc)
        db.session.commit()
        session.clear()

        response_data = {"msg": "添加成功"}
        response_data["student_no"] = Sc.student_no
        response_data["course_no"] = Sc.course_no
        response_data["grade"] = Sc.grade

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "添加失败"}
        response_data.update(form.errors)

@sc_bp.route('/delete', methods=['POST'])
def delete_sc():
    form = DeleteScForm()
    if form.validate_on_submit():
        # 在这里处理删除选课关系逻辑，例如将表单提交的数据保存到数据库中
        student_no = form.data["student_no"]
        course_no = form.data["course_no"]
        sc = Sc.query.filter_by(student_no=student_no,course_no=course_no).first()
        if sc is None:
            return jsonify({"msg": "删除失败，选课关系不存在"})
        else:
            db.session.delete(sc)
            db.session.commit()
            session.clear()
            response_data = {"msg": "删除成功"}

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "删除失败"}
        response_data.update(form.errors)

@sc_bp.route('/update', methods=['POST'])
def update_sc():
    form = UpdateScForm()
    if form.validate_on_submit():
        # 在这里处理更新选课关系逻辑，例如将表单提交的数据保存到数据库中
        student_no = form.data["student_no"]
        course_no = form.data["course_no"]
        sc = Sc.query.filter_by(student_no=student_no,course_no=course_no).first()
        if sc is None:
            return jsonify({"msg": "更新失败，选课关系不存在"})
        else:
            sc.grade = form.data["grade"]
            db.session.commit()
            session.clear()
            response_data = {"msg": "更新成功"}

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "更新失败"}
        response_data.update(form.errors)

@sc_bp.route('/search_by_student_no', methods=['POST'])
def search_by_student_no():
    form = SearchByStudentNoForm()
    if form.validate_on_submit():
        # 在这里处理按学生学号查询选课关系逻辑，例如将表单提交的数据保存到数据库中
        student_no = form.data["no"]
        sc = Sc.query.filter_by(student_no=student_no).all()
        if sc is None:
            return jsonify({"msg": "查询失败，选课关系不存在"})
        else:
            response_data = {"msg": "查询成功"}
            response_data["sc"] = sc

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "查询失败"}
        response_data.update(form.errors)

@sc_bp.route('/search_by_course_no', methods=['POST'])
def search_by_course_no():
    form = SearchByCourseNoForm()
    if form.validate_on_submit():
        # 在这里处理按课程编号查询选课关系逻辑，例如将表单提交的数据保存到数据库中
        course_no = form.data["no"]
        sc = Sc.query.filter_by(course_no=course_no).all()
        if sc is None:
            return jsonify({"msg": "查询失败，选课关系不存在"})
        else:
            response_data = {"msg": "查询成功"}
            response_data["sc"] = sc

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "查询失败"}
        response_data.update(form.errors)

@sc_bp.route('/all', methods=['POST'])
def all_sc():
    sc = Sc.query.all()
    if sc is None:
        return jsonify({"msg": "查询失败，选课关系不存在"})
    else:
        response_data = {"msg": "查询成功"}
        response_data["sc"] = sc

