# ML_in_Prod_batch_1_proj
```bash

#docker build
docker build . -t sample_fastapi

#docker run
docker run -p 8080:8080 sample_fastapi

#docker run with env
docker run -p 8080:8080 --env APP_VERSION=v9999 sample_fastapi
```
