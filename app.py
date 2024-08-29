from flask import Flask, request, jsonify
from datetime import datetime
from symptom_analysis import diagnose  # นำเข้าฟังก์ชันวินิจฉัยจากไฟล์ symptom_analysis.py

app = Flask(__name__)

@app.route('/api/diagnose', methods=['POST'])
def analyze_symptoms():
    data = request.get_json()
    symptoms = data.get('symptoms', [])
    start_date = data.get('start_date', None)
    
    if start_date:
        try:
            start_date_parsed = datetime.strptime(start_date, '%d/%m/%Y')
        except ValueError:
            return jsonify({'error': 'รูปแบบวันที่ไม่ถูกต้อง กรุณาใช้รูปแบบ dd/mm/yyyy'}), 400
    else:
        start_date_parsed = datetime.now()

    result = diagnose(symptoms, start_date_parsed)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
