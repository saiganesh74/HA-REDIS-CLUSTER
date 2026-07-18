FROM python:3.12-slim 
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
COPY discover_master.py .
CMD [ "python","discover_master.py" ]