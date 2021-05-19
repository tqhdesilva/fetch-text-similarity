from fastapi import FastAPI
from pydantic import BaseModel
from text_similarity import similarity

app = FastAPI()


@app.get("/health")
def health():
    return


class SimilarityRequest(BaseModel):
    text1: str
    text2: str


class SimilarityResponse(BaseModel):
    score: float


@app.post("/similarity", response_model=SimilarityResponse)
def similarity_endpoint(request: SimilarityRequest):
    score = similarity(request.text1, request.text2)
    return SimilarityResponse(score=score)
