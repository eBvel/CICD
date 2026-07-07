FROM python:3.10
WORKDIR /image
COPY app/area.py ./app/
COPY tests ./tests/
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only=test
CMD ["pytest", "tests"]