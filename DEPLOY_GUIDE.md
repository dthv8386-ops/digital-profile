# Hướng dẫn Deploy Profile Online

## Vấn đề hiện tại
Profile hiện tại chỉ chạy local trên máy của bạn (`http://localhost:8000`). Bạn bè không thể truy cập được vì đây là server cục bộ.

## Các giải pháp deploy online

### 1. GitHub Pages (Khuyến nghị - Miễn phí, Đơn giản)
**Chi phí:** Miễn phí hoàn toàn  
**Ưu điểm:**
- Hoàn toàn miễn phí
- Dễ setup (chỉ cần GitHub account)
- Tự động deploy khi push code
- HTTPS tự động
- Tốc độ nhanh (CDN của GitHub)

**Nhược điểm:**
- Chỉ hỗ trợ static sites (HTML/CSS/JS)
- Không thể chạy backend Python/Flask
- Giới hạn 1GB storage, 100GB bandwidth/tháng

**Cách deploy:**
1. Tạo repository trên GitHub (public)
2. Push code lên repo
3. Vào Settings > Pages > Source: Deploy from a branch > Branch: main
4. Link sẽ là: `https://[username].github.io/[repo-name]/`

### 2. Vercel (Miễn phí, Linh hoạt)
**Chi phí:** Miễn phí cho hobby projects  
**Ưu điểm:**
- Miễn phí với giới hạn hợp lý
- Deploy tự động từ GitHub
- Hỗ trợ static sites và serverless functions
- Tốc độ rất nhanh
- Preview deployments cho mỗi PR

**Nhược điểm:**
- Free tier có giới hạn bandwidth (100GB/tháng)
- Serverless functions có execution time limit
- Có thể phức tạp hơn GitHub Pages nếu cần backend

**Cách deploy:**
1. Kết nối GitHub với Vercel
2. Import project
3. Deploy tự động

### 3. Netlify (Miễn phí, Tương tự Vercel)
**Chi phí:** Miễn phí cho basic plans  
**Ưu điểm:**
- Miễn phí với 100GB bandwidth/tháng
- Deploy từ GitHub/GitLab
- Form handling built-in
- Preview deployments
- Tốc độ tốt

**Nhược điểm:**
- Free tier giới hạn functions invocations
- Không mạnh bằng Vercel cho serverless

### 4. Heroku/Render (Cho full-stack)
**Chi phí:** Free tier có sẵn, sau đó ~$7/tháng  
**Ưu điểm:**
- Chạy được full backend (Flask + database nếu cần)
- Sleep after inactivity (có thể wake up chậm)
- Hỗ trợ nhiều ngôn ngữ

**Nhược điểm:**
- Free tier sleep sau 30 phút không dùng
- Setup phức tạp hơn
- Chi phí cao hơn khi scale
- Tốc độ khởi động chậm khi sleep

## Khuyến nghị cho project này

**GitHub Pages** là lựa chọn tốt nhất vì:
- Profile của bạn chủ yếu là static (HTML/CSS/JS)
- Telegram integration có thể fallback trực tiếp từ frontend
- Đơn giản và miễn phí

Nếu muốn backend Flask chạy online, dùng **Render** hoặc **Railway** (~$5-7/tháng).

Bạn muốn tôi hướng dẫn deploy bằng cách nào?</content>
<parameter name="filePath">c:\Users\Admin\Downloads\BaiTapDauTien\DEPLOY_GUIDE.md