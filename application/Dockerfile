FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask requests
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*
CMD ["python", "app.py"]
