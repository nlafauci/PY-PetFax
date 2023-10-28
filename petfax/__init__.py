from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    return app