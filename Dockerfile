# start from an official image
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y

RUN mkdir -p /apps/hosamapp/src

WORKDIR /apps/hosamapp/src

COPY Pipfile Pipfile.lock /apps/hosamapp/src/

# install our dependencies
RUN pip install -U pip && pip install pipenv && pipenv install --deploy --system

# copy our project code
COPY . /apps/hosamapp/src

# expose the port 8010
EXPOSE 8010

# define the default command to run when starting the container
CMD ["gunicorn", "--bind", ":8010", "--chdir", "portfolio", "portfolio.wsgi:application"]