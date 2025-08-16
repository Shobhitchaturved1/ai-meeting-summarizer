# 🚀 Deployment Guide

This guide will walk you through deploying your AI Meeting Notes Summarizer to various platforms.

## 📋 Prerequisites

Before deploying, ensure you have:

1. **Groq API Key**: Get one from [Groq Console](https://console.groq.com/)
2. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, etc.)
3. **Account**: Sign up for your chosen deployment platform

## 🌐 Option 1: Render (Recommended - Free Tier)

Render offers a generous free tier and is very easy to use.

### Step 1: Prepare Your Repository
```bash
# Ensure all files are committed
git add .
git commit -m "Initial commit for deployment"
git push origin main
```

### Step 2: Deploy on Render

1. **Sign up** at [render.com](https://render.com)
2. **Connect your GitHub account**
3. **Click "New +" → "Web Service"**
4. **Connect your repository**
5. **Configure the service**:
   - **Name**: `ai-meeting-summarizer` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. **Add Environment Variables**:
   - `GROQ_API_KEY`: Your actual Groq API key
7. **Click "Create Web Service"**

### Step 3: Wait for Deployment
- Render will automatically build and deploy your app
- First deployment takes 5-10 minutes
- You'll get a URL like: `https://your-app-name.onrender.com`

## ☁️ Option 2: Heroku

### Step 1: Install Heroku CLI
```bash
# Windows (using winget)
winget install --id=Heroku.HerokuCLI

# Or download from: https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Login to Heroku
```bash
heroku login
```

### Step 3: Create Heroku App
```bash
# Navigate to your project directory
cd action-collector

# Create a new Heroku app
heroku create your-app-name

# Add your Groq API key
heroku config:set GROQ_API_KEY=your_actual_api_key

# Deploy your app
git push heroku main
```

### Step 4: Open Your App
```bash
heroku open
```

## 🐳 Option 3: Docker Deployment

### Step 1: Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Step 2: Build and Run
```bash
# Build the Docker image
docker build -t ai-meeting-summarizer .

# Run the container
docker run -p 5000:5000 -e GROQ_API_KEY=your_api_key ai-meeting-summarizer
```

## 🖥️ Option 4: Local Production Server

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Environment Variables
```bash
# Windows PowerShell
$env:GROQ_API_KEY="your_api_key"

# Windows Command Prompt
set GROQ_API_KEY=your_api_key

# Linux/Mac
export GROQ_API_KEY=your_api_key
```

### Step 3: Run with Gunicorn
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## 🔧 Environment Configuration

### Required Environment Variables
```bash
GROQ_API_KEY=your_groq_api_key_here
FLASK_ENV=production
FLASK_DEBUG=False
```

### Optional Environment Variables
```bash
PORT=5000
HOST=0.0.0.0
```

## 🧪 Testing Your Deployment

### 1. Health Check
Visit your deployed URL to ensure the app loads.

### 2. Test Summary Generation
1. Paste a sample transcript
2. Add custom instructions
3. Click "Generate Summary"
4. Verify the AI response

### 3. Test Email Sharing
1. Generate a summary
2. Click "Share via Email"
3. Add test email addresses
4. Test the sharing functionality

## 🚨 Troubleshooting

### Common Issues

#### 1. "Module not found" errors
```bash
# Ensure requirements.txt is correct
pip install -r requirements.txt

# Check Python version compatibility
python --version
```

#### 2. API Key errors
```bash
# Verify environment variable is set
echo $GROQ_API_KEY  # Linux/Mac
echo %GROQ_API_KEY% # Windows
```

#### 3. Port binding issues
```bash
# Check if port is in use
netstat -an | grep 5000  # Linux/Mac
netstat -an | findstr 5000  # Windows
```

#### 4. CORS issues
- Ensure `Flask-CORS` is installed
- Check that CORS is properly configured in `app.py`

### Debug Mode
For troubleshooting, temporarily enable debug mode:
```python
# In app.py, change:
app.run(debug=True, host='0.0.0.0', port=5000)
```

## 📊 Monitoring and Logs

### Render
- Logs are available in the Render dashboard
- Automatic restarts on crashes
- Built-in monitoring

### Heroku
```bash
# View logs
heroku logs --tail

# Check app status
heroku ps
```

### Local Server
```bash
# Check process
ps aux | grep gunicorn

# View logs (if logging is configured)
tail -f app.log
```

## 🔒 Security Considerations

### Production Checklist
- [ ] `FLASK_DEBUG=False`
- [ ] `FLASK_ENV=production`
- [ ] API keys are environment variables (not in code)
- [ ] HTTPS enabled (automatic on Render/Heroku)
- [ ] Rate limiting implemented (consider for production)

### API Key Security
```bash
# Never commit API keys
echo ".env" >> .gitignore
echo "*.key" >> .gitignore
```

## 🚀 Performance Optimization

### Gunicorn Configuration
```bash
# For production, use multiple workers
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app

# Or create a gunicorn.conf.py file
workers = 4
bind = "0.0.0.0:5000"
timeout = 120
```

### Environment-Specific Commands

#### Render
```bash
gunicorn app:app
```

#### Heroku
```bash
gunicorn app:app
```

#### Local Production
```bash
gunicorn --workers 2 --bind 0.0.0.0:5000 app:app
```

## 📱 Custom Domain (Optional)

### Render
1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain
4. Update DNS records

### Heroku
```bash
heroku domains:add yourdomain.com
# Update DNS records as instructed
```

## 🔄 Continuous Deployment

### GitHub Actions (Render)
Render automatically deploys when you push to your main branch.

### Manual Deployment
```bash
# After making changes
git add .
git commit -m "Update description"
git push origin main
```

## 📞 Support

If you encounter deployment issues:

1. **Check the logs** in your deployment platform
2. **Verify environment variables** are set correctly
3. **Test locally** first to isolate issues
4. **Check platform-specific documentation**

## 🎯 Next Steps

After successful deployment:

1. **Test all functionality** thoroughly
2. **Monitor performance** and logs
3. **Set up monitoring** (optional)
4. **Configure backups** (if needed)
5. **Share your app** with users!

---

**Happy Deploying! 🚀** 