DOCKER := docker run -v $(shell realpath ../examples):/usr/src/examples -v $(PWD):/mnt -it --rm --name running-libd libd

build:
	docker build -t libd .

run-bash:
	$(DOCKER) bash

run: build
	mkdir -p output
	$(DOCKER) ./runScript.sh ../examples
