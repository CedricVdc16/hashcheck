# hashcheck (Dockerized)
Petit CLI de hachage/verification SHA256 (texte ou fichier).

## Build & run locaux
docker build -t yourdockeruser/hashcheck:local .
docker run --rm yourdockeruser/hashcheck:local --text "hello"
docker run --rm -v "$PWD:/data" yourdockeruser/hashcheck:local --file /data/README.md
docker run --rm yourdockeruser/hashcheck:local --text "hello" --verify 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

## CI
- Configurez DOCKERHUB_USERNAME et DOCKERHUB_TOKEN dans GitHub → Settings → Secrets and variables → Actions.
- Poussez sur main : l'action build, teste, et pousse sur Docker Hub.
