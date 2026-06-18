#!/bin/bash
# 🚀 DORAEMON AI - INSTANT START SCRIPT
# Run this to start everything automatically!

echo "🤖 Starting Doraemon AI..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found"

# Install dependencies
echo "📦 Installing dependencies..."
python3 -m pip install -r requirements.txt --quiet

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "=========================================="
echo "🤖 DORAEMON AI IS READY!"
echo "=========================================="
echo ""
echo "🔧 Backend starting on: http://localhost:5000"
echo "🎨 Frontend: Open index.html in your browser"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "=========================================="
echo ""

# Start the Flask app
python3 app.py
