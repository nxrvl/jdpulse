from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import extraction
import uvicorn

app = FastAPI()


@app.get("/api")
async def root():
    return {"message": "Hello World"}


@app.get("/api/get_keywords")
async def extract_jd(
    text: str,
    model: str | None = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
    top_p: float | None = None,
    frequency_penalty: float | None = None,
    presence_penalty: float | None = None,
    openai_api_key: str | None = None,
) -> JSONResponse:
    try:
        keywords = extraction.extract(text, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, openai_api_key)
    except Exception as e:
        return JSONResponse(content={"error": str(e)})
    return JSONResponse(content={"keywords": keywords})


def main():
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()
