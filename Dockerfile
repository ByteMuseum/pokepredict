FROM python:3.12

WORKDIR /pokepredict

COPY . /pokepredict

RUN pip install --upgrade pip

RUN pip install --no-cache-dir virtualenv

RUN virtualenv venv

RUN . venv/bin/activate

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "server.py"]