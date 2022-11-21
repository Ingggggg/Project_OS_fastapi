# Quick Start
if you want to test and run . Do this step!

```bash
# run fastapi
uvicorn main:app
```

# Run with Docker
- build and run image <br>
```bash
docker build -t fast .
docker run --name cont-fast -p 3050:3050 fast
```
from above after this step you can go to browser then type your url with http://localhost:3050/docs

# Public URL
- use ngrok
- open public url from uvicorn
```bash
ngrok http 8000
```
get link from Forwarding

![image](https://user-images.githubusercontent.com/89680829/203098110-9c5bd8fd-9a69-4a34-afe7-4034ee6a9256.png)
