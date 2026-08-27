FROM python:3.10
RUN pip3 install --upgrade pip
RUN pip3 install notebook
RUN pip3 install numpy==1.23.5
RUN pip3 install matplotlib
WORKDIR /home/MIA2526
#VOLUME .
CMD jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser
