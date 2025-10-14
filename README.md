
# 🎬 넷플릭스 유저 특성에 따른 구독 이탈 예측

## **👥** 팀 소개

**팀명:** **다섯플릭스**

<div align="center">
 
| 배상준 | 김진 | 김범섭 | 이인재 | 왕혁준 |
| --- | --- | --- | --- | --- |
| <img width="204" height="252" alt="image" src="https://github.com/user-attachments/assets/5ddf43cc-777d-4ff4-a8bc-b035aa93ebc0" /> | <img width="211" height="246" alt="image" src="https://github.com/user-attachments/assets/f957b8b2-52ac-4597-9478-bcb5285611fa" /> | <img width="203" height="257" alt="image" src="https://github.com/user-attachments/assets/95cb45c7-a768-4522-892c-a50bc020f93f" /> | <img width="200" height="254" alt="image" src="https://github.com/user-attachments/assets/ec9671dc-9b8d-48b7-8243-0f6567c42a7a" /> | <img width="195" height="260" alt="image" src="https://github.com/user-attachments/assets/d2692b1c-96d5-48c0-b1f9-721631c8940b" /> |
| <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-WindyAle-181717?style=flat&logo=github&logoColor=white)](https://github.com/WindyAle)</div> | <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-KIMjjjjjjjj-181717?style=flat&logo=github&logoColor=white)](https://github.com/KIMjjjjjjjj)</div> | <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-WhatSupYap-181717?style=flat&logo=github&logoColor=white)](https://github.com/WhatSupYap)</div> | <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-distecter-181717?style=flat&logo=github&logoColor=white)](https://github.com/distecter)</div> | <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-vibevibe26-181717?style=flat&logo=github&logoColor=white)](https://github.com/vibevibe26)</div> |

</div>



---

## **🎯** 프로젝트 개요

**프로젝트 명:** 넷플릭스 유저 특성에 따른 구독 이탈 예측

**프로젝트 소개:**

넷플릭스 사용자 데이터를 기반으로 유저의 특성을 분석하고, 구독 이탈(Churn) 가능성을 예측하는 프로젝트이다. 다양한 사용자 행동, 결제 패턴, 선호 장르, 기기 사용 등 다양한 정보를 종합하여, 이탈 위험이 높은 사용자를 사전에 식별하고 맞춤형 유지 전략을 설계할 수 있다.

**프로젝트 필요성(배경):**

- 구독 기반 서비스에서 이탈률 감소는 수익과 직결됨
- 유저 특성에 따른 맞춤형 마케팅 및 유지 전략 설계 필요
- 넷플릭스와 같은 ott 서비스의 사용자 데이터는 한정적이며 이를 체계적으로 분석하여 예측에 활용한 사례는 더욱 제한적임

**프로젝트 목표:**

- 넷플릭스 유저 데이터 기반의 이탈 예측 모델 개발
- 데이터 전처리 및 피처 엔지니어링을 통한 의미 있는 변수 도출
- 시각화를 통해 유저 특성 및 이탈 관련 인사이트 제공
- 모델 결과를 활용한 의사결정 지원

---

## **🛠️** 기술 스택

- **언어 및 라이브러리:** 

![Python](https://img.shields.io/badge/Python-3.12.7-3776AB?style=flat&logo=python&logoColor=white) 
![Pandas](https://img.shields.io/badge/Pandas-2.3.2-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.1.3-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.6-003366?style=flat&logo=plotly&logoColor=white)

![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-4C72B0?style=flat&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.24.1-3F4F75?style=flat&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-FF4B4B?style=flat&logo=streamlit&logoColor=white)

- **머신러닝:**

![LightGBM](https://img.shields.io/badge/LightGBM-4.5.0-017A17?style=flat&logo=lightgbm&logoColor=white)

- **개발 환경 및 협업 도구:**

![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=flat&logo=notion&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)

---

## **📄** WBS

(노션 프로젝트 기획 캡쳐)

1. **데이터 수집 및 로드**
2. **데이터 탐색(EDA)**
    1. **데이터 정제 및 전처리**
3. **피처 엔지니어링**
4. **모델 학습 및 평가**
5. **프론트엔드(Streamlit)**
6. **최종 보고서 작성**

---

## **📊** 데이터 전처리 결과서 (EDA 기반)

### **1️⃣ 데이터 로드**

[NETFLIX 마켓팅 팀과의 협업을 통해 얻은 데이터셋](https://github.com/JackBrowne556/Netflix-Churn-Project)

```markdown
rename_map = {
    "Customer ID": "고객번호",
    "Subscription Length (Months)": "구독기간_개월",
    "Customer Satisfaction Score (1-10)": "고객만족도_1_10",
    "Daily Watch Time (Hours)": "일일시청시간_시간",
    "Engagement Rate (1-10)": "참여도_1_10",
    "Device Used Most Often": "주이용기기",
    "Genre Preference": "선호장르",
    "Region": "지역",
    "Payment History (On-Time/Delayed)": "결제이력_정시_지연",
    "Subscription Plan": "구독플랜",
    "Churn status": "이탈여부",
    "Support Queries Logged": "지원문의_건수",
    "Age": "나이",
    "Monthly Income ($)": "월소득_달러",
    "Promotional Offers Used": "프로모션_사용",
    "Number of Profiles Created": "생성프로필수",
    "Unnamed: 16": "미지정_16",
    "Unnamed: 17": "미지정_17",
    "Unnamed: 18": "미지정_18",
}
```

### **2️⃣ 데이터 구조와 기초 통계 확인**

| **Info** | **Describe** |
| --- | --- |
| (info 캡처) | (descibe 캡처) |


### **3️⃣ 결측치 및 이상치 탐색**

- **Customer ID (고객번호)**
    - 정상: C123456 형태
    - 이상치: NaN, '###', z014464, y117407, x065493, Cz76729
    - 처리: 결측치와 이상치를 공백 처리 후 새로운 코드 부여
- **숫자형 컬럼**
    - **Subscription Length, Satisfaction, Daily Watch Time, Engagement Rate 등**
    - 숫자가 아닌 값 → 결측치 처리 필요
- **범주형 컬럼**
    - **Device, Genre, Region, Payment, Subscription Plan**
    - 허용 값 외 항목 → 유사 값 치환 처리 필요
- **극소수 데이터**
    - Device, Genre, Region, Payment 등 0.3% 수준 → 제거 또는 통합 처리 필요

### **4️⃣ 데이터 시각화를 통한 탐색**

(시각화 자료 - 히트맵 & 박스플롯 & 막대그래프)

### 5️⃣ 데이터 정제 및 전처리

1. **중복 및 결측치 처리**
    - **전체 중복 데이터 제거**
    - **`Churn status` 결측치 및 오류 데이터 수정**
        - 결측치 처리 및 문자형 오류 데이터 치환 처리
        - 극소수 클래스 제거 (Maybe - 0.35%)
    - **`Customer ID` 결측치 401건 처리**
2. **숫자형 데이터 정리**
    - **숫자형 오류 데이터**
        - 결측치 중위값 대체
    - **범위 제한 숫자형 컬럼 정제**
        - `Customer Satisfaction Score (1-10)`
        - `Engagement Rate (1-10)`
            
            → 1~10으로 한정
            
3. **문자형 데이터 정제**
    - **오타 및 유사 문자 치환 처리**
        - 예)  “Mobilz” → “Mobile”, “Smyrt TV” → “Smart TV”
4. **극소수 클래스 제거** 
    
    
    | 컬럼명 | 제거 클래스 | 비율 |
    | --- | --- | --- |
    | `Device Used Most Often` | Smart_Television | 0.32% |
    | `Genre Preference` | Dramedy | 0.31% |
    | `Region` | Eurasia | 0.32% |
    | `Payment History` | Late | 0.32% |

### 6️⃣ 피처 엔지니어링

- **범주화 작업:**
    - `Daily Watch Time (Hours)` →  1시간 단위 구간화
    - `Monthly Income ($)` → 고객 수입 1000달러 단위 구간화
    - `Age` → 연령 10세 단위 구간화

- **지역별 구독료 데이터 결합**
    - 새로운 **지역별 평균 구독료 데이터셋** 로드
    - `Region`별 평균 요금 데이터를 사용자 데이터에 결합
- **새로운 복합 컬럼 생성:**
    
    
    | 새로운 파생 변수 | 설명 |
    | --- | --- |
    | `User_Subscription_Price` | 지역별 평균 요금 데이터 결합 |
    | `Price_Burden_Ratio` | 소득 대비 구독 요금 비율 |
    | `Watch_Time_per_Dollar` | 요금당 시청 시간 (1달러당 얼마나 보는지) |
    | `Satisfaction_per_Dollar` | 요금당 만족도 |
    | `Queries_per_Month` | 월 평균 고객 문의 수 |

### ⚙️ 최종 컬럼 및 시각화

(최종 컬럼)

(시각화와 인사이트)

---

## 🤖 머신러닝 학습 결과서

- **모델**: LightGBM
- **평가 지표:**
    
    
    | 지표 | 점수 |
    | --- | --- |
    | 정확도 (Accuracy) |  |
    | 정밀도 (Precision) |  |
    | 재현율 (Recall) |  |
    | F1 Score |  |
- **주요 피처:**

---

## 🧪 수행 결과

- **Streamlit:**
    - 예측 확률 및 실제 이탈 여부 비교
  
- **주요 인사이트:**
    - (인사이트)
    

---

## 💬 한 줄 회고
