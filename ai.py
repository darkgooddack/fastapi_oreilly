from fastapi import FastAPI
from transformers import (AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig)

app = FastAPI()

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


@app.get("/ai")
def prompt(line: str) -> str:
    tokens = tokenizer(line, return_tensors="pt", padding=True, truncation=True)

    outputs = model.generate(
        **tokens,
        max_length=512,
        num_beams=5,  # Количество пучков для поиска
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        do_sample=True
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return result

