# Web Content Q&A Tool

A powerful web-based tool designed for content ingestion and Q&A directly from web pages. With an intuitive interface and reliable answer generation, this tool ensures precise results based strictly on provided URLs.

---

## 🚀 Features
- **Accurate Q&A**: Get clear answers grounded in the content you provide.
- **Content Summarization**: Condenses lengthy content into concise insights.
- **User-Friendly Interface**: Simple design with easy navigation.
- **Enhanced Extraction**: Focuses on main text areas for improved accuracy.

---

## 🚀 Demo 
[![Web Content Q&A Tool Video Demo](https://img.youtube.com/vi/y1kuaVwzTnY/0.jpg)](https://www.youtube.com/watch?v=y1kuaVwzTnY)

---
## 📂 Project Structure
```
web_content_qa
├── backend
│   ├── app.py
│   ├── content_handler.py
│   ├── requirements.txt
│
├── frontend
│   ├── public
│   │   └── index.html
│   ├── src
│   │   ├── App.js
│   │   ├── index.js
│   │   └── styles.css
│   ├── package.json
│
└── .gitignore
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository
```
git clone https://github.com/your-username/web-content-qa.git
cd web-content-qa
```

### Step 2: Backend Setup
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Mac/Linux
   .\venv\Scripts\activate    # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   python app.py
   ```

### Step 3: Frontend Setup
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend server:
   ```bash
   npm start
   ```
4. Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 📋 Usage Guide

### Ingest Content
1. Enter one or more URLs in the text area (comma-separated).
2. Click the **"Ingest Content"** button.
- **Success Message:** `"Content ingested successfully!"`

### Ask a Question
1. Enter your question in the input field.
2. Click the **"Get Answer"** button.
- **Answer Displayed:** With **confidence scores** for accuracy.

### Summarize Content
1. Click the **"Summarize Content"** button.
- **Summary Displayed:** A concise overview of the content.

---

## 🌐 Sample URLs for Testing
- [Wikipedia: Flask (Web Framework)](https://en.wikipedia.org/wiki/Flask_\(web_framework\))
- [Real Python: Python Exceptions](https://realpython.com/python-exceptions/)
- [MDN Web Docs: JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)

---

## 🔎 Important Notes
- Ensure the **backend** is running before starting the **frontend**.
- URLs with clear text content yield the best results.
- Rephrasing your question may improve results for shorter content.

---

## 🌍 Deployment (Optional)
To deploy on **Render**, **Vercel**, or **Netlify**:
- Add `"proxy": "http://localhost:5000"` in `frontend/package.json` for local testing.
- For production, update Axios URLs to match your deployed backend URL.

---

## 🤝 Contribution
Contributions are welcome! Follow these steps:
1. Fork the repo.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push the branch: `git push origin feature-name`.
5. Open a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📧 Contact
For questions or feedback, feel free to reach out:
- 📨 **mohdazam3131@gmail.com**
- 🌐 **https://www.linkedin.com/in/mohdazam3131/**

