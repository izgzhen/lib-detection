FROM openjdk:8
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
ENV PATH="/usr/src/myapp/apktool/:${PATH}"

RUN apt-get update
RUN apt-get install -y wget unzip python-pip git

RUN git clone https://github.com/izgzhen/apktool

RUN wget https://github.com/androguard/androguard/archive/1.9.zip
RUN unzip 1.9.zip
RUN cd androguard-1.9; pip install .
RUN mkdir decompose
RUN python libd_v_0.0.1.py examples/c577b7e730f955a5f99642e5a8898f64a5b5080d1bf2096804f9992a895ac956.apk decompose/ whitelist
