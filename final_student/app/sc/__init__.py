from flask import Blueprint

sc_bp = Blueprint(
    "sc_bp",
    __name__,
    url_prefix="/sc",
)

from . import views