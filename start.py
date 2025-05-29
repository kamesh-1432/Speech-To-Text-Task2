from pyngrok import ngrok
import subprocess
import time
import os

# Terminate any ngrok processes using port 8502
os.system("fuser -k 8502/tcp")

# Check if app.py exists
if not os.path.exists("app.py"):
    raise FileNotFoundError("app.py not found in the current directory")

# Start Streamlit on port 8502
try:
    subprocess.Popen(["streamlit", "run", "app.py", "--server.port", "8502"])
except FileNotFoundError:
    raise RuntimeError("Streamlit is not installed. Run 'pip install streamlit' first.")

# Wait for Streamlit to start
time.sleep(3)

# Create ngrok tunnel for port 8502
try:
    public_url = ngrok.connect(8502, "http")
    print("Your Streamlit app is live at:", public_url.public_url)
    # Keep script running
    while True:
        time.sleep(60)
except Exception as e:
    print(f"Error starting ngrok: {e}")
finally:
    # Clean up ngrok and Streamlit
    ngrok.kill()
    os.system("fuser -k 8502/tcp")
    print("ngrok tunnels and Streamlit server closed")