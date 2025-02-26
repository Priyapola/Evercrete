# Evercrete

Evercrete is a business management application designed to track **brand purchases, sales, and profit/loss calculations** efficiently.

## 🚀 Features

✅ **Brand & Sales Management**  
- Store brand names and purchase rates in a database.  
- Record sales transactions with brand name, quantity sold, and sold rate.  

✅ **Automated Profit & Loss Calculation**  
- Computes **daily, monthly, and yearly profits** dynamically.  
- Displays **total sales, profits, and losses** in real time.  

✅ **Interactive & User-Friendly UI**  
- Simple, colorful, and easy-to-use interface.  
- Provides graphical reports for better insights.  

✅ **Data Storage & Reporting**  
- Securely stores records in a **SQLite/PostgreSQL/MySQL** database.  
- Users can **access daily, monthly, and yearly reports** easily.  

---

## 🛠 Installation Guide

### **1⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/Evercrete.git
cd Evercrete
```

### **2⃣ Backend Setup (Flask)**
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # (For Windows)
source venv/bin/activate  # (For macOS/Linux)
pip install -r requirements.txt
python app.py
```
✅ Flask backend will start at `http://127.0.0.1:5000/`

---

### **3⃣ Frontend Setup (React.js)**
```bash
cd ../frontend
npm install
npm start

## 📌 API Endpoints

| Endpoint                  | Method | Description |
|---------------------------|--------|-------------|
| `/profit_report?type=daily`   | GET    | Get daily profit report |
| `/profit_report?type=monthly` | GET    | Get monthly profit report |
| `/profit_report?type=yearly`  | GET    | Get yearly profit report |


### 🔗 Connect with Me
📧 Email: `polasatyapriya@gmail.com`  
🔗 GitHub: [https://github.com/Priyapola]  
🔗 LinkedIn: [www.linkedin.com/in/satyapriyapola]  
