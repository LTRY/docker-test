cd ./flask

docker build -t test:latest .
docker run -d -p 5000:5000 --name container-test test

sleep 2
curl localhost:5000

docker stop container-test
docker rm container-test
