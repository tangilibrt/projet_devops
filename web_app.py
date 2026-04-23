from flask import Flask
from controllers.greeting_controller import greeting_bp

app = Flask(__name__)
app.register_blueprint(greeting_bp)

if __name__ == "__main__":
    app.run()
