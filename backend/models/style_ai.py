from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_design(prompt):

    fashion_prompt = f"Create a fashion outfit design: {prompt}. Include colors and style."

    result = generator(
    fashion_prompt,
    max_new_tokens=80,          
    num_return_sequences=1
)


    return result[0]["generated_text"]
