from src.api.controllers.audio_controller import app
from src.api.models.audio import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:my-secret-pw@127.0.0.1:3306/mydatabase'
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)