import ollama

def ask_ai(prompt):

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def extract_bank_data(document_text):

    prompt = f"""
    Extract the following fields from the document.

    Return ONLY JSON.

    Fields:
    - customer_name
    - loan_amount
    - interest_rate

    Document:
    {document_text}
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def fill_template(document_text):

    prompt = f"""
    Analyze the document and extract important information.

    Return ONLY JSON.

    Fields:
    - customer_name
    - account_number
    - loan_amount
    - interest_rate
    - loan_tenure

    Document:
    {document_text}
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

