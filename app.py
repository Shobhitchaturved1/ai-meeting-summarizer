from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
import groq
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Groq client
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    print("❌ GROQ_API_KEY not found in environment variables")
    print("Please check your .env file")
    exit(1)

groq_client = groq.Groq(api_key=api_key)
print(f"✅ Groq client initialized with API key: {api_key[:10]}...")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        transcript = data.get('transcript', '')
        custom_instruction = data.get('custom_instruction', '')
        
        if not transcript:
            return jsonify({'error': 'Transcript is required'}), 400
        
        # Create the prompt for Groq
        system_prompt = """You are an expert meeting summarizer. Create a clear, structured summary based on the user's custom instruction. 
        Format the response in a clean, readable way that matches the user's requirements."""
        
        user_prompt = f"""
        Custom Instruction: {custom_instruction}
        
        Transcript:
        {transcript}
        
        Please provide a summary based on the custom instruction above.
        """
        
        # Generate summary using Groq
        response = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=2000
        )
        
        summary = response.choices[0].message.content
        
        return jsonify({
            'summary': summary,
            'success': True
        })
        
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@app.route('/api/share', methods=['POST'])
def share():
    try:
        data = request.get_json()
        summary = data.get('summary', '')
        recipients = data.get('recipients', [])
        subject = data.get('subject', 'Meeting Summary')
        
        if not summary or not recipients:
            return jsonify({'error': 'Summary and recipients are required'}), 400
        
        # For demo purposes, we'll simulate email sending
        # In production, you'd integrate with a real email service like SendGrid or AWS SES
        
        # Simulate email sending
        email_data = {
            'to': recipients,
            'subject': subject,
            'body': summary,
            'status': 'sent'
        }
        
        return jsonify({
            'message': 'Summary shared successfully!',
            'email_data': email_data,
            'success': True
        })
        
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 