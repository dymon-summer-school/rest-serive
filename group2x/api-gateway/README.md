# build image

docker build -t api-gateway-2 .

# run container

docker run -p 4200:80 api-gateway-2
