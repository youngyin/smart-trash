# -*- coding: utf-8 -*-
# http://hleecaster.com/python-google-drive-spreadsheet-api/

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'source/userkey.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1oy5_hpQ-Ta2JQEejjZPXXl56ODAn7DlqDCikNO3aegE/edit#gid=0'

def pushData(distance, bottom_distance) : 
    gc = gspread.authorize(credentials)
    # 스프레스시트 문서 가져오기 
    doc = gc.open_by_url(spreadsheet_url)
    # 시트 선택하기
    worksheet = doc.worksheet('getData')
    # 행으로 데이터 추가하기
    # device code, year/month/day, hour:minute, distance
    device_code = 1
    now_day = datetime.today()
    date = now_day.strftime('%Y/%m/%d')
    time = now_day.strftime('%H:%M')
    bottom_distance = int(bottom_distance)
    fill_level = (bottom_distance-distance)/bottom_distance
    worksheet.append_row([device_code, date, time, distance, fill_level])

def setBottomDistance(bottom_distance) : 
    gc = gspread.authorize(credentials)
    # 스프레스시트 문서 가져오기 
    doc = gc.open_by_url(spreadsheet_url)
    # 시트 선택하기
    worksheet = doc.worksheet('init')
    # 데이터 쓰기
    worksheet.update_acell('A2', bottom_distance)
    return bottom_distance
    