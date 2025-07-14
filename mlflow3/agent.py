from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import mlflow

system_prompt = mlflow.genai.register_prompt(
    name="chatbot_prompt",
    template="You are a chatbot that can answer questions about IT. Answer this question: {{question}}",
    commit_message="Initial version of chatbot",
)

prompt = ChatPromptTemplate.from_template(system_prompt.to_single_brace_format())

print(prompt)
chain = prompt | ChatOpenAI(temperature=0.7, model="gpt-4.1-nano-2025-04-14") | StrOutputParser()
question = "What is MLflow?"
print(chain.invoke({"question": question}))
