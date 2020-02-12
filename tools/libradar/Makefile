DOCKER := docker run -v $(shell realpath ../examples):/usr/src/examples -v $(PWD):/mnt -it --rm --name running-libradar libradar

build:
	docker build -t libradar .

run-bash:
	$(DOCKER) bash

run: build
	mkdir -p output
	$(DOCKER) ./runScript.sh ../examples
