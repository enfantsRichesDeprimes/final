from flask import jsonify, session
from app.course import course_bp
from app.exts import db
import os

current_path = os.path.dirname(__file__)
ttf_file_path = os.path.join(current_path, "static", "ttf", "ziti.ttf")
from .models import Course
from .forms import CourseForm, DeleteCourseForm, UpdateCourseForm, SearchByTeacherNoForm, SearchByCourseNoForm


@course_bp.route('/add', methods=['POST'])
def add_course():
    form = CourseForm(csrf_enabled=False)
    if form.validate_on_submit():
        # 在这里处理添加课程逻辑，例如将表单提交的数据保存到数据库中
        validate_data = form.data
        course = Course(**validate_data)
        db.session.add(course)
        db.session.commit()
        session.clear()

        response_data = {"msg": "添加成功"}
        response_data["no"] = Course.id
        response_data["name"] = Course.name
        response_data["credit"] = Course.credit
        response_data["class_hour"] = Course.class_hour
        response_data["teacher"] = Course.teacher
        response_data["dept"] = Course.dept
        response_data["major"] = Course.major
        response_data["grade"] = Course.grade
        response_data["semester"] = Course.semester
        response_data["time"] = Course.time
        response_data["place"] = Course.place
        response_data["number"] = Course.number
        response_data["max_number"] = Course.max_number

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "添加失败"}
        response_data.update(form.errors)

    return jsonify(response_data)


@course_bp.route('/delete/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    form = DeleteCourseForm(csrf_enabled=False)
    if form.validate_on_submit():
        # 在这里处理删除课程逻辑，例如将表单提交的数据保存到数据库中
        id = course_id
        course = Course.query.filter_by(id=id).first()
        if course is None:
            return jsonify({"msg": "删除失败，课程不存在"})
        else:
            db.session.delete(course)
            db.session.commit()
            session.clear()
            response_data = {"msg": "删除成功"}

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "删除失败"}
        response_data.update(form.errors)

    return jsonify(response_data)



@course_bp.route('/update', methods=['POST'])
def update_course():
    form = UpdateCourseForm()
    if form.validate_on_submit():
        # 在这里处理更新课程逻辑，例如将表单提交的数据保存到数据库中
        validate_data = form.data
        course = Course.query.filter_by(id=validate_data["no"]).first()
        if course is None:
            return jsonify({"msg": "更新失败，课程不存在"})
        else:
            course.name = validate_data["name"]
            course.credit = validate_data["credit"]
            course.class_hour = validate_data["class_hour"]
            course.teacher = validate_data["teacher"]
            course.dept = validate_data["dept"]
            course.major = validate_data["major"]
            course.grade = validate_data["grade"]
            course.semester = validate_data["semester"]
            course.time = validate_data["time"]
            course.place = validate_data["place"]
            course.number = validate_data["number"]
            course.max_number = validate_data["max_number"]
            db.session.commit()
            session.clear()
            response_data = {"msg": "更新成功"}

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "更新失败"}
        response_data.update(form.errors)

    return jsonify(response_data)


@course_bp.route('/search_by_teacher_no', methods=['POST'])
def search_by_teacher_no():
    form = SearchByTeacherNoForm()
    if form.validate_on_submit():
        # 在这里处理根据教师名字查看课程信息逻辑，例如将表单提交的数据保存到数据库中
        teacher = form.data["no"]
        courses = Course.query.filter_by(teacher=teacher).all()
        if courses is None:
            return jsonify({"msg": "查看失败，课程不存在"})
        else:
            response_data = {"msg": "查看成功"}
            response_data["courses"] = []
            for course in courses:
                response_data["courses"].append({
                    "no": course.id,
                    "name": course.name,
                    "credit": course.credit,
                    "class_hour": course.class_hour,
                    "teacher": course.teacher,
                    "dept": course.dept,
                    "major": course.major,
                    "grade": course.grade,
                    "semester": course.semester,
                    "time": course.time,
                    "place": course.place,
                    "number": course.number,
                    "max_number": course.max_number,
                })

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "查看失败"}
        response_data.update(form.errors)

    return jsonify(response_data)


@course_bp.route('/search_by_course_no', methods=['POST'])
def search_by_course_no():
    form = SearchByCourseNoForm()
    if form.validate_on_submit():
        # 在这里处理根据课程编号查看课程信息逻辑，例如将表单提交的数据保存到数据库中
        no = form.data["no"]
        course = Course.query.filter_by(id=no).first()
        if course is None:
            return jsonify({"msg": "查看失败，课程不存在"})
        else:
            response_data = {"msg": "查看成功"}
            response_data["course"] = {
                "no": course.id,
                "name": course.name,
                "credit": course.credit,
                "class_hour": course.class_hour,
                "teacher": course.teacher,
                "dept": course.dept,
                "major": course.major,
                "grade": course.grade,
                "semester": course.semester,
                "time": course.time,
                "place": course.place,
                "number": course.number,
                "max_number": course.max_number,
            }

    else:
        # 如果验证失败，可以提示用户错误信息，重新登录
        response_data = {"msg": "查看失败"}
        response_data.update(form.errors)

    return jsonify(response_data)


@course_bp.route('/search_all', methods=['POST'])
def search_all():
    # 在这里处理查看所有课程信息逻辑，例如将表单提交的数据保存到数据库中
    courses = Course.query.all()
    if courses is None:
        return jsonify({"msg": "查看失败，课程不存在"})
    else:
        response_data = {"msg": "查看成功"}
        response_data["courses"] = []
        for course in courses:
            response_data["courses"].append({
                "id": course.id,
                "name": course.name,
                "credit": course.credit,
                "class_hour": course.class_hour,
                "teacher": course.teacher,
                "dept": course.dept,
                "major": course.major,
                "grade": course.grade,
                "semester": course.semester,
                "time": course.time,
                "place": course.place,
                "number": course.number,
                "max_number": course.max_number,
            })

    return jsonify(response_data)


@course_bp.route('/search_course/<string:course_name>', methods=['POST'])
def search_course(course_name):
    courses = Course.query.filter_by(name=course_name)
    if courses is None:
        return jsonify({"msg": "查看失败，课程不存在"})
    else:
        response_data = {"msg": "查看成功"}
        response_data["courses"] = []
        for course in courses:
            response_data["courses"].append({
                "id": course.id,
                "name": course.name,
                "credit": course.credit,
                "class_hour": course.class_hour,
                "teacher": course.teacher,
                "dept": course.dept,
                "major": course.major,
                "grade": course.grade,
                "semester": course.semester,
                "time": course.time,
                "place": course.place,
                "number": course.number,
                "max_number": course.max_number,
            })

    return jsonify(response_data)