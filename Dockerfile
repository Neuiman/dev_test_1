FROM python:3.12.6

RUN mkdir "app"

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x scripts/*.sh

CMD [ "./scripts/start.sh"]