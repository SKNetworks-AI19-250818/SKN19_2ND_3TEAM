# Netflix 회원 이탈 예측 시스템

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install streamlit pandas numpy plotly scikit-learn openpyxl
```

2. 애플리케이션 실행:
```bash
streamlit run netflix_churn_app.py
```

## 기능

### 메인 페이지
- **넷플릭스 테마**: 빨간색과 검은색 조합의 넷플릭스 브랜드 색상
- **페이지 배너**: 넷플릭스 로고와 제목
- **인사이트 차트**: 모델에서 얻은 2개의 차트
  - 주요 이탈 예측 요인 (Bar Chart)
  - 구독 플랜별 이탈률 (Pie Chart)
- **파일 업로드**: 엑셀 파일 업로드 기능
- **로딩바**: 분석 진행 상황 표시

### 결과 페이지
- **핵심 지표**: 예측대상 고객수, 이탈 위험고객, 이탈 위험률
- **상세 차트**:
  - 이탈 확률 분포 히스토그램
  - 이탈 요인 중요도 바차트
  - 구독플랜별 평균 이탈률
  - 고객만족도 vs 참여도 산점도
- **이탈 위험 고객 리스트**: 위험도가 높은 고객 목록
- **고객 상세 분석**: 선택한 고객의 상세 정보 및 위험 요인

## 데이터 형식

엑셀 파일에 다음 컬럼들이 포함되어야 합니다:

- `Subscription Length (Months)`: 구독기간 (개월)
- `Customer Satisfaction Score (1-10)`: 고객만족도 (1-10점)
- `Daily Watch Time (Hours)`: 일일시청시간 (시간)
- `Engagement Rate (1-10)`: 참여도 (1-10점)
- `Device Used Most Often`: 주이용기기
- `Genre Preference`: 선호장르
- `Region`: 지역
- `Payment History (On-Time/Delayed)`: 결제이력
- `Subscription Plan`: 구독플랜
- `Churn status`: 이탈여부 (선택사항)
- `Support Queries Logged`: 지원문의 건수
- `Age`: 나이
- `Monthly Income ($)`: 월소득 (달러)
- `Promotional Offers Used`: 프로모션 사용
- `Number of Profiles Created`: 생성프로필수

## 스타일 특징

- **화이트 배경**: 깔끔한 화이트 배경
- **진한 텍스트**: 빔프로젝터에서도 잘 보이는 진한 검은색 텍스트
- **넷플릭스 색상**: 빨간색 (#E50914)과 검은색 (#221F1F) 조합
- **굵은 테두리**: 모든 요소에 진한 테두리 적용
- **그림자 효과**: 카드와 버튼에 그림자 효과로 입체감 연출