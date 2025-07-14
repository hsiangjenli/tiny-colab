import mlflow

system_prompt = mlflow.genai.register_prompt(
    name="chatbot_prompt",
    template="You are a chatbot that can answer questions about IT. Answer this question: {{question}}",
    commit_message="Initial version of chatbot",
)