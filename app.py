from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Groq API configuration
api_key = os.getenv('GROQ_API_KEY')
print(f"🔍 Checking API key: {'Found' if api_key else 'NOT FOUND'}")
if api_key:
    print(f"🔑 API key starts with: {api_key[:10]}...")

# Groq API configuration
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_HEADERS = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
} if api_key else {}

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
        
        # Check if API key is available
        if not api_key:
            return jsonify({'error': 'AI service is not available. Please check your API key configuration.'}), 500
        
        # Create the prompt for Groq
        system_prompt = """You are an expert meeting summarizer. Create a clear, structured summary based on the user's custom instruction. 
        Format the response in a clean, readable way that matches the user's requirements."""
        
        user_prompt = f"""
        Custom Instruction: {custom_instruction}
        
        Transcript:
        {transcript}
        
        Please provide a summary based on the custom instruction above.
        """
        
        try:
            # Generate summary using Groq API directly
            payload = {
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 2000
            }
            
            response = requests.post(
                GROQ_API_URL,
                headers=GROQ_HEADERS,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                summary = result['choices'][0]['message']['content']
                print(f"✅ AI summarization successful!")
            else:
                error_msg = f"Groq API error: {response.status_code} - {response.text}"
                print(f"❌ {error_msg}")
                return jsonify({'error': error_msg}), 500
                
        except requests.exceptions.RequestException as e:
            error_msg = f'Network error: {str(e)}'
            print(f"❌ {error_msg}")
            return jsonify({'error': error_msg}), 500
        except Exception as e:
            error_msg = f'AI service error: {str(e)}'
            print(f"❌ {error_msg}")
            return jsonify({'error': error_msg}), 500
        
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
