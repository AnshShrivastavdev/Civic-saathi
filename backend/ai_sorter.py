VALID_CATEGORIES = ["Water", "Electricity", "Roads", "Garbage", "Police", "Other"]

def classify_complaint(text):

    text = text.lower()

    if "water" in text or "pipe" in text or "leak" in text or "tap" in text:
        return "Water"

    elif "electricity" in text or "power" in text or "light" in text or "transformer" in text:
        return "Electricity"

    elif "road" in text or "pothole" in text or "street" in text or "bridge" in text:
        return "Roads"

    elif "garbage" in text or "trash" in text or "waste" in text or "dirty" in text:
        return "Garbage"

    elif "police" in text or "crime" in text or "theft" in text or "fight" in text:
        return "Police"

    else:
        return "Other"
