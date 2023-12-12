from flask import Blueprint

course_bp = Blueprint(
    "course_bp",
    __name__,
    url_prefix="/course",
)

from . import views