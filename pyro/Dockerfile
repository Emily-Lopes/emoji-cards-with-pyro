FROM python:3.10

RUN apt-get update
RUN pip install Pyro5

EXPOSE 9090

CMD python3 -m Pyro5.nameserver
