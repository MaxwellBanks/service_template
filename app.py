from flask import Flask

from errors.handlers import errors_bp
from api.routes import api_bp

app = Flask(__name__)

app.register_blueprint(errors_bp)
app.register_blueprint(api_bp, url_prefix='/api')


if __name__ == '__main__':
    app.run(port=9300)
