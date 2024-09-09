from django.conf import settings

lock_tokens_settings = getattr(settings, 'LOCK_TOKENS', {})

TIMEOUT = lock_tokens_settings.get('TIMEOUT', 3600)
API_CSRF_EXEMPT = lock_tokens_settings.get('API_CSRF_EXEMPT', False)
