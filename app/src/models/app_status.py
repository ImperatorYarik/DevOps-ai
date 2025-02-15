from src import db

class AppStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_initialized = db.Column(db.Boolean, default=False)

    @classmethod
    def get_status(cls):
        status = cls.query.first()
        if status is None:
            status = cls(is_initialized=False)
            db.session.add(status)
            db.session.commit()
        return status