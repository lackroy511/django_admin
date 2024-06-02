FROM python:slim

USER root

WORKDIR /root/project
COPY . .

COPY .ssh/ /root/.ssh/
RUN chmod 700 /root/.ssh && \
    chmod 600 /root/.ssh/*

ENV PYTHONPATH="${PYTHONPATH}:/root/project"

RUN apt update 

RUN apt install -y nodejs

RUN pip install flake8 flake8-bugbear pep8-naming flake8-commas \
    flake8-multiline-containers flake8-class-attributes-order flake8-clean-block \
    flake8-indent-in-def flake8-newspaper-style flake8-return flake8-length flake8-quotes \
    isort

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt
RUN apt install -y git
RUN git config --global user.name "lackroy511"
RUN git config --global user.email lackroy5111@gmail.com