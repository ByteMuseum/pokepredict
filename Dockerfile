FROM ubuntu:24.04

RUN apt-get update && apt-get install -y python3 python3-pip libhdf5-dev python3.12-venv

WORKDIR /pokepredict

COPY . /pokepredict

ENV HDF5_DIR=/usr/lib/aarch64-linux-gnu/hdf5/serial

RUN python3 -m venv venv

RUN . venv/bin/activate

RUN python3 -m pip install --upgrade pip --break-system-packages

RUN pip3 install -r requirements.txt --break-system-packages

EXPOSE 5443

CMD ["sh", "entrypoint.sh"]
