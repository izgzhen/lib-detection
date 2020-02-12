FROM openjdk:8
RUN apt-get update
RUN apt-get install -y wget unzip python-pip git

COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
ENV PATH="/usr/src/myapp/apktool/:${PATH}"

RUN git clone https://github.com/izgzhen/apktool

RUN wget https://github.com/androguard/androguard/archive/1.9.zip
RUN unzip 1.9.zip
RUN cd androguard-1.9; pip install .
# copy over the correct version of androguard
RUN rm -r androguard-1.9/androguard
RUN cp -r androguard androguard-1.9
RUN mkdir decompose
