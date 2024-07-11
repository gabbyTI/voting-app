FROM python:3.9

WORKDIR /app

COPY scale_hpa.py .

RUN pip install kubernetes

CMD ["python", "./scale_hpa.py"]