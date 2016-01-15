import atexit
from flask_wtf.csrf import CsrfProtect  # type: ignore
import logging

from service.server import app

LOGGER = logging.getLogger(__name__)


@atexit.register
def handle_shutdown(*args, **kwargs):
    LOGGER.info('Stopped the server')

LOGGER.info('Starting the server')
CsrfProtect(app)
port = int(app.config.get('PORT', 8011))
app.debug=True
app.run(host='0.0.0.0', port=port)
