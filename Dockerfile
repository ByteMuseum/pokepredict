FROM python:3.12

WORKDIR /pokepredict

COPY . /pokepredict

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["sh", "entrypoint.sh"]