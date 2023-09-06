Linkedin inviter.
========
[![linters](https://github.com/esemi/linkedin_inviter/actions/workflows/linters.yml/badge.svg?branch=master)](https://github.com/esemi/linkedin_inviter/actions/workflows/linters.yml)


### Local setup
```bash
git clone git@github.com:esemi/linkedin_inviter.git
cd linkedin_inviter
python3.11 -m venv venv
source venv/bin/activate
pip install -U poetry
poetry install
```

### Run linters
```bash
poetry run mypy app/
poetry run flake8 app/
```

### Run inviter
```bash
python -m app.inviter
```


### Destination host preparing
```bash
add-apt-repository ppa:deadsnakes/ppa
apt update
apt install python3.11 python3.11-venv python3.11-dev
adduser USERNAME
scp -r .inviter_session/ USERNAME@HOSTNAME:~/.inviter_session 
```