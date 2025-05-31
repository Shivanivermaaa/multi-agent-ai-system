import json

def detect_format_and_intent(content):
    content_lower = content.lower()

    # Simple format detection
    try:
        json.loads(content)
        fmt = 'JSON'
    except:
        if "dear" in content_lower or "regards" in content_lower or "hi" in content_lower:
            fmt = 'Email'
        else:
            fmt = 'Unknown'

    # Simple intent detection
    if "invoice" in content_lower or "quote" in content_lower or "price" in content_lower:
        intent = 'rfq'  # request for quotation
    elif "thank you" in content_lower or "appreciate" in content_lower:
        intent = 'ack'
    else:
        intent = 'Unknown'

    return fmt, intent
