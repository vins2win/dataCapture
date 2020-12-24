docker build . --tag datadjango
docker tag datadjango cognetrytestrepo.azurecr.io/datadjango:dev

docker push cognetrytestrepo.azurecr.io/datadjango:dev 

kubectl apply -f datadjango.yaml --validate=false