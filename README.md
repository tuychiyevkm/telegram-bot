# 🤖 Telegram Echo Bot

**Telegram Echo Bot** — foydalanuvchi yuborgan barcha turdagi xabar va media fayllarni avtomatik qaytaruvchi bot.  
`python-telegram-bot v13.15` va `Python 3.11.6` asosida yozilgan.

---

## ✨ Xususiyatlari
- 📄 Matn xabarlarini qaytaradi
- 🖼 Rasm (`photo`), 📹 video (`video`), 🔊 ovoz (`voice`), 🎵 audio (`audio`) fayllarni qaytaradi
- 🎬 Animatsiya (GIF), 🎭 sticker, 📷 video note (dumaloq video) obyektlarini qaytaradi
- 📇 Kontakt, 📍 manzil (`location`), 🎲 zar (`dice`) obyektlarini qaytaradi
- 📂 Hujjatlar (PDF, DOCX, ZIP va boshqalar)ni qaytaradi

---

## 🛠 Texnologiyalar
- **Python**: 3.11.6  
- **Kutubxona**: [python-telegram-bot](https://python-telegram-bot.org/) `v13.15`

---

## 🚀 O‘rnatish va ishga tushirish

1. **Virtual muhit yaratish va faollashtirish**
   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

2. **Kerakli kutubxonalarni o‘rnatish**
   ```bash
   pip install python-telegram-bot==13.15
   ```

3. **Token sozlash**  
   `main.py` ichidagi joyga o‘zingizning **Telegram Bot Token** ni yozing.

4. **Botni ishga tushirish**
   ```bash
   python main.py
   ```

---

## 📂 Funksiya nomlari
```
handle_start, handle_help, handle_echo, echo_photo, echo_contact, echo_video, echo_sticker, echo_video_note, echo_animation, echo_location, echo_dice, echo_document, echo_voice, echo_audio
```

---

## 📜 Litsenziya
Bu loyiha **MIT License** asosida tarqatiladi.