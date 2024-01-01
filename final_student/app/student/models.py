from app.exts import db

class User(db.Model):
    """用户表，目前有no、name、password、sex、grade、dept、major、title"""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.String(255), nullable=False)
    grade = db.Column(db.String(255), nullable=False)
    dept = db.Column(db.String(255), nullable=False)
    major = db.Column(db.String(255))
    title = db.Column(db.String(255))

    def __repr__(self):
        return f"<User {self.name}>"

    def check_password(self, password):
        """检查密码是否正确"""
        return self.password == password