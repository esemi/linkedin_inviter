Linkedin inviter.
========
[![linters](https://github.com/esemi/linkedin_inviter/actions/workflows/linters.yml/badge.svg?branch=master)](https://github.com/esemi/linkedin_inviter/actions/workflows/linters.yml)


### Local setup
```shell
$ git clone git@github.com:esemi/linkedin_inviter.git
$ cd linkedin_inviter
$ python3.11 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry
$ poetry install
```

### Run linters
```bash
$ poetry run mypy app/
$ poetry run flake8 app/
```

### Run inviter
```bash
python -m app.inviter
```
