docker build --platform=linux/amd64 -t penn-apps-api . ;
docker tag penn-apps-api thombahm/penn-apps:penn-apps-api ;
docker push thombahm/penn-apps:penn-apps-api