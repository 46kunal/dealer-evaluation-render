from flask import Flask
from flask_cors import CORS
from flask import send_from_directory
from flask import make_response
from pathlib import Path
import os

app = Flask("Product deal check")
CORS(app)

@app.route("/")
def getHomePage():
  page = (Path(__file__).parent / "html" / "index.html").read_text(encoding="utf-8")
  page = page.replace("__PRODUCT_API_URL__", os.environ.get("PRODUCT_API_URL", "http://localhost:5000").rstrip("/"))
  page = page.replace("__DEALER_API_URL__", os.environ.get("DEALER_API_URL", "http://localhost:8080").rstrip("/"))
  response = make_response(page)
  response.headers["Content-Type"] = "text/html; charset=utf-8"
  return response

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5001")))
    # When no port is specified, starts at default port 5000
