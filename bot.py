from pyrogram import Client
print("""
Go to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
Check your Telegram saved messages section to get your SESSION_NAME
"""
)
API_ID=int(input("Enter API ID: "))
API_HASH=input("Enter API HASH: ")

with Client(":memory:" ,api_id=API_ID ,api_hash=API_HASH, hide_password=False) as pyrogram:
    SESSION_NAME = "SESSION_NAME\n\n" + (pyrogram.export_session_string())
    print("\nGenerating your SESSION_NAME...\n")
    pyrogram.send_message("me", SESSION_NAME, parse_mode="html")
    print("Your SESSION_NAME have been sent to your Telegram Saved Messages")
