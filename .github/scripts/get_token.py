from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import json

# 認証用のスコープ
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def main():
    # credentials.json は Google Cloud Console からダウンロードしたファイル
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=3000) # GCPの

    # トークン情報を JSON 形式で取得
    token_json = {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'token_uri': creds.token_uri,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret,
        'scopes': creds.scopes
    }

    # トークン情報を表示
    print("\n=== GitHub Secrets に設定する値 ===\n")
    print("GOOGLE_CALENDAR_CREDENTIALS:")
    with open('credentials.json', 'r') as f:
        print(f.read())
    
    print("\nGOOGLE_CALENDAR_TOKEN:")
    print(json.dumps(token_json))

if __name__ == '__main__':
    main()