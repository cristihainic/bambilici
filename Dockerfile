FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /game
WORKDIR /game
COPY requirements.txt /game/
RUN pip install -r requirements.txt
COPY ./game/ /game/
EXPOSE 80

CMD python app.py