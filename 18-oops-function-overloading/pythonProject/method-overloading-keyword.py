class Notifier:
    def send_notification(self, method, email=None, subject=None, phone=None, message=""):
        if method == "email":
            if email and subject:
                return f"Send email to {email} with subject '{subject}', message '{message}'"
            else:
                return "Email and subject are required for email notifications."
        elif method == "sms":
            if phone:
                return f"Send SMS to {phone} with message '{message}'"
            else:
                return "Phone number is required for SMS notifications."
        else:
            return "Invalid notification method."

notifier = Notifier()
print(notifier.send_notification(method="email", email="user@example.com", subject="Hello", message="This is an email"))
print(notifier.send_notification(method="sms", phone="1234567890", message="This is an SMS"))

