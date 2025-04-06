FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim as builder

WORKDIR /app
COPY pyproject.toml .
COPY uv.lock .
RUN uv sync

FROM python:3.11-slim-buster AS prod

WORKDIR /app
ARG BUILDER_PACKAGE_PATH="/app/.venv/lib/python3.11/site-packages"
ARG PROD_PACKAGE_PATH="/usr/local/lib/python3.11"
COPY --from=builder ${BUILDER_PACKAGE_PATH} ${PROD_PACKAGE_PATH}
