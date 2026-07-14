import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_requirements(text, prompt_file="prompts/requirement_prompt.txt"):
    """Send requirements text to LLM for analysis."""
    with open(prompt_file, "r") as f:
        base_prompt = f.read()

    full_prompt = f"{base_prompt}\n\nSRS Content:\n{text}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI assistant for requirement analysis."},
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=1500,
            temperature=0.3
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error during analysis: {str(e)}"