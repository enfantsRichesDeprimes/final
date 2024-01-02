HOSTNAME="localhost"
PORT=3306
USERNAME="root"
PASSWORD=""
DATABASE="web"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True  # 追踪修改
SECRET_KEY = "dev"
WTF_CSRF_ENABLED = False
HOST = "127.0.0.1"
PORT = 5000
DEBUG = True
TEMPLATES_AUTO_RELOAD = True