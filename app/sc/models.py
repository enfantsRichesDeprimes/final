from app.exts import db

class Sc(db.Model):
    __tablename__ = "sc"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(255), db.ForeignKey('user.no'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    student = db.relationship('User', backref='sc')
    course = db.relationship('Course', backref='sc')

    def __repr__(self):
        return f"<Sc {self.id}>"