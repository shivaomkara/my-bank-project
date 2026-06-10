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

Return ONLY valid JSON.

Fields:
- customer_name
- loan_amount
- interest_rate

If a field is not found, return null.

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
Return ONLY valid JSON.

Do not explain.
Do not use markdown.
Do not use triple backticks.

Extract these fields:
- customer_name
- account_number
- loan_amount
- interest_rate
- loan_tenure

If a field is not found, return null.

Example Output:

{{
    "customer_name": "Rajesh Kumar Sharma",
    "account_number": "3721005868941200",
    "loan_amount": 500000,
    "interest_rate": 10.5,
    "loan_tenure": 36
}}

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
def ask_document_question(document_text, question):

    prompt = f"""
You are a banking document assistant.

Answer the question ONLY based on the document.

Document:
{document_text}

Question:
{question}
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
    