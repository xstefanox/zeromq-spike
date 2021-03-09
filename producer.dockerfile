FROM python:3.9-slim
RUN pip install pipenv
WORKDIR /opt/
ADD producer ./producer
ADD Pipfile* .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install
ENV PYTHONPATH=.
CMD ["pipenv", "run", "producer"]
EXPOSE 5555
