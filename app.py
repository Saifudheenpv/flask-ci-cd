from flask import Flask, jsonify
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info('Homepage endpoint accessed')
    return jsonify({
        'message': 'Hello, DevOps World!',
        'timestamp': datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring."""
    logger.info('Health check endpoint accessed')
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.errorhandler(404)
def not_found(error):
    logger.error(f'Page not found: {error}')
    return jsonify({
        'error': 'Resource not found',
        'status': 404
    }), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Server error: {error}')
    return jsonify({
        'error': 'Internal server error',
        'status': 500
    }), 500

if __name__ == '__main__':
    logger.info('Starting Flask application...')
    app.run(host='0.0.0.0', port=5001, debug=True)
