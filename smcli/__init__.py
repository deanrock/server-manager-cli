import click
import os
import json
import sys
import requests
import ConfigParser


class API:
    def __init__(self, host):
        self.host = host
        self.session = requests.Session()

    def _get(self, path):
        return self.session.get(self.host + path).json()

    def _post(self, path, data=None):
        r = self.session.post(self.host + path, data=json.dumps(data))

        # return empty object if no response text (this happens on login API)
        if r.text == '':
            return {}

        return r.json()

    def login(self, username, password):
        return self._post('/api/v1/auth/login', data={
            'username': username,
            'password': password
        })

    def profile(self):
        return self._get('/api/v1/profile')

    def apps(self, account):
        return self._get('/api/v1/accounts/%s/apps' % account)

    def redeploy_app(self, account, app):
        return self._post('/api/v1/accounts/%s/apps/%s/redeploy'
                          % (account, app))


config = ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/.smcli'))


api = API(config.get('credentials', 'hostname'))
api.login(config.get('credentials', 'username'),
          config.get('credentials', 'password'))


@click.group()
@click.option('--account',
              help='Name of the account.')
@click.pass_context
def cli(ctx, account):
    ctx.obj['account'] = account


@cli.command()
def profile():
    p = api.profile()
    print(json.dumps(p['user'], indent=4))


@cli.command(name='redeploy-app')
@click.option('--name',
              prompt='App name',
              help='Name of the application to redeploy.')
@click.pass_context
def redeploy_app(ctx, name):
    found = None

    apps = api.apps(ctx.obj['account'])

    for app in apps:
        if app['name'] == name:
            found = app
            break

    if not found:
        print("cannot find app with the name: %s" % (name,))
        sys.exit(1)

    o = api.redeploy_app(ctx.obj['account'], app['id'])
    print(json.dumps(o, indent=4))


def myCli():
    return cli(obj={})


if __name__ == '__main__':
    myCli()
