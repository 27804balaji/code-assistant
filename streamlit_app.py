# import streamlit as st
# import requests
# from streamlit_ace import st_ace

# st.set_page_config(page_title="Code Comment Generator", layout="wide")

# st.title("💡 Python Code Comment Generator")

# st.markdown("Type your Python code below and click 'Generate Comments'.")

# # Ace Editor for typing Python code
# code_input = st_ace(
#     placeholder="Type your Python code here...",
#     language="python",
#     theme="monokai",
#     key="editor",
#     tab_size=4,
#     show_gutter=True,
#     wrap=False,
#     height=400,
#     auto_update=True
# )

# # Submit button
# if st.button("🚀 Generate Comments"):
#     if not code_input or code_input.strip() == "":
#         st.warning("⚠️ Please type some Python code before submitting.")
#     else:
#         with st.spinner("Processing..."):
#             try:
#                 response = requests.post(
#                     "http://localhost:8000/generate-comments/",
#                     files={"file": ("input.py", code_input)}
#                 )
#                 if response.status_code == 200:
#                     result = response.json()["result"]
#                     st.subheader("📝 Commented Code")
#                     st.code(result, language="python")
#                 else:
#                     st.error("❌ Error from server: " + response.text)
#             except Exception as e:
#                 st.error(f"❌ Failed to connect to backend: {e}")

import streamlit as st
import requests
from streamlit_ace import st_ace

st.set_page_config(page_title="Python Code Assistant", layout="wide")

st.title("🧠 Python Code Assistant")

st.markdown("Type your Python code below. Choose to generate comments or explain the workflow.")

# Ace Editor for typing Python code
code_input = st_ace(
    placeholder="Type your Python code here...",
    language="python",
    theme="monokai",
    key="editor",
    tab_size=4,
    show_gutter=True,
    wrap=False,
    height=400,
    auto_update=True
)

# Buttons in one row
col1, col2 = st.columns(2)

with col1:
    if st.button("💬 Generate Comments"):
        if not code_input or code_input.strip() == "":
            st.warning("⚠️ Please type some Python code before submitting.")
        else:
            with st.spinner("Generating comments..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/generate-comments/",
                        files={"file": ("input.py", code_input)}
                    )
                    if response.status_code == 200:
                        result = response.json()["result"]
                        st.subheader("📝 Commented Code")
                        st.code(result, language="python")
                    else:
                        st.error("❌ Error from server: " + response.text)
                except Exception as e:
                    st.error(f"❌ Failed to connect to backend: {e}")

with col2:
    if st.button("📊 Explain Code & Workflow"):
        if not code_input or code_input.strip() == "":
            st.warning("⚠️ Please type some Python code before submitting.")
        else:
            with st.spinner("Explaining workflow..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/explain-code/",
                        files={"file": ("input.py", code_input)}
                    )
                    print(f"Recieved Code :\n{code_input}")
                    if response.status_code == 200:
                        data = response.json()["result"]
                        st.subheader("🧾 Workflow Explanation")
                        st.text(data["explanation"])
                        if "image_path" in data:
                            st.image(data["image_path"], caption="Workflow Diagram")
                    else:
                        st.error("❌ Error from server: " + response.text)
                except Exception as e:
                    st.error(f"❌ Failed to connect to backend: {e}")
