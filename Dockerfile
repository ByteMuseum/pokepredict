FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip libhdf5-dev

WORKDIR /pokepredict

COPY . /pokepredict

# print the libhdf5 path
RUN dpkg -L libhdf5-dev



RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["sh", "entrypoint.sh"]



# FROM python:3.12

# WORKDIR /pokepredict

# COPY . /pokepredict

# RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 5000

# CMD ["sh", "entrypoint.sh"]