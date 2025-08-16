# 🤖 AI Meeting Notes Summarizer

A full-stack web application that uses AI to summarize meeting transcripts and share them via email. Built with Python Flask backend and a clean, responsive frontend.

## ✨ Features

- **AI-Powered Summarization**: Upload meeting transcripts and get intelligent summaries
- **Custom Instructions**: Specify how you want the summary formatted (e.g., "bullet points for executives", "action items only")
- **Editable Summaries**: Review and edit AI-generated summaries before sharing
- **Email Sharing**: Share summaries with multiple recipients via email
- **Responsive Design**: Clean, modern interface that works on all devices

## 🚀 Live Demo

**Deployed Application**:[https://ai-meeting-summarizer-wchl.onrender.com/](https://ai-meeting-summarizer-wchl.onrender.com/)
**Developer**: Shobhit

## 🛠️ Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **AI Service**: Groq (Llama 3.1 8B model)
- **Deployment**: Render (free tier)
- **Email**: Simulated email service (easily integratable with SendGrid, AWS SES, etc.)

## 📋 Prerequisites

- Python 3.8+
- Groq API key ([Get one here](https://console.groq.com/))
- Git

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd action-collector
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your Groq API key
GROQ_API_KEY=your_actual_api_key_here
```

### 4. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🌐 Deployment

### Option 1: Render (Recommended - Free Tier)

1. **Fork/Clone** this repository to your GitHub account
2. **Sign up** for a free account at [Render](https://render.com)
3. **Create a new Web Service** and connect your GitHub repository
4. **Set environment variables**:
   - `GROQ_API_KEY`: Your Groq API key
5. **Deploy** - Render will automatically build and deploy your app

### Option 2: Heroku

1. **Install Heroku CLI** and login
2. **Create a new Heroku app**:
   ```bash
   heroku create your-app-name
   ```
3. **Set environment variables**:
   ```bash
   heroku config:set GROQ_API_KEY=your_api_key
   ```
4. **Deploy**:
   ```bash
   git push heroku main
   ```

### Option 3: Local Development

For local development and testing:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export GROQ_API_KEY=your_api_key

# Run the app
python app.py
```

## 📁 Project Structure

```
action-collector/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── render.yaml           # Render deployment config
├── Procfile             # Heroku deployment config
├── runtime.txt          # Python version specification
├── env.example          # Environment variables template
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)
- `FLASK_ENV`: Flask environment (production/development)
- `FLASK_DEBUG`: Debug mode (True/False)

### AI Model Configuration

The application uses Groq's Llama 3.1 8B model by default. You can modify the model in `app.py`:

```python
response = groq_client.chat.completions.create(
    messages=[...],
    model="llama3-8b-8192",  # Change this to use different models
    temperature=0.7,
    max_tokens=2000
)
```

## 📧 Email Integration

Currently, the application simulates email sending. To integrate with real email services:

### SendGrid Integration
```python
import sendgrid
from sendgrid.helpers.mail import Mail

# Replace the share function in app.py
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
message = Mail(
    from_email='your-email@domain.com',
    to_emails=recipients,
    subject=subject,
    plain_text_content=summary
)
response = sg.send(message)
```

### AWS SES Integration
```python
import boto3

# Replace the share function in app.py
ses = boto3.client('ses', region_name='us-east-1')
response = ses.send_email(
    Source='your-email@domain.com',
    Destination={'ToAddresses': recipients},
    Message={'Subject': {'Data': subject}, 'Body': {'Text': {'Data': summary}}}
)
```

## 🧪 Testing

### Manual Testing
1. **Upload a transcript**: Paste any meeting transcript or text content
2. **Add custom instructions**: Try different prompts like:
   - "Summarize in bullet points for executives"
   - "Highlight only action items"
   - "Create a timeline of events"
3. **Generate summary**: Click "Generate Summary" and wait for AI processing
4. **Edit summary**: Make any necessary changes to the generated summary
5. **Share summary**: Test the email sharing functionality

### Sample Transcript for Testing
```
Meeting: Q4 Planning Session
Date: December 15, 2024
Attendees: John (CEO), Sarah (CTO), Mike (CFO), Lisa (Head of Marketing)

John: Welcome everyone to our Q4 planning session. Let's review our goals and set priorities.

Sarah: From a technical perspective, we need to focus on the mobile app launch. We're behind schedule by about 2 weeks.

Mike: Budget-wise, we have $50K allocated for Q4 marketing campaigns. We need to decide how to allocate this.

Lisa: I suggest we focus 60% on digital ads, 30% on content marketing, and 10% on events.

John: Good suggestions. Sarah, what's the timeline for the mobile app?

Sarah: We can launch by December 20th if we prioritize the core features and delay some nice-to-have features.

Mike: That works with our budget timeline. We can allocate the marketing spend starting January 1st.

John: Perfect. Let's set these as our Q4 priorities: 1) Mobile app launch by Dec 20th, 2) Marketing campaign planning, 3) Budget allocation review.
```

## 🔒 Security Considerations

- **API Key Protection**: Never commit your API keys to version control
- **Input Validation**: All user inputs are validated on both frontend and backend
- **CORS**: Configured for development; adjust for production deployment
- **Rate Limiting**: Consider implementing rate limiting for production use

## 🚀 Performance Optimization

- **AI Model Selection**: Choose appropriate Groq models based on your needs
- **Caching**: Implement Redis caching for frequently requested summaries
- **CDN**: Use CDN for static assets in production
- **Database**: Consider adding a database for storing summaries and user data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:

1. Check the [Issues](https://github.com/yourusername/action-collector/issues) page
2. Create a new issue with detailed information
3. Include your environment details and error messages

## 🔮 Future Enhancements

- [ ] User authentication and account management
- [ ] Summary history and search
- [ ] Multiple AI model support
- [ ] Real-time collaboration
- [ ] Mobile app
- [ ] Integration with calendar systems
- [ ] Advanced analytics and insights
- [ ] Multi-language support

## 📊 Metrics

- **Response Time**: Average AI summary generation: 2-5 seconds
- **Model**: Llama 3.1 8B (via Groq)
- **Max Tokens**: 2000 (configurable)
- **Temperature**: 0.7 (balanced creativity and consistency)

---

**Built with ❤️ using Python Flask and Groq AI** 
