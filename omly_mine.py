import requests
import pandas as pd

# URL 및 요청 데이터 설정
url = "https://www.kleague.com/record/teamRank.do"
data = {
    'leagueId': '1',   # K리그1
    'year': '2024',    # 년도
    'stadium': 'home', # 홈 경기
    'recordType': 'rank' # 순위 데이터
}

# POST 요청 보내기
response = requests.post(url, data=data)

# 응답 상태 코드 확인
if response.status_code == 200:
    print("데이터 요청 성공!")
    
    # JSON 데이터를 파싱하여 구조 확인
    json_data = response.json()
    print(json_data)  # JSON 구조 확인

    # 데이터프레임으로 변환
    try:
        df = pd.DataFrame(json_data['data']['teamRank'])  # 정확한 키로 접근
        print(df)

        # CSV 파일로 저장 (UTF-8 BOM 포함)
        df.to_csv("k_league_home_data.csv", index=False, encoding="utf-8-sig")  # 한글 깨짐 방지
        print("데이터가 'k_league_home_data.csv' 파일에 저장되었습니다.")
    except KeyError as e:
        print(f"JSON 키 오류: {e}")
        print("JSON 데이터 구조를 확인하세요.")
else:
    print(f"데이터 요청 실패! 상태 코드: {response.status_code}")


#### 근데 이거를 post 방식으로 하지말고 selenium 으로 하라는데 이유를 모르겠음...
#### post 방식으로 csv를 가지고 오는 것까지 성공했으니, selenium으로 하는 방법을 알아보자!!!

# selenium으로 가지고 오기