FROM python:3.12-alpine AS builder
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.in-project true && poetry install --no-dev
COPY . /app

FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app
RUN ls -pilaF /app
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8080
ENV PONG_LISTENING_ADDRESS=":8080"
CMD ["python", "pong_py/main.py"]