from openai import OpenAI

client = OpenAI(
    api_key="OLLAMA",
    base_url="http://localhost:11434/v1",
)

# Pseudo example
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Extract the main content from the given HTML and convert it to Markdown format",
        },
        {
            "role": "user",
            "content": open("reader-lm/pseudo.html", "r").read(),
        },
    ],
    model="reader-lm",
    temperature=0,
)

with open("reader-lm/pseudo_output.md", "w") as f:
    f.write(response.choices[0].message.content)

# Real example

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Extract the main content from the given HTML and convert it to Markdown format",
        },
        {"role": "user", "content": open("reader-lm/test.html", "r").read()},
    ],
    model="reader-lm",
    temperature=0,
)

with open("reader-lm/output.md", "w") as f:
    f.write(response.choices[0].message.content)
