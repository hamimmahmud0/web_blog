from flask import Flask

app = Flask(__name__)

from app import blog
from app import static
from app import project_manager
from app import admin