# Hướng dẫn Deploy Profile Online

## Vấn đề hiện tại
Profile hiện tại chỉ chạy local trên máy của bạn (`http://localhost:8000`). Bạn bè không thể truy cập được vì đây là server cục bộ.

## Deploy lên GitHub Pages (Khuyến nghị)

### Bước 1: Chuẩn bị GitHub Repository
1. Đăng nhập GitHub.com
2. Click "New repository"
3. Đặt tên: `digital-profile` (hoặc tên bất kỳ)
4. Chọn **Public** (để miễn phí)
5. **Không** check "Add a README file"
6. Click "Create repository"

### Bước 2: Push code lên GitHub
Code đã được commit local. Bây giờ:

1. Sao chép URL repository (ví dụ: `https://github.com/yourusername/digital-profile.git`)

2. Chạy lệnh sau (thay `yourusername` và `digital-profile` bằng tên thật):
```bash
git remote add origin https://github.com/yourusername/digital-profile.git
git push -u origin main
```

### Bước 3: Kích hoạt GitHub Pages
1. Vào repository trên GitHub
2. Click tab "Settings"
3. Cuộn xuống "Pages" (trái sidebar)
4. Ở "Source", chọn "Deploy from a branch"
5. Branch: `main`, folder: `/ (root)`
6. Click "Save"

### Bước 4: Truy cập link
Sau 1-2 phút, link sẽ là: `https://yourusername.github.io/digital-profile/`

**Ví dụ:** Nếu username là `johndoe`, link sẽ là `https://johndoe.github.io/digital-profile/`

## Các giải pháp khác

### Vercel (Nếu muốn serverless)
1. Đăng ký Vercel.com (miễn phí)
2. Connect GitHub
3. Import project
4. Deploy tự động

### Heroku (Nếu cần backend Flask)
1. Đăng ký Heroku.com
2. Install Heroku CLI
3. `heroku create`
4. Push code
5. Link: `https://your-app-name.herokuapp.com`

## So sánh chi phí

| Platform | Chi phí | Bandwidth | Storage | Backend Support |
|----------|---------|-----------|---------|-----------------|
| GitHub Pages | Miễn phí | 100GB/tháng | 1GB | Không |
| Vercel | Miễn phí | 100GB/tháng | Không giới hạn | Serverless |
| Netlify | Miễn phí | 100GB/tháng | 100GB | Serverless |
| Heroku | Free tier, sau $7/tháng | 2TB/tháng | 512MB | Full backend |

## Lưu ý quan trọng
- **Telegram integration**: Vì GitHub Pages chỉ static, form sẽ tự động fallback gửi trực tiếp đến Telegram (đã code sẵn)
- **HTTPS**: Tất cả platforms trên đều có HTTPS tự động
- **Tốc độ**: GitHub Pages rất nhanh với CDN global</content>
<parameter name="filePath">c:\Users\Admin\Downloads\BaiTapDauTien\DEPLOY_GUIDE.md