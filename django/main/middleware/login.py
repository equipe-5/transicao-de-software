from urllib.parse import urlparse

from django.conf import settings
from django.urls import reverse
from django.contrib.auth.views import redirect_to_login


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_urls = [reverse(url) for url in settings.PUBLIC_URLS]

        full_path = request.get_full_path()
        path = urlparse(full_path).path
        if not path.endswith('/'):
            path = path + '/'

        if not request.user.is_authenticated and path not in public_urls:
            return redirect_to_login(full_path)
        return self.get_response(request)
