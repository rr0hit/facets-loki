# Stage 1 - Install build dependencies
FROM python:3.7-alpine AS builder
WORKDIR /app
RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir -U pip setuptools
COPY requirements.txt .
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt && find /app/.venv \( -type d -a -name test -o -name tests \) -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' \+
# Stage 2 - Copy only necessary files to the runner stage
FROM python:3.7-alpine
RUN apk add --update --no-cache bind-tools
WORKDIR /app
COPY --from=builder /app /app
COPY src/ .
ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "seed.py"]