from google import genai

client = genai.Client(api_key="AIzaSyB2lMjNGGirV0o2QbcJEyFeBM0L_aiGTLA")

VALID_CATEGORIES = ["Water", "Electricity", "Roads", "Garbage", "Police", "Other"]

def classify_complaint(text):

    prompt = f"""
Classify this civic complaint into exactly one of these departments:
Water, Electricity, Roads, Garbage, Police, Other.

Complaint: {text}

Reply with ONLY the category name.
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    category = response.text.strip()

    # Validate output
    if category not in VALID_CATEGORIES:
        for valid in VALID_CATEGORIES:
            if valid.lower() in category.lower():
                return valid
        return "Other"

    return category
