from app.exts import db

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    class_hour = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String(255), nullable=False)
    dept = db.Column(db.String(255), nullable=False)
    major = db.Column(db.String(255), nullable=False)
    grade = db.Column(db.String(255), nullable=False)
    semester = db.Column(db.String(255), nullable=False)
    time = db.Column(db.String(255), nullable=False)
    place = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    max_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Course {self.name}>"