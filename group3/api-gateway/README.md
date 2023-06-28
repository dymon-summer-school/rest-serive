# build image

docker build -t api-gateway-3 .

# run container

docker run -p 4300:80 api-gateway-3
