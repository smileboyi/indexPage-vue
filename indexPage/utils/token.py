from itsdangerous import URLSafeTimedSerializer as utsr
from django.conf import settings as django_settings
import base64
import re

class Token:
	def __init__(self, security_key):
		self.security_key = security_key
		self.salt = base64.encodestring(b'webapp')
	def generate_validate_token(self, data):
		serializer = utsr(self.security_key)
		return serializer.dumps(data, self.salt)
	def confirm_validate_token(self, token, expiration=3600):
		serializer = utsr(self.security_key)
		return serializer.loads(token, salt=self.salt, max_age=expiration)
	def remove_validate_token(self, token):
		serializer = utsr(self.security_key)
		return serializer.loads(token, salt=self.salt)

token_confirm = Token(django_settings.SECRET_KEY)
