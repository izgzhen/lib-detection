build:
	docker build -t libd .

run-bash:
	docker run -v $(shell realpath ../examples):/usr/src/examples -it --rm --name running-libd libd bash

run:
	docker run -v $(shell realpath ../examples):/usr/src/examples -it --rm --name running-libd libd ./runScript.sh ../examples
