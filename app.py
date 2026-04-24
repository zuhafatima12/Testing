from flask import Flask
import os   
#app 
app = Flask(__name__)
app.config.from_object('config.Config')
from database import db
db.init_app(app)
from routes import routes
app.register_blueprint(routes)  
if __name__ == '__main__':
    app.run(debug=True)
    
    
