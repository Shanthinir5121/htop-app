from flask import Flask
import os
import time
import subprocess

app= Flask(__name__)

@app.route('/htop')
def htop_endpoint():
    full_name = "Shanthini R"
    username = os.getlogin()
    server_time = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.gmtime(time.time() + 19800))
    top_output = subprocess.getoutput('top -bn1')
    return f"<h1>Name: {full_name}</h1><h2>Username: {username}</h2><h3>Server Time (IST): {server_time}</h3><pre>{top_output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
