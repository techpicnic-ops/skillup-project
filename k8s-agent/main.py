from ollama import chat
from tools.apply import kubectl_apply

while True:
    question = input("You: ")

    response = chat(
        model="qwen3:1.7b",  #"qwen3:8b"
        messages = [
                    {
                    "role":"system",
                    "content":"""
                    You are a Kubernetes expert.

                    Generate Kubernetes manifests.
                    Always use apiVersion and kind.
                    """
                    },
                    {
                    "role":"user",
                    "content":question
                    }
                ]
    )

    print(response["message"]["content"])

output = kubectl_apply(
    "generated/resource.yaml"
)

print(output)