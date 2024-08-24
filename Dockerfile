FROM alpine

RUN apk add python3

WORKDIR /myapp

COPY . .

RUN python3 -m venv .fvenv

RUN .fvenv/bin/pip install Flask psycopg2-binary

CMD ["sh","script.sh"]