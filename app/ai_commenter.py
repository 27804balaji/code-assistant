from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

comment_generator = ChatOllama(model="llama2:7b-chat")  

def generate_comments(code):
    prompt = f"Generate Python comments for the following code:\n{code}"
    result = comment_generator.invoke([HumanMessage(content=prompt)])
    return result.content if hasattr(result, 'content') else result
