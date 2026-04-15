import re


def analyze_message(message):
    suspicious_phrases = {
        "urgent": 12,
        "verify": 14,
        "click here": 18,
        "bank account": 18,
        "password": 18,
        "ssn": 22,
        "social security": 22,
        "winner": 18,
        "won": 15,
        "lottery": 18,
        "gift card": 20,
        "payment": 15,
        "pay": 15,
        "limited time": 12,
        "act now": 15,
        "suspended": 18,
        "confirm your account": 20,
        "account locked": 20,
        "avoid closure": 20,
        "immediately": 12,
        "wire transfer": 22,
        "send money": 22,
        "cash app": 18,
        "paypal": 12,
        "bitcoin": 20,
        "crypto": 18,
        "refund": 14,
        "claim now": 16,
        "prize": 18,
    }

    reasons = []
    score = 0
    text = message.lower()

    for phrase, weight in suspicious_phrases.items():
        if phrase in text:
            reasons.append(f"Contains suspicious phrase: '{phrase}'")
            score += weight

    if "http://" in text or "https://" in text or "www." in text:
        reasons.append("Contains a link")
        score += 20

    if "!" in message:
        reasons.append("Uses urgent or emotional punctuation")
        score += 6

    phone_pattern = r"(\+?\d{1,2}[\s-]?)?(\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4})"
    if re.search(phone_pattern, message):
        reasons.append("Contains a phone number")
        score += 10

    money_words = ["money", "transfer", "payment", "pay", "deposit", "invoice", "refund"]
    for word in money_words:
        if word in text:
            reasons.append(f"References financial request: '{word}'")
            score += 12
            break

    urgency_patterns = ["now", "immediately", "today", "asap"]
    for word in urgency_patterns:
        if word in text:
            reasons.append(f"Uses urgency word: '{word}'")
            score += 8
            break

    if len(message.strip()) < 15:
        reasons.append("Very short message, possible bait content")
        score += 5

    if score > 100:
        score = 100

    if score >= 70:
        verdict = "Likely Scam"
    elif score >= 35:
        verdict = "Suspicious"
    else:
        verdict = "Low Risk"

    return {
        "verdict": verdict,
        "risk_score": score,
        "reasons": reasons
    }
