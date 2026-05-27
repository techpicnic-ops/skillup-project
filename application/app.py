from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Read environment variables from container if present
try:
    PROXY = os.environ['PROXY']
    DB_HOST = os.environ['DB_HOST']
    PORT = os.environ['PORT']
except:
    PROXY = ""
    DB_HOST = ""
    PORT = ""

# The path where the ConfigMap is mounted in your deployment
CONFIG_FILE_PATH = "/etc/config/config.json"

@app.route("/")
def home():
    # Default data in case the file is missing
    config_data = {}
    
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, 'r') as f:
            config_data = json.load(f)


    return render_template(
        "index.html", 
        proxy=PROXY, 
        db_host=DB_HOST, 
        port=PORT,
        config=config_data
    )

# If we handle / call below endpoints directly from frontend app, then its not needed to expose to ingress to work. 
# I disabled these purposely. So that I can expose these two endpoints in Ingress and call directly which will be path-based routing
# @app.route("/hr-department")
# def hr():
#     response = requests.get(
#         "http://company-portal-backend-hr-svc/hr"
#     )
#     return response.text

# @app.route("/finance-department")
# def finance():
#     response = requests.get(
#         "http://company-portal-backend-finance-svc/finance"
#     )
#     return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
    #app.run(host="0.0.0.0", port=8081, debug=True, ssl_context=("app.local.crt", "app.local.key"))
