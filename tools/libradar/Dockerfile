FROM openjdk:8
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp

RUN apt-get update
RUN apt-get install -y wget unzip python-pip git

RUN git clone https://github.com/pkumza/LiteRadar

RUN wget https://raw.githubusercontent.com/pkumza/Data_for_LibRadar/master/lite_dataset_10.csv
RUN mv lite_dataset_10.csv LiteRadar/LiteRadar/Data/
