# AI service Dockerfile
# Uses a Python version compatible with the project's requirements.

FROM python:3.14-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY . .
RUN uv sync --frozen

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]