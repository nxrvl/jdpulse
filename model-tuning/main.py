import requests
import json


def load_text(file_path: str) -> str:
    with open(file_path, "r") as f:
        text = f.read()
    return text


def extract(
    api_url: str,
    text: str,
    model: str = "text-davinci-003",
    temperature: float = 0.5,
    max_tokens: int = 150,
    top_p: float = 1,
    frequency_penalty: float = 0.5,
    presence_penalty: float = 0,
) -> list:
    """Extract keywords from a job description."""
    keywords = requests.get(
        api_url,
        params={
            "text": text,
            "model": model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
        },
    )
    return keywords.json()


def results_generator(values: dict) -> str:
    """Generates a string with the results of the extraction."""
    for key, value in values.items():
        print(value[0], value[1], value[2], value[3], value[4])
        result = extract(
            "http://localhost:8000/extract",
            load_text("jd.txt"),
            value[0],
            float(value[1]),
            int(value[2]),
            float(value[3]),
            float(value[4]),
            float(value[5]),
        )
        print(f"{key}: {result}")


def main():
    with open("parameters.json", "r") as f:
        values = json.load(f)

    results_generator(values)


if __name__ == "__main__":
    main()
