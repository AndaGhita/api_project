from flask import Flask, jsonify, request

app = Flask(__name__)

#Import routers
from .routers import bp
app.register_blueprint(bp)

return app
