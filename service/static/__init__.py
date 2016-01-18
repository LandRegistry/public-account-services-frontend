from flask.ext.assets import Environment # type: ignore
from . import pipeline

assets = Environment()

assets.register('styleguide_js', pipeline.js)
assets.register('styleguide', pipeline.sass)

def register_assets(app):
    assets.init_app(app)
    return assets
