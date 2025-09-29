FROM python:3.9
WORKDIR /app
COPY test99.py .
RUN pip install requests
CMD ["python", "test99.py"]