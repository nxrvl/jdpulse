from jd_pulse_backend.extraction import clean_openai_answer_to_list


def test_clean_openai_answer_to_list():
    """Test the clean_openai_answer_to_list function."""
    text = (
        "Senior Technical Product Manager, Order Management APIs, merchants, payments, disputes, "
        "integrations, backend engineers, product managers, e-commerce products, "
        "Payment Service Provider (PSP) landscape, API focused products, analytical skills, "
        "data-driven success criteria, product documentation/training."
    )
    text_list = clean_openai_answer_to_list(text)
    print(text)
    print(text_list)
    assert text_list == [
        "Senior Technical Product Manager",
        "Order Management APIs",
        "merchants",
        "payments",
        "disputes",
        "integrations",
        "backend engineers",
        "product managers",
        "e-commerce products",
        "Payment Service Provider (PSP) landscape",
        "API focused products",
        "analytical skills",
        "data-driven success criteria",
        "product documentation/training",
    ]
