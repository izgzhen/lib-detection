build:
	docker build -t libd .

run-bash:
	docker run -v $(shell realpath ../examples):/usr/src/examples -it --rm --name running-libd libd bash

run:
	docker run -v $(shell realpath ../examples):/usr/src/examples -it --rm --name running-libd libd python libd_v_0.0.1.py /usr/src/examples/c577b7e730f955a5f99642e5a8898f64a5b5080d1bf2096804f9992a895ac956.apk decompose/ whitelist
