
from flask import Flask
from flask_migrate import Migrate
from app.exts import db, mail, cache


from app.course import course_bp
from app.student import student_bp
from app.sc import sc_bp
from app.web import web_bp



from configs import dev_config as config


app = Flask(__name__)


app.config.from_object(config)

app.static_folder = 'static'

app.register_blueprint(course_bp)
app.register_blueprint(student_bp)
app.register_blueprint(sc_bp)
app.register_blueprint(web_bp)


db.init_app(app)


migrate = Migrate(app, db)


mail.init_app(app)


cache.init_app(app)
