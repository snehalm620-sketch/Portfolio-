# 🤖 Doraemon AI - Your Friendly Robot Assistant

A helpful AI companion inspired by Doraemon that provides friendly advice and assistance using Python and Flask!

## ✨ Features

- 🎯 **Smart Problem Solving** - Get contextual advice for homework, work, learning, coding, creativity, and more
- 💬 **Friendly Conversations** - Warm, encouraging responses with fun emoji and personality
- 🎨 **Beautiful Web Interface** - Modern, responsive chatbot UI
- 🔧 **REST API Backend** - Flask-based API for easy integration
- 📚 **Multiple Advice Categories** - Homework, Work, Learning, Coding, Creative, Time Management, Motivation
- 🎁 **AI Gadget Suggestions** - Random AI tool recommendations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/snehalm620-sketch/Portfolio-.git
   cd Portfolio-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the backend server**
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`

4. **Open the frontend**
   - Simply open `index.html` in your web browser
   - Or use a local server: `python -m http.server 8000`
   - Then visit `http://localhost:8000`

## 📚 Project Structure

```
Portfolio-/
├── doraemon_ai.py      # Core Doraemon AI logic and conversation engine
├── app.py              # Flask REST API backend
├── index.html          # Frontend web interface
├── requirements.txt    # Python dependencies
├── SETUP.md           # Detailed setup guide
└── README.md          # This file
```

## 🌐 API Endpoints

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. **Start Chat Session**
```
POST /api/chat/start
Content-Type: application/json

{
  "user_name": "Your Name",
  "session_id": "unique_session_id"
}

Response:
{
  "status": "success",
  "session_id": "Your_Name",
  "message": "Greeting message from Doraemon",
  "user_name": "Your Name"
}
```

#### 2. **Send Message**
```
POST /api/chat/message
Content-Type: application/json

{
  "session_id": "Your_Name",
  "message": "Your question or problem"
}

Response:
{
  "status": "success",
  "message": "Doraemon's response",
  "type": "response"
}
```

#### 3. **Get AI Gadget Suggestion**
```
GET /api/chat/gadget?session_id=Your_Name

Response:
{
  "status": "success",
  "message": "Gadget suggestion from Doraemon"
}
```

#### 4. **End Chat Session**
```
POST /api/chat/goodbye
Content-Type: application/json

{
  "session_id": "Your_Name"
}

Response:
{
  "status": "success",
  "message": "Farewell message",
  "session_closed": true
}
```

#### 5. **Health Check**
```
GET /api/health

Response:
{
  "status": "healthy",
  "timestamp": "Now",
  "active_sessions": 2
}
```

## 💻 Frontend Features

### Web Interface
- Clean, modern design with gradient colors
- Real-time chat messaging
- Responsive layout (mobile-friendly)
- Special buttons for gadget suggestions and goodbye
- Smooth animations and transitions
- Auto-scrolling to latest messages

### How to Use
1. Enter your name and click "Start Chat"
2. Type your question or problem
3. Doraemon provides helpful advice
4. Click "🎯 Get Gadget" for AI tool suggestions
5. Click "👋 Say Goodbye" to end the chat

## 🎯 Advice Categories

Doraemon can help with:
- **Homework** - Study tips and learning strategies
- **Work** - Productivity and professional guidance
- **Learning** - Education and skill development advice
- **Coding** - Programming tips and best practices
- **Creative** - Inspiration for creative projects
- **Time Management** - Organizing and saving time
- **Motivation** - Encouragement and stress relief

## 🔧 Backend Architecture

### Flask Application Features
- **CORS Enabled** - For frontend-backend communication
- **Session Management** - Multiple concurrent user sessions
- **Error Handling** - Comprehensive error responses
- **Type Safety** - Proper HTTP status codes
- **RESTful Design** - Clean API structure

### Doraemon AI Class
- Problem analysis and keyword matching
- Contextual advice generation
- Mood and personality management
- Gadget suggestion system
- Randomized responses for variety

## 📦 Dependencies

```
Flask==2.3.3           # Web framework
Flask-CORS==4.0.0      # Cross-Origin Resource Sharing
Python-dotenv==1.0.0   # Environment variables
Gunicorn==21.2.0       # Production server
```

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app.py
```

### Docker Support (Optional)
Create a `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.py"]
```

Build and run:
```bash
docker build -t doraemon-ai .
docker run -p 5000:5000 doraemon-ai
```

## 🎨 Customization

### Change Advice
Edit the advice functions in `doraemon_ai.py`:
- `_homework_advice()`
- `_work_advice()`
- `_learning_advice()`
- `_coding_advice()`
- etc.

### Modify Gadgets
Update the `self.gadgets` list in the `__init__` method

### Change UI Colors
Edit the CSS in `index.html`:
- Primary color: `#667eea`
- Secondary color: `#764ba2`
- Accent color: `#ffb347`

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if port 5000 is in use
# Kill the process or use different port
python app.py --port 5001
```

### CORS Error in Frontend
- Make sure backend is running
- Check CORS is enabled in `app.py` (it is by default)

### Session not found
- Start a new chat session first
- Check session_id matches

## 📝 Example Usage

### Python (Using Requests)
```python
import requests

# Start chat
response = requests.post('http://localhost:5000/api/chat/start', 
    json={'user_name': 'Alice'})
session_id = response.json()['session_id']

# Send message
response = requests.post('http://localhost:5000/api/chat/message',
    json={'session_id': session_id, 'message': 'I have homework'})
print(response.json()['message'])
```

### JavaScript (Using Fetch)
```javascript
// Start chat
const response = await fetch('http://localhost:5000/api/chat/start', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({user_name: 'Bob'})
});
const data = await response.json();
const sessionId = data.session_id;
```

## 🌟 Features in Development

- [ ] User history and preferences
- [ ] Multiple language support
- [ ] Advanced NLP for better understanding
- [ ] Integration with real AI APIs
- [ ] Database for session persistence
- [ ] Mobile app (React Native)
- [ ] Voice interaction support

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Snehal M**
- GitHub: [@snehalm620-sketch](https://github.com/snehalm620-sketch)
- Portfolio: [snek.ai.com](https://snek.ai.com)

## 🙏 Acknowledgments

- Inspired by Doraemon from the manga/anime series
- Built with Flask and modern web technologies
- Special thanks to the Python and web development communities

## 💬 Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the author.

---

**Enjoy chatting with Doraemon AI! 🤖✨**

Made with ❤️ by Snehal M