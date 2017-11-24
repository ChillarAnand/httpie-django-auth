"""
Django Auth plugin for HTTPie.
"""

import json
import os
import shlex
import subprocess

try:
    # If Python 3
    from urllib.parse import urlsplit
except ImportError:
    # If Python 2
    from urlparse import urlsplit
    
from httpie.plugins import AuthPlugin, builtin


auth_endpoint = os.environ.get('HTTPIE_DJANGO_AUTH_URL', '/tech-admin/login/')


def get_session_file(domain, session_name):
    domain = domain.replace(':', '_')
    file_path = '~/.httpie/sessions/{}/{}.json'.format(domain, session_name)
    return os.path.expanduser(file_path)


def clean_session(domain, session_name):
    file_path = get_session_file(domain, session_name)
    try:
        os.remove(file_path)
    except OSError:
        pass


def run_shell_command(cmd):
    print(cmd)
    subprocess.check_output(shlex.split(cmd))


class DjangoAuth(builtin.HTTPBasicAuth):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session_name = 'httpie_django_auth'

    def __call__(self, r):
        result = urlsplit(r.url)
        scheme = result.scheme
        domain = result.netloc

        login_url = '{}://{}{}'.format(scheme, domain, auth_endpoint)

        clean_session(domain, self.session_name)
        cmd = 'http GET {} --session={}'.format(login_url, self.session_name)
        run_shell_command(cmd)

        session = json.load(open(get_session_file(domain, self.session_name)))
        csrf_token = session['cookies']['csrftoken']['value']
        cmd = 'http -f POST {} username={} passowrd={} X-CSRFToken:{} --session={}'.format(
            login_url, self.username, self.password, csrf_token, self.session_name
        )
        run_shell_command(cmd)
        return r


class DjangoAuthPlugin(AuthPlugin):

    name = 'django auth'
    auth_type = 'django'
    description = 'Sign requests using a django authentication method like AWS'

    def get_auth(self, username=None, password=None):
        return DjangoAuth(username, password)
