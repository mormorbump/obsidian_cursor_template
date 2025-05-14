import os
import yaml
from datetime import datetime, timedelta, date
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
import glob
import re

# スコープの設定
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_credentials():
    creds = None
    # トークンの読み込み
    if os.environ.get('GOOGLE_CALENDAR_TOKEN'):
        creds = Credentials.from_authorized_user_info(
            json.loads(os.environ['GOOGLE_CALENDAR_TOKEN']), 
            SCOPES
        )
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
    
    return creds

def parse_date(date_str):
    """日付文字列をパースする"""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None

def parse_time_range(time_range_str, event_date):
    """時間範囲（例：10:00-11:00）をパースする"""
    try:
        start_time_str, end_time_str = time_range_str.split('-')
        start_time = datetime.strptime(start_time_str.strip(), '%H:%M').time()
        end_time = datetime.strptime(end_time_str.strip(), '%H:%M').time()
        
        start_datetime = datetime.combine(event_date, start_time)
        end_datetime = datetime.combine(event_date, end_time)
        
        return start_datetime, end_datetime
    except ValueError:
        return None, None

def extract_metadata(lines):
    """予定の詳細情報を抽出する"""
    metadata = {}
    for line in lines:
        line = line.strip()
        if line.startswith('- '):
            try:
                key, value = line[2:].split(':', 1)
                metadata[key.strip().lower()] = value.strip()
            except ValueError:
                continue
    return metadata

def parse_events_from_content(content):
    """Markdownの内容から予定情報を抽出する"""
    events = []
    current_date = None
    current_event = None
    event_lines = []
    
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # 日付の行を検出
        if line.startswith('# '):
            date_match = re.search(r'\d{4}-\d{2}-\d{2}', line)
            if date_match:
                current_date = parse_date(date_match.group())
                
        # 予定の行を検出
        elif line.startswith('## '):
            # 前の予定があれば保存
            if current_event and event_lines:
                metadata = extract_metadata(event_lines)
                events.append({**current_event, **metadata})
                
            # 新しい予定の解析
            event_pattern = r'## (\d{1,2}:\d{2}-\d{1,2}:\d{2})\s+(.+)'
            match = re.match(event_pattern, line)
            if match and current_date:
                time_range, title = match.groups()
                start_time, end_time = parse_time_range(time_range, current_date)
                if start_time and end_time:
                    current_event = {
                        'title': title,
                        'start_time': start_time,
                        'end_time': end_time,
                        'description': ''
                    }
                    event_lines = []
                    
        # 予定の詳細情報を収集
        elif current_event and line.startswith('- '):
            event_lines.append(line)
            
    # 最後の予定を保存
    if current_event and event_lines:
        metadata = extract_metadata(event_lines)
        events.append({**current_event, **metadata})
        
    return events

def parse_task_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return parse_events_from_content(content)

def create_calendar_event(service, event):
    # カレンダーIDを固定値に設定
    calendar_id = 'mormorbump@gmail.com'
    
    event_body = {
        'summary': event['title'],
        'description': event.get('description', ''),
        'start': {
            'dateTime': event['start_time'].isoformat(),
            'timeZone': 'Asia/Tokyo',
        },
        'end': {
            'dateTime': event['end_time'].isoformat(),
            'timeZone': 'Asia/Tokyo',
        },
    }
    
    # 場所が指定されている場合は追加
    if 'location' in event:
        event_body['location'] = event['location']
    
    try:
        result = service.events().insert(calendarId=calendar_id, body=event_body).execute()
        print(f'Event created in calendar {calendar_id}: {result.get("htmlLink")}')
    except Exception as e:
        print(f'Error creating event: {e}')

def main():
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    task_files = glob.glob('Tasks/**/*.md', recursive=True)

    for file_path in task_files:
        events = parse_task_file(file_path)
        for event in events:
            create_calendar_event(service, event)

if __name__ == '__main__':
    main()

