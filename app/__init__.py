from flask import Flask
from flask_migrate import Migrate
from app.exts import db, mail, cache

# 导入蓝图
from app.course import course_bp
from app.student import student_bp
from app.sc import sc_bp
from app.web import web_bp


# 这里用as重命名是为了用户启动时不用区分是dev_config还是pro_config
from configs import dev_config as config

# 实例化flask
app = Flask(__name__)

# 从文件里面加载配置项
app.config.from_object(config)

app.static_folder = 'static'

app.register_blueprint(course_bp)
app.register_blueprint(student_bp)
app.register_blueprint(sc_bp)
app.register_blueprint(web_bp)

# 将app和SQLAlchemy关联起来，初始数据库
db.init_app(app)

# 数据迁移文件
migrate = Migrate(app, db)

# 发邮箱
mail.init_app(app)

# 缓存
cache.init_app(app)
