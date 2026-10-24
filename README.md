# MarCode

An interactive desktop app for learning Python, with lessons, a built-in code editor, challenges, and local network chat.

[English](#english) · [کوردی](#کوردی) · [فارسی](#فارسی)

<br>

<img width="1616" height="1002" alt="MarCode screenshot" src="https://github.com/user-attachments/assets/28d66011-4228-432d-a02f-ffeb18f5e31c" />

---

## English

MarCode is a desktop application for learning Python from scratch. Each lesson comes with a short explanation, a code example you can edit, and a challenge. You write code, run it inside the app, and check your solution to earn points, so there is nothing else to set up.

### Purpose

MarCode was built with a simple goal: to make learning Python approachable and practical. It is meant for two kinds of people: teachers and mentors who want a ready-made tool for teaching Python in classrooms, and self-learners who want to study at their own pace.

### Customizing the lessons

All lesson content lives in a single file, `shared.py`. Titles, explanations, example code, challenges, hints and translations are all defined there, so you can edit existing lessons or add your own without touching the application code in `start.py`. That makes MarCode easy to adapt to your own course, classroom or teaching style. Each lesson needs a unique `id` and its text in all three languages.

### Features

- Built-in code editor with syntax highlighting
- Run your code and see the output right inside the app
- One challenge per lesson, checked automatically, with a score and visual progress bar
- **LAN Talk (Local Network Chat):** built-in chat room for classrooms and labs. Users on the same network can talk to each other automatically, without setting up IP addresses
- Customizable font family and font sizes from the settings menu
- Seamless language switching between English, Persian and Kurdish (Sorani) without restarting
- Your progress, font settings and language choice are saved between sessions
- Dark interface built with CustomTkinter

### Lessons

29 lessons in 7 sections:

1. Getting Started
2. Variables and Data
3. Conditions
4. Loops
5. Data Structures
6. Functions
7. Modules

### Requirements

- Windows
- Python 3.8 or newer (only if running from source)
- `customtkinter`

### Installation

**Option 1: Installer (recommended)**

Download and run `MarCode_Setup.exe` from the [Releases](https://github.com/RamyarHasanpour/marcode/releases) page. No Python installation is required.

**Option 2: Run from source**

```bash
git clone https://github.com/RamyarHasanpour/marcode.git
cd marcode
pip install customtkinter
python start.py
```

On the first launch, the app creates a folder named `MarcodeProject` on one of your drives and stores your progress and font settings there.

### Project structure

| File | Description |
| --- | --- |
| `start.py` | The app window, code editor, challenge checking, font settings and LAN chat (UDP/TCP sockets) |
| `shared.py` | Lesson content, translations and interface settings |
| `M_Logo.ico` | Application icon |

---

<div dir="rtl">

## کوردی

مارکۆد (MarCode) بەرنامەیەکی دێسکتۆپە بۆ فێربوونی پایتۆن لە سفرەوە. هەر وانەیەک شرۆڤەیەکی کورت، نموونەیەکی کۆد کە دەتوانیت دەستکاری بکەیت، و ئاڵنگارییەکی تێدایە. کۆدەکە دەنووسیت، لەناو بەرنامەکە جێبەجێی دەکەیت و بە چارەسەرکردنی ئاڵنگارییەکە خاڵ وەردەگریت؛ پێویستت بە هیچ بەرنامەیەکی تر نییە.

### ئامانج

مارکۆد بە ئامانجێکی سادە دروستکراوە: ئاسان و کارامەکردنی فێربوونی پایتۆن. بۆ دوو جۆر کەس گونجاوە: مامۆستا و ڕێنمایکارەکان کە ئامرازێکی ئامادەیان پێویستە بۆ فێرکردنی پایتۆن لە پۆلدا، و ئەوانەی دەیانەوێت بە خۆیان و بە خێرایی خۆیان پایتۆن فێر ببن.

### گۆڕینی وانەکان

هەموو ناوەڕۆکی وانەکان لە یەک فایلدایە: `shared.py`. ناونیشان، شرۆڤە، نموونەی کۆد، ئاڵنگاری، ڕێنمایی و وەرگێڕانەکان هەموویان لەوێ دیاریکراون، بۆیە دەتوانیت وانەکان دەستکاری بکەیت یان وانەی نوێ زیاد بکەیت بەبێ ئەوەی دەست بە کۆدی بەرنامەکە لە `start.py` بدەیت. ئەمە وا دەکات مارکۆد بە ئاسانی لەگەڵ کۆرس، پۆل یان شێوازی وانەوتنەوەی خۆتدا بگونجێت. هەر وانەیەک پێویستی بە `id`ی تایبەت و دەقی هەر سێ زمانەکە هەیە.

### تایبەتمەندییەکان

- ئیدیتۆری کۆدی ناوخۆیی لەگەڵ ڕەنگکردنی وشە سەرەکییەکانی پایتۆن
- جێبەجێکردنی کۆد و پیشاندانی دەرەنجام لەناو خودی بەرنامەکە
- ئاڵنگارییەک بۆ هەر وانەیەک کە بە شێوەی خۆکار دەپشکنرێت لەگەڵ نیشاندەری پێشکەوتن (Progress Bar)
- **گفتوگۆی تۆڕی ناوخۆیی (LAN Talk):** بەشی چاتی ناوخۆیی بۆ پۆل و تاقیگەکان؛ بەکارهێنەرانی سەر هەمان تۆڕ دەتوانن بەبێ ڕێکخستنی IP ڕاستەوخۆ پەیام بۆ یەکتر بنێرن
- بەشی ڕێکخستنەکان (Settings) بۆ گۆڕینی جۆری فۆنت و قەبارەی نووسینەکان
- گۆڕینی ڕاستەوخۆی زمانی بەرنامەکە لە نێوان ئینگلیزی، فارسی و کوردی بەبێ داخستنەوەی بەرنامە
- هەڵگرتنی پێشکەوتن، ڕێکخستنی فۆنت و زمانی هەڵبژێردراو لە نێوان جارەکانی کارپێکردندا
- ڕووکارێکی تاریک کە بە CustomTkinter دروستکراوە

### وانەکان

٢٩ وانە لە ٧ بەشدا:

1. دەستپێکردن
2. گۆڕاوەکان و دراوەکان
3. پێکهاتە مەرجدارەکان
4. بازنەکانی دووبارەبوونەوە
5. پێکهاتەکانی دراوە
6. فانکشنەکان
7. مۆدیوڵەکان

### پێداویستییەکان

- ویندۆز
- پایتۆنی ٣.٨ یان نوێتر (ئەگەر لە سۆرس کۆدەوە کاری پێدەکەیت)
- کتێبخانەی `customtkinter`

### دابەزاندن و کارپێکردن

**ڕێگەی یەکەم: فایلی دامەزراندن (پێشنیارکراو)**

فایلی `MarCode_Setup.exe` لە بەشی [Releases](https://github.com/RamyarHasanpour/marcode/releases) دابەزێنە و دایبمەزرێنە (پێویستی بە پایتۆن نییە).

**ڕێگەی دووەم: لە ڕێگەی سۆرس کۆدەوە**

```bash
git clone https://github.com/RamyarHasanpour/marcode.git
cd marcode
pip install customtkinter
python start.py
```

لە یەکەم جار کارپێکردندا، بەرنامەکە فۆڵدەرێک بە ناوی `MarcodeProject` لەسەر یەکێک لە درایڤەکانت دروست دەکات و پێشکەوتن و ڕێکخستنەکانت لەوێ هەڵدەگرێت.

</div>

---

<div dir="rtl">

## فارسی

مارکد (MarCode) یک برنامه دسکتاپ برای یادگیری پایتون از صفر است. هر درس شامل یک توضیح کوتاه، یک کد نمونه قابل ویرایش و یک چالش است. کد را می‌نویسید، همان‌جا اجرا می‌کنید و با حل چالش امتیاز می‌گیرید؛ نیازی به نصب هیچ محیط توسعه دیگری نیست.

### هدف پروژه

مارکد با یک هدف ساده ساخته شده است: آسان و کاربردی کردن یادگیری پایتون. این برنامه برای دو گروه مناسب است: مدرس‌ها و مربی‌هایی که به ابزاری آماده برای آموزش پایتون در کلاس نیاز دارند، و کسانی که می‌خواهند خودشان و با سرعت خودشان پایتون یاد بگیرند.

### شخصی‌سازی درس‌ها

تمام محتوای درس‌ها در یک فایل قرار دارد: `shared.py`. عنوان، توضیح، کد نمونه، چالش، راهنمایی و ترجمه‌ها همه همان‌جا تعریف شده‌اند؛ بنابراین می‌توانید بدون دست زدن به کد اصلی برنامه در `start.py`، درس‌های موجود را ویرایش کنید یا درس جدید اضافه کنید. همین باعث می‌شود مارکد را بتوان به‌راحتی با دوره، کلاس یا سبک تدریس خودتان هماهنگ کرد. هر درس به یک `id` منحصربه‌فرد و متن هر سه زبان نیاز دارد.

### امکانات

- ادیتور کد داخلی با رنگی شدن کلمات کلیدی پایتون
- اجرای کد و نمایش خروجی داخل خود برنامه
- یک چالش برای هر درس که به‌صورت خودکار بررسی می‌شود، همراه با نوار پیشرفت (Progress Bar)
- **گفتگوی شبکه محلی (LAN Talk):** سیستم چت داخلی برای کلاس‌ها و کارگاه‌ها؛ کاربران متصل به یک شبکه می‌توانند بدون نیاز به تنظیم دستی IP، به‌طور خودکار با هم گفتگو کنند
- منوی تنظیمات (Settings) برای تغییر نوع فونت و اندازه متن‌ها
- تغییر آنی زبان برنامه بین انگلیسی، فارسی و کوردی (سورانی) بدون نیاز به بستن برنامه
- ذخیره پیشرفت، تنظیمات فونت و زبان انتخاب‌شده بین دفعات اجرا
- ظاهر تیره ساخته‌شده با CustomTkinter

### سرفصل‌ها

۲۹ درس در ۷ بخش:

1. شروع کار
2. متغیرها و داده‌ها
3. ساختارهای شرطی
4. حلقه‌های تکرار
5. ساختارهای داده
6. توابع
7. ماژول‌ها

### پیش‌نیازها

- ویندوز
- پایتون ۳.۸ یا جدیدتر (در صورت اجرا از روی سورس کد)
- کتابخانه `customtkinter`

### نصب و اجرا

**روش اول: فایل نصبی (پیشنهادی)**

فایل `MarCode_Setup.exe` را از بخش [Releases](https://github.com/RamyarHasanpour/marcode/releases) دانلود و نصب کنید (نیازی به نصب بودن پایتون نیست).

**روش دوم: اجرا از روی سورس کد**

```bash
git clone https://github.com/RamyarHasanpour/marcode.git
cd marcode
pip install customtkinter
python start.py
```

در اولین اجرا، برنامه پوشه‌ای به نام `MarcodeProject` را روی یکی از درایوهای شما می‌سازد و پیشرفت و تنظیمات فونت شما را آنجا ذخیره می‌کند.

</div>
