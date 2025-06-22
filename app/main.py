from fastapi import FastAPI, UploadFile, HTTPException, File
from app.models import CommentResponse, ExplanationResponse
from app.code_parser import parse_code
from app.ai_commenter import generate_comments as comment_function
from app.explainer import explain_code

app = FastAPI(title="Code Comment Generator")

@app.post("/generate-comments/", response_model=CommentResponse)
async def generate_comments(file: UploadFile):
    print("Starting generating response...")
    if not file.filename.endswith(".py"):
        raise HTTPException(status_code=400, detail="Only Python files (.py) are supported")
    print("Valid file format")
    content = await file.read()
    code = content.decode('utf-8')
    
    # Process immediately (no Celery)
    print("Started parsing...")
    parsed_elements = parse_code(code)
    print("Parsing completed.")
    commented_code = code

    print("Generating response...")
    for element in parsed_elements:
        comment = comment_function(element['code_snippet'])  
        commented_code = commented_code.replace(
            element['code_snippet'],
            f"# {comment}\n{element['code_snippet']}"
        )
    
    print("Response Generated.")
    return {
        "task_id": "direct",
        "status": "Completed",
        "result": commented_code
    }


@app.post("/explain-code/", response_model=ExplanationResponse)
async def explain(file: UploadFile = File(...)):
    if not file.filename.endswith(".py"):
        raise HTTPException(status_code=400, detail="Only Python files (.py) are supported")
    
    content = await file.read()
    code = content.decode('utf-8')

    print("Generating explanation using LLM...")
    explanation = explain_code(code)
    print("Explanation complete.")
    
    return {
        "task_id": "direct",
        "status": "Completed",
        "result" : {"explanation": explanation}
    }
