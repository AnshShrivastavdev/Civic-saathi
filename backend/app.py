from flask import Flask, request, jsonify
from ai_sorter import classify_complaint
from airtable_service import update_record
from email_service import send_email

app = Flask(__name__)

DEPARTMENT_EMAILS = {
    "Water": "water@gov.in",
    "Electricity": "electricity@gov.in",
    "Roads": "roads@gov.in",
    "Garbage": "garbage@gov.in",
    "Police": "police@gov.in",
    "Other": "municipal@gov.in"
}

@app.route("/process-complaint", methods=["POST"])
def process():
    data = request.json

    # Input validation
    if not data or "complaint" not in data or "record_id" not in data:
        return jsonify({"error": "Missing 'complaint' or 'record_id' in request body"}), 400

    complaint = data["complaint"].strip()
    record_id = data["record_id"].strip()

    if not complaint or not record_id:
        return jsonify({"error": "'complaint' and 'record_id' cannot be empty"}), 400

    try:
        # Step 1: Classify via Gemini
        category = classify_complaint(complaint)

        # Step 2: Update Airtable
        update_record(record_id, category)

        # Step 3: Send email to responsible department
        email = DEPARTMENT_EMAILS.get(category, DEPARTMENT_EMAILS["Other"])
        send_email(email, complaint, category)

        return jsonify({"status": "processed", "category": category}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
