<div align="center">
 
# 🎥 넷플릭스 유저 특성에 따른 구독 이탈 예측

</div>

## 👥 팀 소개

## 🍿 다섯플릭스 
[![Notion](https://img.shields.io/badge/Notion-000000?style=flat&logo=notion&logoColor=white)](https://www.notion.so/3-28b0413479c4818d911dd3df82000d7b?source=copy_link)


<div align="center">
 
| 배상준 | 김진 | 김범섭 | 이인재 | 왕혁준 |
| --- | --- | --- | --- | --- |
| <img width="204" height="252" alt="image" src="https://github.com/user-attachments/assets/5ddf43cc-777d-4ff4-a8bc-b035aa93ebc0" /> | <img width="211" height="246" alt="image" src="https://github.com/user-attachments/assets/f957b8b2-52ac-4597-9478-bcb5285611fa" /> | <img width="203" height="257" alt="image" src="https://github.com/user-attachments/assets/95cb45c7-a768-4522-892c-a50bc020f93f" /> | <img width="200" height="254" alt="image" src="https://github.com/user-attachments/assets/ec9671dc-9b8d-48b7-8243-0f6567c42a7a" /> | <img width="195" height="260" alt="image" src="https://github.com/user-attachments/assets/d2692b1c-96d5-48c0-b1f9-721631c8940b" /> |
| <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-WindyAle-181717?style=flat&logo=github&logoColor=white)](https://github.com/WindyAle)</div> | <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-KIMjjjjjjjj-181717?style=flat&logo=github&logoColor=white)](https://github.com/KIMjjjjjjjj)</div> | <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-WhatSupYap-181717?style=flat&logo=github&logoColor=white)](https://github.com/WhatSupYap)</div> | <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-distecter-181717?style=flat&logo=github&logoColor=white)](https://github.com/distecter)</div> | <div align="center">[![GitHub](https://img.shields.io/badge/GitHub-vibevibe26-181717?style=flat&logo=github&logoColor=white)](https://github.com/vibevibe26)</div> |

</div>


---

## 🎯 프로젝트 개요

<div align="center">
<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/8eb8b568-293e-4d44-936f-9a9e0179ff56" />
</div>

**프로젝트 명:** 넷플릭스 유저 특성에 따른 구독 이탈 예측

**프로젝트 소개:**

넷플릭스 사용자 데이터를 기반으로 유저의 특성을 분석하고, 구독 이탈(Churn) 가능성을 예측하는 프로젝트이다. 다양한 사용자 행동, 결제 패턴, 선호 장르, 기기 사용 등 다양한 정보를 종합하여, 이탈 위험이 높은 사용자를 사전에 식별하고 맞춤형 유지 전략을 설계할 수 있다.

**프로젝트 필요성:**

- 스트리밍 서비스 경쟁 심화  
- 구독 기반 서비스에서 이탈률 감소는 수익과 직결
- 고객 이탈 최소화 필요
- 유저 특성에 따른 맞춤형 마케팅 및 유지 전략 설계

**프로젝트 목표:**

- 넷플릭스 유저 데이터 기반의 이탈 예측 모델 개발
- 데이터 전처리 및 피처 엔지니어링을 통한 의미 있는 변수 도출
- 시각화를 통해 유저 특성 및 이탈 관련 인사이트 제공
- 모델 결과를 활용한 의사결정 지원

---

## **🛠️** 기술 스택

**언어 및 라이브러리:** 

![Python](https://img.shields.io/badge/Python-3.12.7-3776AB?style=flat&logo=python&logoColor=white) 
![Pandas](https://img.shields.io/badge/Pandas-2.3.2-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.1.3-013243?style=flat&logo=numpy&logoColor=white)

![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.6-003366?style=flat&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-4C72B0?style=flat&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.24.1-3F4F75?style=flat&logo=plotly&logoColor=white)


**머신러닝 및 프론트엔드:**
  
![Streamlit](https://img.shields.io/badge/Model-LightGBM-017A17?style=flat&logo=LightGBM&logoColor=white)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

**개발 환경 및 협업 도구:**

![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=flat&logo=visualstudiocode&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=flat&logo=notion&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)

---

## 📄 WBS

```mermaid
flowchart LR
    A[데이터 수집]:::blueNode --> B[데이터 탐색]:::greenNode
    B --> C[정제 및 전처리]:::yellowNode
    C --> D[피처 엔지니어링]:::redNode
    D --> E[모델 학습 및 평가]:::purpleNode
    E --> F[Streamlit 대시보드]:::orangeNode

    %% 노드 스타일 정의
    classDef blueNode fill:#cce5ff,stroke:#3399ff,stroke-width:2px;
    classDef greenNode fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef yellowNode fill:#fff3cd,stroke:#ffc107,stroke-width:2px;
    classDef redNode fill:#f8d7da,stroke:#dc3545,stroke-width:2px;
    classDef purpleNode fill:#e2d6f9,stroke:#6f42c1,stroke-width:2px;
    classDef orangeNode fill:#ffe5b4,stroke:#ff851b,stroke-width:2px;

```

<div align="center">
<img width="892" height="763" alt="image" src="https://github.com/user-attachments/assets/f3d86257-861d-4bac-902c-c02623c9ddee" />
</div>

---

## 🎬 데이터 전처리 결과서 (EDA 기반)

### 1️⃣ 데이터 구조

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/JackBrowne556/Netflix-Churn-Project">
        <img src="https://img.shields.io/badge/NETFLIX%20사용자%20데이터-Link-blue?style=flat" alt="사용자 데이터 링크">
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/JackBrowne556/Netflix-Churn-Project">
        <img src="https://img.shields.io/badge/지역별%20구독료%20데이터-Link-green?style=flat" alt="지역별 구독료 데이터 링크">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img width="600" src="https://github.com/user-attachments/assets/596bb4fb-962b-4996-b66a-ede5c41fdb0d" alt="사용자 데이터">
    </td>
    <td align="center">
      <img width="680" src="https://github.com/user-attachments/assets/6a3a8655-7da1-4732-b6de-3fa00626854b" alt="지역별 구독료 데이터">
    </td>
  </tr>
</table>


---

### 2️⃣ 결측치 및 이상치 탐색

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
 
---


### 3️⃣ 데이터 시각화를 통한 탐색

<div align="center">

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/70082a7d-7574-4836-81df-1b9fede27300" />

<img width="1189" height="989" alt="image" src="https://github.com/user-attachments/assets/76a274b1-825b-4453-ad28-802ab93b7188" />

</div>

---

### 4️⃣ 데이터 정제 및 전처리

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
    | `Genre Preference` | Dramedy | 0.31% |
    | `Region` | Eurasia | 0.32% |
    | `Payment History` | Late | 0.32% |
   
---

### 5️⃣ 피처 엔지니어링

- **범주화 작업:**
    - `Daily Watch Time (Hours)` →  1시간 단위 구간화
    - `Monthly Income ($)` → 고객 수입 1000달러 단위 구간화
    - `Age` → 연령 10세 단위 구간화

- **지역별 구독료 데이터 결합**
    - 새로운 **지역별 평균 구독료 데이터셋** 로드
    - `Region`별 평균 요금 데이터를 사용자 데이터에 결합
- **새로운 복합 컬럼 생성:**
    
	| 새로운 파생 변수                 | 설명                       | 사용한 원본 컬럼                                                       |
	| ------------------------- | ------------------------ | --------------------------------------------------------------- |
	| `User_Subscription_Price` | 지역별 평균 요금 데이터 결합         | 지역별 요금 데이터                                                      |
	| `Price_Burden_Ratio`      | 소득 대비 구독 요금 비율           | `User_Subscription_Price`, `Monthly Income ($)`                 |
	| `Watch_Time_per_Dollar`   | 요금당 시청 시간 (1달러당 얼마나 보는지) | `Daily Watch Time (Hours)`, `User_Subscription_Price`           |
	| `Satisfaction_per_Dollar` | 요금당 만족도                  | `Customer Satisfaction Score (1-10)`, `User_Subscription_Price` |
	| `Queries_per_Month`       | 월 평균 고객 문의 수             | `Support Queries Logged`, `Subscription Length (Months)`        |


---


## ⚙️ 최종 컬럼 및 시각화


### 상관계수 히트맵
<img width="1273" height="1048" alt="image" src="https://github.com/user-attachments/assets/16f566a9-ffba-4c08-b54c-23bf6d417ad7" />

```markdown
1. 가격 대비 부담률(Price_Burden_Ratio)과 소득(Income_group): (-0.7)소득이 낮을수록 가격 부담률이 높고 이탈률과 연관 가능

2. 고객 만족도(Customer Satifaction Score)와 1달러당 만족도(Satisfaction_per_Dollar): (0.76)가격 대비 만족도가 낮은 사용자 이탈률 높음

3. 구독기간(Subscription Length)과 월 평균 문의 수(Queries_per_Month): (-0.51)구독기간이 길수록 월 평균 문의 수는 낮음

4. 시청 시간대(Time_group)과 1달러당 시청시간(Watch_Time_per_Dollar): (0.72)시청 시간 대비 가성비 낮은 사용자 이탈률 높음
```

### 월 소득 대비 가격 부담률(Price_Burden_Ratio)과 소득(Income_group)
<div align="center">
<img width="712" height="556" alt="image" src="https://github.com/user-attachments/assets/e38e867d-8bfb-4169-b8bc-fa974ee05c4b" />
</div>

---

### 고객 특성별 이탈/잔류 수 분포
<img width="1783" height="2484" alt="image" src="https://github.com/user-attachments/assets/2edc199f-0b22-4f80-92b2-a8b3777eb17b" />

### 고객 특성별 이탈률 비교
<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/c5cb9c16-519a-41c4-9cea-a3488d8b3eb3" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/31db387b-2249-4196-930f-96df8ebfb7bf" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/fa44a14f-5312-4c47-8db0-15aa44172cea" width="300"></td>
  </tr>
</table>


```markdown
1. 지원 문의 수(Support Queries): 문의가 많을수록 이탈률이 높음
	- 지원 문의 많은 사용자 → 불만족 징후 보임

2. 연령대(Age_group): 젊은층일수록 이탈율이 높음
```

---

### 고객 속성 조합별 이탈률 분석
<img width="1740" height="1383" alt="image" src="https://github.com/user-attachments/assets/a728bc5d-2cf6-4f56-a152-394396363694" />

```markdown
1. 장르 × 기기: Comedy + Laptop, Documentary + Laptop 조합에서 상대적으로 이탈률 높음

2. 지역 × 구독 플랜: Europe + Premium 조합에서 이탈률 상대적으로 높음

3. 결제 이력 × 구독 플랜: Delayed + Premium 사용자 이탈률 높음

→ 프리미엄 사용자 이탈 주의

4. 연령대 × 장르: 10~20대는 전 장르에서 거의 100%에 가까운 이탈률을 보이고 70대 이상은 Sci-Fi/Documentary 장르에서 상대적으로 낮은 이탈율을 보임
```


---

## 🤖 머신러닝 학습 결과서

- **모델**: LightGBM
- **평가 지표:**
    
    | 지표 | 점수 |
    | --- | --- |
    | 정확도 (Accuracy) | 67% |
    | 정밀도 (Precision) | 96% |
    | 재현율 (Recall) | 66% |
    | F1 Score | 78% |
  
- **주요 피처:**

    | Feature | 중요도 |
    |---------|--------|
    | Age Group (연령대) | <span style="color:red">★★★★★</span> |
    | Promotional Offers Used (쿠폰 사용 횟수) | <span style="color:orange">★★★★★</span> |
    | Support Queries Logged (총 문의 수) | <span style="color:green">★★★★☆</span> |
    | Queries Per Month (월별 문의 수) | <span style="color:green">★★★☆☆</span> |
    | Genre Preference (선호 장르) | <span style="color:green">★★★☆☆</span> |
    | Subscription Length (구독 기간) | <span style="color:green">★★☆☆☆</span> |
    | Monthly Income (월 소득) | <span style="color:green">★★☆☆☆</span> |
    | Price_Burden_Ratio (월 소득 대비 부담률) | <span style="color:green">★★☆☆☆</span> |
    | Engagement Rate (참여도) | <span style="color:green">★★☆☆☆</span> |

- **예측 결과 분포 확인**
  
<div align="center">
<img width="1064" height="719" alt="image" src="https://github.com/user-attachments/assets/cfffc7b6-3023-4897-b215-f5ef1a56c0fd" />
</div>


- **임계치에 따른 성능 지표 변화**
<div align="center">
<img width="845" height="552" alt="image" src="https://github.com/user-attachments/assets/aa00c741-9e25-4899-81f9-f922f039aca4" />
</div>

---

## 🧪 수행 결과

- **Streamlit:**
    - 예측 확률 및 실제 이탈 여부 비교
    <img width="1878" height="768" alt="image" src="https://github.com/user-attachments/assets/d31eca55-6b34-4524-875d-403e1b62bc30" />
	<img width="1870" height="917" alt="image" src="https://github.com/user-attachments/assets/b7e70a0b-ebeb-4804-b7c8-75736ef1cc6f" />
	<img width="1880" height="463" alt="image" src="https://github.com/user-attachments/assets/c1f4012d-fc55-4ec2-b55f-6b248e37585a" />
	<img width="1889" height="953" alt="image" src="https://github.com/user-attachments/assets/5fd43521-1ea8-4b18-b295-505663ae2c61" />



- **주요 인사이트:**
    - (인사이트)
    

---

## 💬 한 줄 회고


---


