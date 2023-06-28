# build image

docker build -t api-gateway-1 .

# run container

docker run -p 4100:80 api-gateway-1
