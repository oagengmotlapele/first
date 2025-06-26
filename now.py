from langchain_ollama import OllamaLLM
llm=OllamaLLM(model='qwen:0.5b')
ff=llm.invoke("hello bot")