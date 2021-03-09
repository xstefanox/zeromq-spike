FROM python:3.9-slim
RUN pip install pipenv
WORKDIR /opt
COPY . .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install
ENV PYTHONPATH=.
