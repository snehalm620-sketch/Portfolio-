# 🚀 Complete Setup Guide for Doraemon AI

## Option 1: Quick Start (Windows, Mac, Linux)

### Step 1: Install Python
- Download from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Step 2: Clone Repository
```bash
git clone https://github.com/snehalm620-sketch/Portfolio-.git
cd Portfolio-
```

### Step 3: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run Backend
```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

### Step 6: Open Frontend
- Open `index.html` in your web browser
- Or use: `python -m http.server 8000` and visit `http://localhost:8000`

---

## Option 2: Using Command Line (Terminal Mode)

If you prefer using Doraemon AI from the command line:

```bash
python doraemon_ai.py
```

Then follow the interactive prompts.

---

## Option 3: Docker Setup

### Prerequisites
- Install Docker from https://www.docker.com/

### Steps
```bash
# Build image
docker build -t doraemon-ai .

# Run container
docker run -p 5000:5000 doraemon-ai

# Open browser to http://localhost:5000
```

---

## 🎯 Using the Web Interface

1. **Start the backend** (Terminal 1):
   ```bash
   python app.py
   ```

2. **Open frontend** (Terminal 2 - optional):
   ```bash
   python -m http.server 8000
   ```

3. **Open browser**:
   - Option A: Direct file - Open `index.html` in browser
   - Option B: Local server - Visit `http://localhost:8000`

4. **Chat with Doraemon**:
   - Enter your name
   - Click "Start Chat"
   - Type your questions/problems
   - Use special buttons for gadgets and goodbye

---

## 🔧 API Testing

### Using cURL

```bash
# Start chat
curl -X POST http://localhost:5000/api/chat/start \
  -H "Content-Type: application/json" \
  -d '{"user_name":"Alice","session_id":"alice"}'

# Send message
curl -X POST http://localhost:5000/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{"session_id":"alice","message":"I have homework"}'

# Get gadget
curl http://localhost:5000/api/chat/gadget?session_id=alice

# Health check
curl http://localhost:5000/api/health
```

### Using Postman

1. Download Postman from https://www.postman.com/
2. Import the endpoints above
3. Test each endpoint

### Using Python Requests

```python
import requests
import json

BASE_URL = "http://localhost:5000/api"

# Start chat
response = requests.post(f'{BASE_URL}/chat/start',
    json={"user_name": "Alice", "session_id": "alice"})
print(json.dumps(response.json(), indent=2))

# Send message
response = requests.post(f'{BASE_URL}/chat/message',
    json={"session_id": "alice", "message": "How do I study for exams?"})
print(json.dumps(response.json(), indent=2))
```

---

## 📊 Project Architecture

```
Frontend (index.html)
        ↓
    Browser (JavaScript/Fetch API)
        ↓
    Flask Backend (app.py)
        ↓
    Doraemon AI Logic (doraemon_ai.py)
        ↓
    Response back to Frontend
```

---

## ⚠️ Troubleshooting

### Problem: Port 5000 already in use

**Solution 1**: Kill the process
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :5000
kill -9 <PID>
```

**Solution 2**: Use different port
```bash
# Edit app.py last line:
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

### Problem: CORS error in browser

**Solution**: Make sure backend is running and CORS is enabled in `app.py` (already done)

```python
CORS(app)  # This line is already there
```

---

### Problem: Module not found (e.g., Flask)

**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

---

### Problem: Python command not recognized

**Solution**: 
- Ensure Python is in PATH
- Use `python3` instead of `python` (Mac/Linux)
- Reinstall Python with "Add to PATH" checked

---

## 🌐 Accessing from Other Devices

### Same Network (LAN)
1. Find your computer's IP:
   ```bash
   # Windows
   ipconfig
   # Look for "IPv4 Address"
   
   # Mac/Linux
   ifconfig
   # Look for "inet" under active connection
   ```

2. From another device on same network:
   ```
   http://YOUR_IP:5000
   http://YOUR_IP:8000
   ```

### Internet (Remote Access)
Use services like:
- ngrok: `ngrok http 5000`
- Heroku, AWS, Google Cloud, etc.

---

## 📱 Mobile Access

The web interface is responsive and works on:
- Phones (iOS/Android)
- Tablets
- Desktop computers

Just open the URL on your mobile device!

---

## 🎓 Learning Resources

- **Flask Docs**: https://flask.palletsprojects.com/
- **JavaScript Fetch API**: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- **REST API Design**: https://restfulapi.net/
- **Python Guide**: https://docs.python.org/3/

---

## 📝 Environment Configuration

Create `.env` file for custom settings:

```env
FLASK_ENV=development
FLASK_DEBUG=True
API_PORT=5000
```

Then load in `app.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
PORT = os.getenv('API_PORT', 5000)
```

---

## 🚢 Production Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app.py
```

### Using Heroku
```bash
# Login and create app
heroku login
heroku create your-app-name

# Deploy
git push heroku main
```

### Using Google Cloud Run
```bash
gcloud run deploy doraemon-ai \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## ✅ Verification Checklist

- [ ] Python installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Backend running (`python app.py`)
- [ ] Frontend accessible (index.html or localhost:8000)
- [ ] Can chat with Doraemon
- [ ] Gadget button works
- [ ] Goodbye button works

---

## 🆘 Need Help?

1. Check the README.md for API documentation
2. Check error messages in terminal
3. Visit GitHub Issues: https://github.com/snehalm620-sketch/Portfolio-/issues
4. Check browser console (F12) for frontend errors

---

## 🎉 You're Ready!

Enjoy chatting with Doraemon AI! 🤖✨

Made with ❤️ by Snehal M
