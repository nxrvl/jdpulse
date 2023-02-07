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
    openai_api_key: str = config.OPENAI_API_KEY,
) -> list:
    """Extract keywords from a job description."""
    default_values = {
        "model": "text-davinci-003",
        "temperature": 0.5,
        "max_tokens": 150,
        "top_p": 1,
        "frequency_penalty": 0.5,
        "presence_penalty": 0,
        "openai_api_key": config.OPENAI_API_KEY,
    }
    if model is None:
        model = default_values["model"]
    if temperature is None:
        temperature = default_values["temperature"]
    if max_tokens is None:
        max_tokens = default_values["max_tokens"]
    if top_p is None:
        top_p = default_values["top_p"]
    if frequency_penalty is None:
        frequency_penalty = default_values["frequency_penalty"]
    if presence_penalty is None:
        presence_penalty = default_values["presence_penalty"]
    if openai_api_key is None:
        openai_api_key = default_values["openai_api_key"]

    openai.api_key = openai_api_key
    if openai_api_key == "":
        raise Exception("No OpenAI API key provided.")
    try:
        response = openai.Completion.create(
            model=model,
            prompt="Extract keywords what is expected from candidate from the following job "
                   "description and return it as a list with comma separation:\n\n" + text,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )
    except Exception as e:
        raise Exception(e)
    text_list = clean_openai_answer_to_list(response["choices"][0]["text"])
    return text_list
