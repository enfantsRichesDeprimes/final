import sys
sys.path.append(r'.')
from app import app
from app import config
from app.exts import db


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run('0.0.0.0', 8000)
