from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

explainer_model = ChatOllama(model="codellama:latest")

def explain_code(code: str) -> str:
    prompt = f"""
You are a helpful assistant. Please explain the following Python code and describe its workflow: {code}
Provide a step-by-step explanation.
"""
    response = explainer_model.invoke([HumanMessage(content=prompt)])
    return response.content if hasattr(response, "content") else str(response)
