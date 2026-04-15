# Hướng dẫn chi tiết kết nối Telegram

## Bước 1: Tạo bot Telegram và lấy Token

### 1.1 Tìm BotFather
1. Mở ứng dụng Telegram trên điện thoại hoặc máy tính
2. Trong thanh tìm kiếm, gõ **@BotFather** (hoặc **BotFather**)
3. Nhấp vào kết quả đầu tiên có dấu xanh (official)

### 1.2 Tạo bot mới
1. Nhấp vào **START** hoặc nhắn tin `/start` để bắt đầu
2. BotFather sẽ hiển thị menu các lệnh
3. Nhắn tin `/newbot` để tạo bot mới
4. BotFather hỏi: "Alright, a new bot. How are we going to call it? Please choose a name for your bot."
5. Nhập tên bot (ví dụ: `Digital Profile Bot`)
6. BotFather hỏi: "Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot."
7. Nhập username (ví dụ: `digital_profile_bot`) - phải kết thúc bằng `bot`
8. Nếu username đã tồn tại, BotFather sẽ báo lỗi và yêu cầu nhập lại
9. Khi thành công, BotFather sẽ gửi thông tin bot và **TOKEN**

### 1.3 Sao chép Token
Token sẽ có dạng: `123456789:ABCDefGHijKLmnoPQRstUVwXYZ`
- Sao chép toàn bộ token này
- **Quan trọng:** Giữ token bí mật, không chia sẻ với ai

## Bước 2: Lấy Chat ID

### Phương pháp 1: Nhận tin nhắn từ bot (Khuyến nghị)

1. Mở bot vừa tạo (tìm username bạn đặt)
2. Nhấp **START** hoặc nhắn tin bất kỳ (ví dụ: "Hello")
3. Mở trình duyệt web
4. Truy cập URL: `https://api.telegram.org/bot[TOKEN]/getUpdates`
   - Thay `[TOKEN]` bằng token bạn vừa sao chép
   - Ví dụ: `https://api.telegram.org/bot123456789:ABCDefGHijKLmnoPQRstUVwXYZ/getUpdates`
5. Trang web sẽ hiển thị JSON response
6. Tìm phần `"chat":{"id":123456789,...}`
7. Số `123456789` chính là **Chat ID** của bạn

### Phương pháp 2: Sử dụng nhóm Telegram

1. Tạo nhóm mới trên Telegram hoặc mở nhóm hiện có
2. Thêm bot vào nhóm:
   - Nhấp vào tên nhóm > **Add members**
   - Tìm username bot và thêm vào
3. Gửi một tin nhắn bất kỳ trong nhóm
4. Truy cập URL: `https://api.telegram.org/bot[TOKEN]/getUpdates`
5. Tìm phần `"chat":{"id":-123456789,...}`
   - Chat ID của nhóm sẽ có dấu `-` ở đầu
6. Sao chép số này (bao gồm dấu `-`)

### Phương pháp 3: Sử dụng Bot khác để lấy Chat ID

#### Bước 3.1: Sử dụng @userinfobot
1. Tìm kiếm và mở `@userinfobot` trên Telegram
2. Nhấp **"START"**
3. Bot sẽ trả về thông tin của bạn, bao gồm **Chat ID**

#### Bước 3.2: Sử dụng @get_id_bot
1. Tìm kiếm `@get_id_bot`
2. Nhấp **"START"**
3. Bot sẽ hiển thị Chat ID của bạn

### Phương pháp 4: Hướng dẫn chi tiết với hình ảnh (Text-based)

#### Bước 4.1: Chuẩn bị
- Đảm bảo bạn đã tạo bot và có TOKEN
- Mở Telegram và trình duyệt web cùng lúc

#### Bước 4.2: Gửi tin nhắn cho bot
1. Trong Telegram, tìm bot của bạn (ví dụ: `@digital_profile_bot`)
2. Mở cuộc trò chuyện
3. Gửi tin nhắn: "test chat id" hoặc bất kỳ gì

#### Bước 4.3: Truy cập API Telegram
1. Mở tab mới trong trình duyệt
2. Nhập URL: `https://api.telegram.org/botYOUR_TOKEN/getUpdates`
3. Thay `YOUR_TOKEN` bằng token thật
4. Nhấn Enter

#### Bước 4.4: Đọc kết quả JSON
1. Bạn sẽ thấy text như:
   ```json
   {"ok":true,"result":[{"update_id":123456789,"message":{"message_id":1,"from":{"id":987654321,"is_bot":false,"first_name":"Your Name","username":"yourusername"},"chat":{"id":987654321,"first_name":"Your Name","username":"yourusername","type":"private"},"date":1640995200,"text":"test chat id"}}]}
   ```
2. Tìm `"chat":{"id":987654321`
3. Số `987654321` là Chat ID

#### Bước 4.5: Test Chat ID
1. Thay vào URL test:
   ```
   https://api.telegram.org/botYOUR_TOKEN/sendMessage?chat_id=987654321&text=Hello
   ```
2. Nếu nhận được "Hello" trên Telegram, Chat ID đúng!

### Lưu ý quan trọng về Chat ID
- **Chat ID cá nhân**: Số dương (ví dụ: 123456789)
- **Chat ID nhóm**: Số âm với dấu `-` (ví dụ: -123456789)
- **Chat ID kênh**: Tương tự nhóm
- Nếu không thấy update, gửi tin nhắn mới cho bot và refresh URL getUpdates

## Bước 3: Cập nhật thông tin vào backend

1. Mở file `app.py` trong thư mục project
2. Tìm dòng:
   ```python
   TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   ```
   Thay bằng:
   ```python
   TELEGRAM_TOKEN = "123456789:ABCDefGHijKLmnoPQRstUVwXYZ"
   ```

3. Tìm dòng:
   ```python
   CHAT_ID = "YOUR_CHAT_ID"
   ```
   Thay bằng:
   ```python
   CHAT_ID = "123456789"  # hoặc "-123456789" nếu là nhóm
   ```

## Bước 4: Cài đặt và chạy backend

### 4.1 Cài đặt dependencies
Mở PowerShell/Terminal và chạy:
```
pip install flask requests
```

### 4.2 Chạy backend
Trong thư mục project, chạy:
```
python app.py
```

Backend sẽ chạy tại `http://localhost:5000`
- Bạn sẽ thấy: `* Running on http://127.0.0.1:5000/`

## Bước 5: Chạy frontend

### 5.1 Mở terminal mới
Mở PowerShell/Terminal khác (để backend vẫn chạy)

### 5.2 Chạy server HTTP
```
python -m http.server 8000
```

### 5.3 Truy cập trang web
Mở trình duyệt và truy cập: `http://localhost:8000`

## Bước 6: Kiểm tra hoạt động

1. Nhấp nút **"Để lại lời nhắn"**
2. Điền tên và lời nhắn
3. Nhấp **"Gửi"**
4. Kiểm tra Telegram - bạn sẽ nhận được tin nhắn!

## Xử lý sự cố thường gặp

### Lỗi "Unauthorized"
- Kiểm tra lại TOKEN có đúng không
- Đảm bảo không có khoảng trắng thừa

### Không nhận được tin nhắn
- Kiểm tra CHAT_ID có đúng không
- Đảm bảo bot đã được thêm vào nhóm (nếu dùng nhóm)
- Gửi tin nhắn cho bot trước khi kiểm tra getUpdates

### Lỗi CORS
- Đảm bảo backend chạy trên port 5000
- Frontend chạy trên port 8000

### Bot không phản hồi
- Đảm bảo đã nhấp START với bot
- Kiểm tra username bot có đúng không

## Bảo mật
- Không commit TOKEN và CHAT_ID lên Git
- Sử dụng biến môi trường cho production
- Chỉ chia sẻ với người đáng tin cậy

## Hỗ trợ thêm
Nếu gặp vấn đề, kiểm tra:
- Console browser (F12 > Console) để xem lỗi
- Terminal chạy backend để xem log lỗi
- Đảm bảo cả backend và frontend đều đang chạy
