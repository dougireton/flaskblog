FROM python:3-alpine
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["python", "flaskblog.py"]