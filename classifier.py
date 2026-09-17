# Smart IT Helpdesk - ISSUE CLASSIFIER
def classify_issue(text):

    # Convert the user's input to lowercase
    # This makes matching easier.
    # Example: "Wifi" becomes "wifi"
    text = text.lower()


# Keywords for each issue category
    passwords_keywords = [
        "password",
        "forgot password",
        "reset password",
        "credentials",
        "locked account",
        "account locked",
        "login help",
        "login",
        "password not working",
        "login issue"
    ]
    network_keywords = [
        "wifi",
        "wi-fi",
        "network issue",
        "internet",
        "network",
        "router",
        "connection",
        "disconnecting",
        "network connection",
        "offline"
    ]

    performance_keywords = [
        "slow",
        "lag",
        "lagging",
        "freeze",
        "freezing",
        "hanging",
        "performance",
        "hanging",
        "hang"
    ]

    application_keywords = [
        "application",
        "app",
        "software",
        "outlook",
        "teams",
        "excel",
        "sap",
        "servicenow"
    ]

# Check PASSWORD
    for keywords in passwords_keywords:
        if keywords in text:
            return "LOGIN ISSUE"

# Check NETWORK
    for keywords in network_keywords:
        if keywords in text:
            return "NETWORK"

# Check PERFORMANCE
    for keywords in performance_keywords:
        if keywords in text:
            return "PERFORMANCE"

# Check APPLICATION
    for keywords in application_keywords:
        if keywords in text:
            return "APPLICATION"

# If nothing matches
    return "UNKNOWN"