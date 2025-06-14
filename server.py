from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import base64
import asyncio

app = FastAPI()

# --- Timeout Middleware ---
REQUEST_TIMEOUT = 30  # seconds


@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    try:
        return await asyncio.wait_for(call_next(request), timeout=REQUEST_TIMEOUT)
    except asyncio.TimeoutError:
        return JSONResponse(
            {"detail": "Request exceeded the time limit for processing"},
            status_code=504,
        )


# --- Request and Response Models ---
class Link(BaseModel):
    url: str
    text: str


class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None  # base64-encoded string


class AnswerResponse(BaseModel):
    answer: str
    links: List[Link]


# --- Endpoint Implementation ---
@app.post("/api/", response_model=AnswerResponse)
async def answer_question(req: QuestionRequest):
    # Optionally decode and process the image
    if req.image:
        try:
            image_bytes = base64.b64decode(req.image)
            # You can process the image here if needed
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid base64 image data")

    # Dummy logic for demonstration - replace with your actual answer logic
    answer = "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question."
    links = [
        Link(
            url="https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
            text="Use the model that’s mentioned in the question.",
        ),
        Link(
            url="https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
            text="My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate.",
        ),
    ]

    return AnswerResponse(answer=answer, links=links)
