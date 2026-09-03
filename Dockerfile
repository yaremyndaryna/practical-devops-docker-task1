FROM python:3.9-alpine
WORKDIR /code
COPY requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt && pip3 install gunicorn
COPY . .
ENV REDIS_ADDRESS=redis \
    REDIS_PORT=6379
EXPOSE 8000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "home:app"]
