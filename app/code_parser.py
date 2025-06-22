import ast

def parse_code(code: str) -> list:
    tree = ast.parse(code)
    elements = []
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            code_snippet = ast.get_source_segment(code, node)
            elements.append({
                'type': type(node).__name__,
                'name': node.name,
                'code_snippet': code_snippet
            })
    
    return elements