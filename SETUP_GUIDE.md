# Investment Assistant - Setup Guide

## 📋 Prerequisites

✅ **Already Installed:**
- Python 3.12.3
- Node.js v22.21.0
- npm 10.9.4

## 🚀 Quick Start (3 Steps)

### Step 1: Configure Environment Variables

#### Backend Configuration (`backend\.env`)
Open `backend\.env` and replace the placeholder values:

```env
# Required API Keys
GROQ_API_KEY=your_groq_api_key_here          # Get from: https://console.groq.com
GOOGLE_API_KEY=your_google_gemini_api_key_here  # Get from: https://makersuite.google.com/app/apikey
TAVILY_API_KEY=your_tavily_api_key_here      # Get from: https://tavily.com

# Database (Optional - uses SQLite if not configured)
DB_URI=postgresql+asyncpg://username:password@localhost:5432/investment_db
DB_URI_CHECKPOINTER=postgresql://username:password@localhost:5432/investment_db
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=investment_assistant
```

**Where to get API Keys:**
1. **GROQ API**: https://console.groq.com/keys
2. **Google Gemini API**: https://makersuite.google.com/app/apikey
3. **Tavily API**: https://tavily.com (for web search)

#### Frontend Configuration (`frontend\.env`)
Already configured to connect to `http://localhost:8000`

### Step 2: Install Dependencies

**Option A: Run setup scripts (Recommended)**
1. Double-click `setup-backend.bat`
2. Double-click `setup-frontend.bat`

**Option B: Manual installation**
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

### Step 3: Start the Application

**Option A: Start everything at once (Recommended)**
- Double-click `start-all.bat`

**Option B: Start individually**
1. Double-click `start-backend.bat` (starts on http://localhost:8000)
2. Double-click `start-frontend.bat` (starts on http://localhost:5173)

## 📝 Available Scripts

| Script | Description |
|--------|-------------|
| `setup-backend.bat` | Install backend dependencies |
| `setup-frontend.bat` | Install frontend dependencies |
| `start-backend.bat` | Start backend server only |
| `start-frontend.bat` | Start frontend server only |
| `start-all.bat` | Start both servers at once |

## 🌐 Access Points

After starting:
- **Frontend Application**: http://localhost:5173 (or the port shown in frontend terminal)
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **API Redoc**: http://localhost:8000/redoc

## 🔧 Troubleshooting

### Port Already in Use
If you get a "port already in use" error:
- **Backend (8000)**: Kill the process or change port in `start-backend.bat`
- **Frontend (5173)**: Vite will automatically try the next available port

### Module Not Found Errors
Run the setup scripts again:
```bash
setup-backend.bat
setup-frontend.bat
```

### API Key Errors
Make sure you've:
1. Created `.env` files (already done)
2. Added your actual API keys to `backend\.env`
3. Restarted the backend server

### Database Connection Issues
The app can run without PostgreSQL/MongoDB - it will use in-memory storage.
To use databases:
1. Install PostgreSQL and MongoDB
2. Update the connection strings in `backend\.env`

## 📚 Project Structure

```
investment_assistant/
├── backend/
│   ├── app/
│   │   ├── core/              # Configuration
│   │   ├── database/          # Database connections
│   │   ├── investment_assistant/  # Main AI logic
│   │   │   ├── graphs/        # LangGraph workflows
│   │   │   ├── nodes/         # Graph nodes
│   │   │   ├── prompts/       # AI prompts
│   │   │   └── utils/         # Utilities
│   │   ├── routes/            # API endpoints
│   │   └── main.py            # FastAPI app
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── types/             # TypeScript types
│   │   └── App.tsx            # Main app
│   ├── package.json
│   └── .env
└── [Startup Scripts]
```

## 🎯 Next Steps

1. **Get API Keys** (if you haven't already)
2. **Run** `setup-backend.bat` and `setup-frontend.bat`
3. **Update** `backend\.env` with your API keys
4. **Start** the app with `start-all.bat`
5. **Open** http://localhost:5173 in your browser

## 💡 Features

- **AI-Powered Investment Research**: Uses LangGraph for complex research workflows
- **Multiple LLM Support**: Groq (fast) and Google Gemini (comprehensive)
- **Web Search Integration**: Tavily for real-time financial data
- **Interactive Chat Interface**: React-based UI with markdown support
- **Conversation History**: MongoDB-backed chat persistence

## 📞 Support

For issues with:
- **Setup**: Check the troubleshooting section above
- **API Keys**: Visit the respective provider websites
- **Dependencies**: Ensure Python 3.12+ and Node.js 22+ are installed

---

**Ready to go!** Run `start-all.bat` and start exploring investment insights! 🚀
