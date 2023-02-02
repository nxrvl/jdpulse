import openai
import config
import re


def str_to_list(text: str) -> list:
    """Converts a string to a list of strings. Each string is a line in the original string."""
    return text.split("\n")


def clean_openai_answer_to_list(text: str) -> list:
    """Cleans the answer from OpenAI and returns a list of strings."""
    text = text.replace(".", "")
    text = re.sub(r"[^a-zA-Z,/\s-]\(\)", "", text)
    text_list = []
    for item in text.split(","):
        if item == "":
            pass
        elif len(item) < 4:
            pass
        else:
            text_list.append(item.strip())
    return text_list


def extract(
    text: str,
    model: str = "text-davinci-003",
    temperature: float = 0.5,
    max_tokens: int = 150,
    top_p: float = 1,
    frequency_penalty: float = 0.5,
    presence_penalty: float = 0,
) -> list:
    """Extract keywords from a job description."""
    openai.api_key = config.OPENAI_API_KEY
    response = openai.Completion.create(
        model=model,
        prompt="Extract keywords from the following text:\n\n" + text,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    print(response["choices"][0]["text"])
    text_list = clean_openai_answer_to_list(response["choices"][0]["text"])
    return text_list
