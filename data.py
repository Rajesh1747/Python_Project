import pywhatkit
import schedule
import time
from datetime import datetime
import pytz  # Correct timezone handling

# ✅ Use a correct timezone (e.g., India = "Asia/Kolkata")
timezone = pytz.timezone("Asia/Kolkata")  

# Function to send WhatsApp message
def send_whatsapp_message():
    phone_number = "+91234567891"  # Replace with recipient's number
    message = "Hello! This is an automated message from my WhatsApp bot."

    # Get current time in the correct timezone
    now = datetime.now(timezone)  # ✅ Fixed tzinfo usage
    hour = now.hour
    minute = now.minute + 1  # Schedule for the next minute

    print(f"Scheduling WhatsApp message to {phone_number} at {hour}:{minute}...")

    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

    print("Message sent successfully!")

# ✅ Schedule message (every day at 16:33 IST)
schedule.every().day.at("14:45").do(send_whatsapp_message)

print("WhatsApp Auto Message Sender is running...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
