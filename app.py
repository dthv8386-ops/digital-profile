from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Thay TELEGRAM_TOKEN và CHAT_ID bằng giá trị của bạn
TELEGRAM_TOKEN = "8689598699:AAFZnv65M1echQF4moiHvX0f2IZ7PbmGNQM"
CHAT_ID = "5513473150"  # ID của bạn hoặc Group ID

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.json
        name = data.get('name')
        message = data.get('message')
        
        if not name or not message:
            return jsonify({'success': False, 'error': 'Tên và lời nhắn là bắt buộc'}), 400
        
        # Tạo tin nhắn
        telegram_message = f"📬 Tin nhắn mới từ {name}:\n\n{message}"
        
        # Gửi đến Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': telegram_message
        }
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return jsonify({'success': True, 'message': 'Tin nhắn đã gửi thành công!'})
        else:
            return jsonify({'success': False, 'error': 'Lỗi khi gửi tin nhắn'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
