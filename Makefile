build:
	docker build -t my-test-image12345 .
run:
	docker run -ti -v `pwd`:/home/root my-test-image12345