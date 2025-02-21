import json

# โหลดข้อมูลจากไฟล์ JSON
with open('Shinchan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ฟังก์ชั่นในการค้นหาคำถาม
def find_faq_answer(question):
    for faq in data["faq"]:
        if question in faq["question"]:
            return faq["answer"]
    return "ไม่พบคำตอบที่ตรงกัน"

# รับคำถามจากผู้ใช้
question = input("ถามคำถาม: ")
answer = find_faq_answer(question)

# แสดงคำตอบ
print("คำตอบ: ", answer)