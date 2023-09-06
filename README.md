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
apt install python3.11 python3.11-venv python3.11-dev google-chrome-stable
adduser USERNAME

# https://googlechromelabs.github.io/chrome-for-testing/
su - USERNAME
mkdir bin
cd bin
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chrome-linux64.zip
unzip chrome-linux64.zip
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip

scp -r .inviter_session/ USERNAME@HOSTNAME:~/.inviter_session 
```