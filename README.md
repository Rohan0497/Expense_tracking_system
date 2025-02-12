# 🚀 Expense Management System  

A robust **Expense Management System** consisting of a **FastAPI** backend and a **Streamlit** frontend for seamless tracking and management of expenses. This project is designed for efficiency, scalability, and ease of use, making it suitable for both personal and business expense tracking.

---

## 📁 Project Structure  

```
expense-management-system/
│── backend/        # FastAPI backend server
│── frontend/       # Streamlit frontend application
│── tests/          # Test cases for both backend and frontend
│── requirements.txt # Python dependencies
│── README.md       # Project documentation
```

---

## 🛠️ Setup & Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system
```

### 2️⃣ Install Dependencies  
Make sure you have **Python 3.8+** installed. Then, install the required dependencies:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Start the FastAPI Backend  
Run the **FastAPI** backend server with **Uvicorn**:  
```bash
uvicorn backend.server:app --reload
```
By default, the server runs at **`http://127.0.0.1:8000`**.  
Access the **interactive API documentation** at:  
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

### 4️⃣ Start the Streamlit Frontend  
Run the **Streamlit** frontend application:  
```bash
streamlit run frontend/app.py
```
By default, it runs at **`http://localhost:8501`**.  

---

## 🔍 Features  

✅ **User Authentication** – Secure login/logout mechanism  
✅ **Expense Tracking** – Add, edit, and delete expenses with categories  
✅ **Data Visualization** – Interactive charts for expense analysis  
✅ **RESTful API** – Well-structured API endpoints with FastAPI  
✅ **Scalability** – Modular backend and frontend architecture  
✅ **Automated Tests** – Ensuring reliability of core functionalities  

---

## 🧪 Running Tests  

To ensure the application runs smoothly, execute tests using **pytest**:  
```bash
pytest tests/
```

---

## 📌 API Endpoints  

| Method | Endpoint               | Description               |
|--------|------------------------|---------------------------|
| `GET`  | `/expenses`            | Get all expenses          |
| `POST` | `/expenses`            | Add a new expense         |
| `PUT`  | `/expenses/{id}`        | Update an expense         |
| `DELETE` | `/expenses/{id}`      | Delete an expense         |

Full API documentation is available at **`/docs`** after starting the backend.

---

## 🔥 Tech Stack  

- **Backend:** FastAPI, Uvicorn  
- **Frontend:** Streamlit  
- **Database:** SQLite/PostgreSQL (Configurable)  
- **Testing:** Pytest  
- **Dependency Management:** `pip`  

---

## 💡 Future Enhancements  

🔹 Multi-user support with role-based access  
🔹 Integration with external financial APIs (e.g., Plaid, Stripe)  
🔹 Advanced analytics and AI-driven spending insights  

---

## 🤝 Contributing  

Contributions are welcome! Please follow these steps:  

1. **Fork** the repository  
2. **Create a new branch** for your feature (`git checkout -b feature-name`)  
3. **Commit changes** (`git commit -m "Add new feature"`)  
4. **Push to the branch** (`git push origin feature-name`)  
5. Open a **Pull Request**  

---

## 📜 License  

This project is licensed under the **MIT License**. Feel free to use and modify as needed.

---

## ✨ Contact  

For questions, issues, or feature requests, feel free to reach out via GitHub Issues or email me at **your.email@example.com**.
