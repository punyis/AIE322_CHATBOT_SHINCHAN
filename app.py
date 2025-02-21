from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# โหลดข้อมูลจากไฟล์ JSON
with open('Shinchan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ฟังก์ชั่นในการค้นหาคำถามจากไฟล์ JSON
def find_faq_answer(question):
    for faq in data["faq"]:
        if question in faq["question"]:
            return faq["answer"]
    return "ไม่พบคำตอบที่ตรงกัน"

# ฟังก์ชั่นในการเล่นเกม
# ดึงคำถามเกมจาก JSON
game_questions = data["game_questions"]
def play_game():
    score = 0
    random.shuffle(game_questions)  # สลับลำดับคำถามเพื่อไม่ให้ซ้ำ
    print("🎮 ยินดีต้อนรับสู่เกมทายคำถามจากชินจัง! 🎮")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']
    bot_response = find_faq_answer(user_message)
    return jsonify({'response': bot_response})

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/get_questions', methods=['GET'])
def get_questions():
    questions = random.sample(data["game_questions"], 5)  # สุ่มคำถาม 5 ข้อ
    # สร้างรูปแบบข้อมูลคำถามพร้อมตัวเลือก
    formatted_questions = []
    for question in questions:
        formatted_questions.append({
            "question": question["question"],
            "choices": question["choices"],  # ตัวเลือกที่มี
            "answer": question["answer"]  # คำตอบที่ถูกต้อง
        })
    return jsonify(formatted_questions)

@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    user_answers = request.json.get('answers', [])
    questions = request.json.get('questions', [])
    
    score = 0
    for i in range(len(questions)):
        if user_answers[i] == questions[i]['answer']:
            score += 1
    
    return jsonify({'score': score, 'total': len(questions)})

if __name__ == "__main__":
    app.run(debug=True)
