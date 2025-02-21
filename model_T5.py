from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# โหลดโมเดลและ Tokenizer
model_name = "t5-small"  # สามารถเลือกเป็น t5-base หรือ t5-large ตามขนาดของโมเดล
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# ฟังก์ชั่นในการสร้างคำตอบ
def generate_answer(question, context):
    input_text = f"question: {question} context: {context}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    # การสร้างคำตอบจากโมเดล
    outputs = model.generate(input_ids, max_length=200, num_beams=4, early_stopping=True)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer


