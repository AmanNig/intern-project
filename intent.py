from langchain_ollama import ChatOllama
from config import MODEL_NAME

#Connect to your local LLaMA 3 model
llm = ChatOllama(model=MODEL_NAME)

def classify_intent(question: str) -> str:
    prompt = (
   "You are an intent classifier. Your job is to read a user's question and classify it into ONLY ONE of these categories:\n"
    "- yes_no: A question that can be answered with yes or no.\n"
    "- timeline: A question about when, how long, or timeframes.\n"
    "- insight: A question asking for an explanation, reason, or deeper understanding.\n"
    "- guidance: A question seeking advice, recommendation, or next steps.\n"
    "- general: Anything else, including greetings, statements, or unclear intent.\n"
    "\n"
    "Respond with ONLY one of the category names, in all lowercase, and nothing else. Do not include any explanation, punctuation, or extra words.\n"
    "\n"
    "Here are some examples:\n"
    "Q: Will I become an engineer?\n"
    "A: yes_no\n"
    "Q: When will I become an engineer?\n"
    "A: timeline\n"
    "Q: Why do people become engineers?\n"
    "A: insight\n"
    "Q: What should I do to become an engineer?\n"
    "A: guidance\n"
    "Q: Hello there!\n"
    "A: general\n"
    "\n"
    "Classify this question:\n"
    f"Q: {question}\n"
    "A:"
)
    
    response = llm.invoke(prompt)
    intent = response.content.strip().lower()

    valid = {"yes_no", "timeline", "insight", "guidance", "general"}
    return intent if intent in valid else "general"

