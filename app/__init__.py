from flask import Flask

app = Flask(__name__)

from app import models, auth, web, private