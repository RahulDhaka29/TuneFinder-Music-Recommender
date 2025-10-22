import os

client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

print("--- Checking Spotify Environment Variables ---")
print(f"SPOTIPY_CLIENT_ID: {client_id}")
print(f"SPOTIPY_CLIENT_SECRET: {client_secret}")

if not client_id or not client_secret:
    print("\nRESULT: ERROR!")
    print("Python cannot find your API keys.")
    print("This is the reason for the 'API Error' on your website.")
    print("\nNext Steps:")
    print("1. Make sure you ran the 'setx' commands exactly as written.")
    print("2. IMPORTANT: You MUST completely close and then reopen your terminal and your code editor (VS Code).")
    print("3. Run this 'check_keys.py' script again in the new terminal.")
else:
    print("\nRESULT: SUCCESS!")
    print("Python can see your environment variables.")
    print("\nNext Steps:")
    print("If you still see the API error on the website after this, it means the ID or Secret you copied has a typo.")
    print("Please double-check the values on the Spotify Developer Dashboard and run the 'setx' commands again.")

print("--- End of Check ---")