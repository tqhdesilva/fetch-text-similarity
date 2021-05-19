# fetch-text-similarity
Fetch text similarity take home.


# Test the text_similarity module
Simply run `python text_similarity.py` to run the tests on the three given samples.
You can also import from the module:
```python
from text_similarity import similarity

similarity('hello world', 'goodbye world')
```

# Build the docker image
Run the following docker command to build the image locally:
```
docker build -t fetch-text-similarity:1.0 .
```

The following command will serve the FastAPI application on port `8000` locally:
```
docker run --rm -it -p 8000:80 fetch-text-similarity:1.0
```

`test.http` contains some requests to test the endpoint.
API docs are available at `http://localhost:8000/docs`.