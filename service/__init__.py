from flask import Flask

from service import static

app = Flask(__name__)
app.config.from_object('config')

static.register_assets(app)
