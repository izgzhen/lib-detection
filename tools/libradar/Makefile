build:
	docker build -t libradar .
run-bash:
	docker run -v $(shell realpath ../examples):/usr/src/examples -it --rm --name running-libradar libradar bash
run:
	docker run -v $(shell realpath ../examples):/usr/src/examples -it --rm --name running-libradar libradar ./runScript.sh ../examples