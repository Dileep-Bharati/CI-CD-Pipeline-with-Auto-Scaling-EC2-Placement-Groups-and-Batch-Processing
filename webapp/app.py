from flask import Flask, jsonify
import boto3
import os
import requests

app = Flask(__name__)

# Get instance metadata
def get_metadata(path):
    try:
        token = requests.put(
            'http://169.254.169.254/latest/api/token',
            headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'},
            timeout=2
        ).text
        response = requests.get(
            f'http://169.254.169.254/latest/meta-data/{path}',
            headers={'X-aws-ec2-metadata-token': token},
            timeout=2
        )
        return response.text
    except:
        return 'localhost'

@app.route('/')
def home():
    instance_id = get_metadata('instance-id')
    availability_zone = get_metadata('placement/availability-zone')
    private_ip = get_metadata('local-ipv4')
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Project 2 - CI/CD Web App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background: linear-gradient(135deg, #232F3E, #FF9900);
                color: white;
                min-height: 100vh;
            }}
            .box {{
                background: rgba(0,0,0,0.5);
                padding: 40px;
                border-radius: 15px;
                display: inline-block;
                margin-top: 50px;
            }}
            h1 {{ color: #FF9900; font-size: 2.5em; }}
            p {{ font-size: 1.2em; margin: 10px 0; }}
            .badge {{
                background: #FF9900;
                color: #232F3E;
                padding: 5px 15px;
                border-radius: 20px;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Project 2 — CI/CD Pipeline</h1>
            <p><span class="badge">Instance ID</span> {instance_id}</p>
            <p><span class="badge">Availability Zone</span> {availability_zone}</p>
            <p><span class="badge">Private IP</span> {private_ip}</p>
            <p><span class="badge">Deployed via</span> GitHub Actions + Docker + ECR</p>
            <p>✅ Docker Container Running</p>
            <p>✅ ALB Load Balancing Active</p>
            <p>✅ Auto Scaling Enabled</p>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'version': os.getenv('APP_VERSION', '1.0.0')
    }), 200

@app.route('/api/info')
def info():
    return jsonify({
        'instance_id': get_metadata('instance-id'),
        'availability_zone': get_metadata('placement/availability-zone'),
        'private_ip': get_metadata('local-ipv4'),
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'production')
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
