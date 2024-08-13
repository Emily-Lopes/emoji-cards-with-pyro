FROM python:3.10

COPY requirements.txt ./

RUN apt-get update
# # && apt-get install -y 

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python3 -u server.py