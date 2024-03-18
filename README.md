
# Pokemon api

# วิธีติดตั้ง
ติดตั้ง Python ลงเครื่อง
[Python](https://www.python.org/downloads/)

เปิด command prompt เลือก file path ที่ต้องการจะเก็บไฟล์ไว้ และเข้าถึงไฟล์ผ่านคำสั่ง cd
```bash
cd filepath
```
clone ไฟล์จาก git ลงเครื่อง
```bash
git clone https://github.com/ArmNonthakon/pokemon_api.git
```
เข้าไปในไฟล์โฟลเดอร์
```bash
cd pokemon_api
```
ติดตั้ง dependency ต่างๆ
```bash
pip install fastapi uvicorn[standard] 
```
run คำสั่ง
```bash
python -m uvicorn main:app --reload
```
run web on port [127.0.0.1:8000](http://127.0.0.1:8000/)


