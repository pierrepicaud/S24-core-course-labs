from flask import Flask
from datetime import datetime, timezone, timedelta

def get_moscow_time():
    moscow_timezone = timezone(timedelta(hours=3))  # Moscow time is UTC+3
    moscow_time = datetime.now(moscow_timezone)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

@app.route("/")
def home():
    moscow_time = get_moscow_time()
    return f"Moscow Time {moscow_time}";

if __name__ == "__main__":
    app.run(debug=True)