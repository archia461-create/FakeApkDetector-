# from flask import Flask, render_template, request, jsonify
# import os
# import random
# import datetime

# app = Flask(__name__)
# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Helper function to simulate APK analysis
# def analyze_apk(file_path):
#     file_name = os.path.basename(file_path)
#     file_size_kb = round(os.path.getsize(file_path) / 1024, 2)

#     # Simulated analysis
#     features = [
#         {"feature": "Has Bank Keyword", "value": int(bool(random.getrandbits(1)))},
#         {"feature": "Permissions Count", "value": random.randint(5, 50)},
#         {"feature": "File Size (KB)", "value": file_size_kb},
#         {"feature": "Has SMS Permission", "value": int(bool(random.getrandbits(1)))},
#         {"feature": "Has Camera Permission", "value": int(bool(random.getrandbits(1)))},
#         {"feature": "Certificate Valid", "value": int(bool(random.getrandbits(1)))},
#         {"feature": "Code Obfuscation", "value": int(bool(random.getrandbits(1)))},
#         {"feature": "Network Connections", "value": random.randint(1, 20)},
#     ]

#     # Simulated prediction
#     prediction = random.choice(["fake", "safe"])
#     features.append({"feature": "Prediction", "value": prediction})

#     # Simulated detailed analysis
#     details = [
#         {"title": "Filename", "description": file_name},
#         {"title": "File Size", "description": f"{file_size_kb} KB"},
#         {"title": "Analysis Time", "description": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
#     ]

#     return {"features": features, "details": details}

# # Home route
# @app.route("/")
# def index():
#     return render_template("index.html")

# # API endpoint for file upload and analysis
# @app.route("/analyze", methods=["POST"])
# def analyze():
#     if "apkFile" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["apkFile"]
#     if file.filename == "":
#         return jsonify({"error": "No file selected"}), 400

#     if file.filename.endswith(".apk"):
#         save_path = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(save_path)
#         analysis_result = analyze_apk(save_path)
#         return jsonify(analysis_result)
#     else:
#         return jsonify({"error": "Invalid file type. Please upload an APK."}), 400

# if __name__ == "__main__":
#     app.run(debug=True)





from flask import Flask, render_template, request, jsonify
import os
import random

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# APK analysis route
@app.route('/analyze', methods=['POST'])
def analyze():
    if 'apk_file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    apk = request.files['apk_file']
    filename = apk.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    apk.save(file_path)

    # --- Dummy Analysis Logic ---
    file_size_kb = os.path.getsize(file_path) // 1024

    # Randomized dummy values for permissions and features
    permissions_count = random.randint(10, 50)
    has_sms_permission = random.choice([True, False])
    has_camera_permission = random.choice([True, False])
    certificate_valid = random.choice([True, False])
    code_obfuscation = random.choice([True, False])
    network_connections = random.randint(1, 20)

    # Risk scoring logic
    risk_score = 0
    if any(k in filename.lower() for k in ["fake", "phish", "malware"]):
        risk_score += 2
    if permissions_count > 30:
        risk_score += 1
    if has_sms_permission:
        risk_score += 1
    if has_camera_permission:
        risk_score += 1
    if not certificate_valid:
        risk_score += 1
    if code_obfuscation:
        risk_score += 1

    prediction = "fake" if risk_score >= 3 else "safe"

    # Features list
    features = [
        {"feature": "Has Bank Keyword", "value": "Yes" if "bank" in filename.lower() else "No"},
        {"feature": "Permissions Count", "value": permissions_count},
        {"feature": "File Size (KB)", "value": file_size_kb},
        {"feature": "Has SMS Permission", "value": "Yes" if has_sms_permission else "No"},
        {"feature": "Has Camera Permission", "value": "Yes" if has_camera_permission else "No"},
        {"feature": "Certificate Valid", "value": "Yes" if certificate_valid else "No"},
        {"feature": "Code Obfuscation", "value": "Yes" if code_obfuscation else "No"},
        {"feature": "Network Connections", "value": network_connections},
        {"feature": "Prediction", "value": prediction}
    ]

    # Detailed analysis
    details = [
        {"title": "Filename", "description": filename},
        {"title": "File Size", "description": f"{file_size_kb} KB"},
        {"title": "Upload Path", "description": file_path},
        {"title": "Analysis Type", "description": "Dummy static analysis with risk scoring"}
    ]

    return jsonify({"filename": filename, "features": features, "details": details})

if __name__ == "__main__":
    app.run(debug=True)
