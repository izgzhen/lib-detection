build:
	docker build -t libradar .

run:
	docker run -v $(shell realpath ../examples):/usr/src/examples -it --rm --name running-libradar libradar python LiteRadar/LiteRadar/literadar.py /usr/src/examples/c577b7e730f955a5f99642e5a8898f64a5b5080d1bf2096804f9992a895ac956.apk
