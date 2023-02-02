from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import extraction
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/extract")
async def extract_jd(
    text: str,
    model: str | None = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
    top_p: float | None = None,
    frequency_penalty: float | None = None,
    presence_penalty: float | None = None,
) -> JSONResponse:
    keywords = extraction.extract(text)
    return JSONResponse(content=keywords)


def main():
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()
