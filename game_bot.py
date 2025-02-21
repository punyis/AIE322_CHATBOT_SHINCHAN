import json
import random

# โหลดข้อมูลจากไฟล์ JSON
with open('Shinchan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ดึงคำถามเกมจาก JSON
questions = data["game_questions"]

# ฟังก์ชั่นในการเล่นเกม
def play_game():
    score = 0
    random.shuffle(questions)  # สลับลำดับคำถามเพื่อไม่ให้ซ้ำ
    print("🎮 ยินดีต้อนรับสู่เกมทายคำถามจากชินจัง! 🎮")
    
    for i, q in enumerate(questions):
        print(f"\nคำถามที่ {i+1}: {q['question']}")

        # แสดงตัวเลือก
        for idx, choice in enumerate(q['choices']):
            print(f"{idx + 1}. {choice}")
        
        # ให้ผู้เล่นเลือกคำตอบ
        try:
            user_choice = int(input("เลือกคำตอบ (ใส่หมายเลข): "))
            if q['choices'][user_choice - 1] == q['answer']:
                print("✅ ถูกต้อง!")
                score += 1
            else:
                print(f"❌ ผิด! คำตอบที่ถูกต้องคือ: {q['answer']}")
        except (ValueError, IndexError):
            print("⚠️ กรุณาใส่หมายเลขที่ถูกต้อง!")

    print(f"\n🎉 คุณตอบถูก {score} จาก {len(questions)} คำถาม! 🎉")
    print("ขอบคุณที่เล่นเกมนะครับ! 😊")

# เรียกใช้ฟังก์ชั่น
play_game()