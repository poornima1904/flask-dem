from flask import Flask

from home import home_bp
from contact import contact_bp

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')
app.logger.debug('This is a DEBUG message')
app.logger.info('This is an INFO message')
app.logger.warning('This is a WARNING message')
app.logger.error('This is an ERROR message')

app.run()