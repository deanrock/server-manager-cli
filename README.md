# server-manager-cli

CLI tool for server manager (https://github.com/deanrock/server-manager).

## Features

* redeploy apps on server-manager accounts

## Setup

```bash
pip install git+https://github.com/deanrock/server-manager-cli
```

## Credentials file

You need to create `~/.smcli` file with credentials about server-manager installation:
```bash
[credentials]
hostname=http://example.com:4444
username=ci-user
password=mypassword
```

## Usage

### Redeploy application `php56` of `my-blog` account:
```bash
smcli --account=my-blog redeploy-app --name=php56
```

## For developers

```bash
virtualenv ./env
pip install -e https://github.com/deanrock/server-manager-cli
```

## TODO

- [ ] Support executing of shell commands
- [ ] Fix returning of success/failure when redeploy an app (SM API needs to be changed)
