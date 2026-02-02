# 🔑 API Keys Setup Guide

## Required API Keys

### 1. GROQ API Key
**Purpose**: Fast LLM inference (primary AI model)
**Get it from**: https://console.groq.com/keys
**Steps**:
1. Go to https://console.groq.com
2. Sign up/Login
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste into `backend\.env` as `GROQ_API_KEY`

**Free Tier**: Yes (generous limits for testing)

---

### 2. Google Gemini API Key
**Purpose**: Alternative LLM for comprehensive analysis
**Get it from**: https://makersuite.google.com/app/apikey
**Steps**:
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Select or create a project
5. Copy and paste into `backend\.env` as `GOOGLE_API_KEY`

**Free Tier**: Yes (60 requests per minute)

---

### 3. Tavily API Key
**Purpose**: Web search for real-time financial data
**Get it from**: https://tavily.com
**Steps**:
1. Go to https://tavily.com
2. Sign up for an account
3. Navigate to API Keys in dashboard
4. Copy your API key
5. Paste into `backend\.env` as `TAVILY_API_KEY`

**Free Tier**: Yes (1,000 searches/month)

---

## Optional: Database Configuration

### PostgreSQL (Optional)
**Purpose**: Persistent storage for conversations and checkpoints
**If not configured**: App will use in-memory storage

**Setup**:
1. Install PostgreSQL from https://www.postgresql.org/download/
2. Create a database: `investment_db`
3. Update these in `backend\.env`:
   - `DB_URI=postgresql+asyncpg://username:password@localhost:5432/investment_db`
   - `DB_URI_CHECKPOINTER=postgresql://username:password@localhost:5432/investment_db`

### MongoDB (Optional)
**Purpose**: Store conversation history
**If not configured**: Conversations won't persist

**Setup**:
1. Install MongoDB from https://www.mongodb.com/try/download/community
2. Start MongoDB service
3. Update in `backend\.env`:
   - `MONGODB_URI=mongodb://localhost:27017`
   - `MONGODB_DB_NAME=investment_assistant`

---

## Verification Checklist

After setting up, your `backend\.env` should look like:

```env
# ✓ All three API keys filled
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GOOGLE_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Optional (can leave as-is for testing)
DB_URI=postgresql+asyncpg://username:password@localhost:5432/investment_db
DB_URI_CHECKPOINTER=postgresql://username:password@localhost:5432/investment_db
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=investment_assistant

# These are already configured
LANGFUSE_SECRET_KEY=sk-lf-ac6e9c26-3f07-4e59-9030-dfd8276dfec0
LANGFUSE_PUBLIC_KEY=pk-lf-2cdadb57-86b4-4943-82ab-ce4cfcaa601e
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

---

## Testing Your Setup

1. Save your API keys to `backend\.env`
2. Run `start-backend.bat`
3. Check the terminal for any errors
4. If successful, you'll see: "Application startup complete"
5. Visit http://localhost:8000/docs to test the API

---

## Troubleshooting

**"API key invalid" error**:
- Double-check you copied the entire key
- Make sure there are no extra spaces
- Verify the key is active in the provider's dashboard

**"Rate limit exceeded"**:
- You're using the free tier limits
- Wait a bit and try again
- Consider upgrading your API plan

**Database connection errors**:
- The app will work without databases
- They're only needed for persistence
- You can set them up later

---

**Next Step**: Once you have at least the 3 required API keys, run `start-all.bat`!
