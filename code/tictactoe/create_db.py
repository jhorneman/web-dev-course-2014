from application import create_app


def create_db(db):
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        create_db(app.db)
