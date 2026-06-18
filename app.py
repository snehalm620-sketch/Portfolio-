"""
Flask Backend for Doraemon AI
REST API Server for the Doraemon AI Chatbot
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from doraemon_ai import DoraemonAI
import json

app = Flask(__name__)
CORS(app)

# Store Doraemon instances per user session
users_data = {}

@app.route('/', methods=['GET'])
def home():
    """API Welcome endpoint"""
    return jsonify({
        "status": "success",
        "message": "🤖 Doraemon AI Backend is Running!",
        "version": "1.0.0",
        "endpoints": {
            "POST /api/chat/start": "Start a new chat session",
            "POST /api/chat/message": "Send a message to Doraemon",
            "GET /api/chat/gadget": "Get AI gadget suggestion",
            "POST /api/chat/goodbye": "End the chat session"
        }
    })

@app.route('/api/chat/start', methods=['POST'])
def start_chat():
    """Start a new Doraemon chat session"""
    try:
        data = request.get_json()
        user_name = data.get('user_name', 'Friend').strip() or 'Friend'
        session_id = data.get('session_id', user_name.replace(' ', '_'))
        
        # Create new Doraemon instance for this session
        doraemon = DoraemonAI(user_name)
        users_data[session_id] = {
            'doraemon': doraemon,
            'user_name': user_name
        }
        
        greeting = doraemon.greet_user()
        
        return jsonify({
            "status": "success",
            "session_id": session_id,
            "message": greeting,
            "user_name": user_name
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error starting chat: {str(e)}"
        }), 400

@app.route('/api/chat/message', methods=['POST'])
def chat_message():
    """Send a message and get Doraemon's response"""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'Friend')
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                "status": "error",
                "message": "Message cannot be empty"
            }), 400
        
        # Get Doraemon instance for this session
        if session_id not in users_data:
            return jsonify({
                "status": "error",
                "message": "Session not found. Please start a new chat first."
            }), 404
        
        doraemon = users_data[session_id]['doraemon']
        
        # Handle special commands
        if user_message.lower() == 'bye':
            response = doraemon.farewell_message()
            del users_data[session_id]  # Clean up session
            return jsonify({
                "status": "success",
                "message": response,
                "type": "farewell",
                "session_ended": True
            }), 200
        
        if user_message.lower() == 'gadget':
            response = doraemon.get_gadget_suggestion()
            return jsonify({
                "status": "success",
                "message": response,
                "type": "gadget"
            }), 200
        
        # Get regular response
        response = doraemon.respond_to_problem(user_message)
        
        return jsonify({
            "status": "success",
            "message": response,
            "type": "response"
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error processing message: {str(e)}"
        }), 400

@app.route('/api/chat/gadget', methods=['GET'])
def get_gadget():
    """Get an AI gadget suggestion"""
    try:
        session_id = request.args.get('session_id', 'Friend')
        
        if session_id not in users_data:
            return jsonify({
                "status": "error",
                "message": "Session not found"
            }), 404
        
        doraemon = users_data[session_id]['doraemon']
        gadget_message = doraemon.get_gadget_suggestion()
        
        return jsonify({
            "status": "success",
            "message": gadget_message
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error: {str(e)}"
        }), 400

@app.route('/api/chat/goodbye', methods=['POST'])
def goodbye():
    """End chat session"""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'Friend')
        
        if session_id in users_data:
            doraemon = users_data[session_id]['doraemon']
            farewell = doraemon.farewell_message()
            del users_data[session_id]
            
            return jsonify({
                "status": "success",
                "message": farewell,
                "session_closed": True
            }), 200
        
        return jsonify({
            "status": "error",
            "message": "Session not found"
        }), 404
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error: {str(e)}"
        }), 400

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": "Now",
        "active_sessions": len(users_data)
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == '__main__':
    # Development mode
    app.run(debug=True, host='0.0.0.0', port=5000)
