FROM python:3.11-slim

WORKDIR /app

# copy dependencies file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

EXPOSE 3000

CMD ["python", "app.py"]
