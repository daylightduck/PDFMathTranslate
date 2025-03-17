import os

from groq import Groq
os.environ["GROQ_API_KEY"] = "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"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Benchmarking the readout of a superconducting qubit for repeated measurements, translate this into arabic please",
        }
    ],
    model="llama-3.3-70b-versatile",
    # model="gemma2-9b-it",
)

print(chat_completion.choices[0].message.content)