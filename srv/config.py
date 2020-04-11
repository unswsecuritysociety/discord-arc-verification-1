import os
import logging

version = '%BUILD_VERSION%'

environment = os.getenv('ENVIRONMENT', 'development')
postgres_name = os.getenv('POSTGRES_DB', 'arc_verification')
postgres_host = os.getenv('POSTGRES_HOST', '172.17.0.2')
postgres_port = os.getenv('POSTGRES_PORT', '5432')
postgres_user = os.getenv('POSTGRES_USER', 'postgres')
postgres_pass = os.getenv('POSTGRES_PASSWORD', '')

redis_host = os.getenv('REDIS_HOST', '172.17.0.3')
redis_port = os.getenv('REDIS_PORT', '6379')

api_url = os.getenv('API_URL', 'http://localhost:8000')
bot_url = os.getenv('BOT_URL', 'http://localhost:3000')

recaptcha_secret = os.getenv('RECAPTCHA_SECRET', '')

if environment == 'development':
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)