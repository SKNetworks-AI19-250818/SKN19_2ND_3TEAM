import streamlit as st
import streamlit.components.v1
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
import os, time, pickle
import chardet
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')

# 페이지 설정
st.set_page_config(
    page_title="Netflix 회원 이탈 예측 시스템",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 넷플릭스 테마 CSS
st.markdown("""
<style>
    /* 전체 배경 */
    .main {
        background-color: #ffffff;
    }
    
    /* 페이지 상단 앵커 */
    #top-anchor {
        position: absolute;
        top: 0;
        left: 0;
        width: 1px;
        height: 1px;
        visibility: hidden;
    }
    
    /* 자동 스크롤 애니메이션 */
    .scroll-to-top {
        animation: scrollToTop 0.5s ease-out;
    }
    
    @keyframes scrollToTop {
        from {
            scroll-behavior: smooth;
        }
        to {
            scroll-behavior: auto;
        }
    }
    
    /* 헤더 스타일 */
    .netflix-header {
        background: linear-gradient(90deg, #221F1F 0%, #920C12 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.3);
        color: white;
    }
    
    .netflix-title {
        color: white !important;
        font-size: 8rem !important;
        font-weight: bold;
        text-align: center;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .netflix-subtitle {
        color: #f0f0f0 !important;
        font-size: 2rem !important;
        text-align: center;
        margin: 0.5rem 0 0 0;
        font-weight: 300;
    }
    
    /* 메트릭 카드 스타일 */
    .metric-card {
        background: linear-gradient(135deg, #E50914 0%, #B81D24 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.4);
        border: 3px solid #221F1F;
    }
    
    .metric-title {
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: #f0f0f0;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* 버튼 스타일 */
    .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #B81D24 100%);
        color: white;
        border: 3px solid #221F1F;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #B81D24 0%, #E50914 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.5);
    }
    
    /* 파일 업로더 스타일 */
    .stFileUploader {
        border: 3px dashed #E50914;
        border-radius: 10px;
        padding: 2rem;
        background-color: #fafafa;
    }
    
    /* 텍스트 스타일 */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #221F1F;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .stMarkdown p {
        color: white;
        font-weight: 500;
    }
    
    /* 데이터프레임 스타일 */
    .stDataFrame {
        border: 2px solid #E50914;
        border-radius: 10px;
    }
    
    /* 차트 컨테이너 스타일 */
    .chart-box {
        background-color: #fafafa;
        border: 2px solid #221F1F;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    /* 사이드바 숨기기 */
    .css-1d391kg {
        display: none;
    }
    
    /* 프로그레스 바 스타일 */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #E50914 0%, #B81D24 100%);
    }
    
    /* 전체 화면 오버레이 */
    .loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        backdrop-filter: blur(5px);
    }
    
    /* 로딩 모달 */
    .loading-modal {
        background: linear-gradient(135deg, #221F1F 0%, #E50914 100%);
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
        border: 3px solid #E50914;
        min-width: 400px;
        animation: modalFadeIn 0.5s ease-out;
    }
    
    @keyframes modalFadeIn {
        from {
            opacity: 0;
            transform: scale(0.8);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* 로딩 텍스트 */
    .loading-text {
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* 로딩 프로그레스바 */
    .loading-progress {
        width: 100%;
        height: 20px;
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 1rem;
    }
    
    .loading-progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #ffffff 0%, #f0f0f0 100%);
        border-radius: 10px;
        transition: width 0.3s ease;
        box-shadow: 0 2px 10px rgba(255, 255, 255, 0.3);
    }
    
    /* Netflix 로고 애니메이션 */
    .loading-logo {
        font-size: 3rem;
        margin-bottom: 1rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.1);
        }
    }
</style>
""", unsafe_allow_html=True)

# 데이터 컬럼 매핑
COLUMN_MAPPING = {
    "Subscription Length (Months)": "구독기간(월)",
    "Customer Satisfaction Score (1-10)": "고객만족도(1~10)",
    "Daily Watch Time (Hours)": "일일시청시간",
    "Engagement Rate (1-10)": "참여도(1~10)",
    "Device Used Most Often": "주이용기기",
    "Genre Preference": "선호장르",
    "Region": "지역",
    "Payment History (On-Time/Delayed)": "결제이력(정시/지연)",
    "Subscription Plan": "구독플랜",
    "Churn status": "이탈여부",
    "Support Queries Logged": "지원문의(수)",
    "Age": "나이",
    "Monthly Income ($)": "월소득(달러)",
    "Promotional Offers Used": "프로모션(사용)",
    "Number of Profiles Created": "생성프로필수",
    "Age_group": "나이대",
    "Customer ID": "고객명"
}




def get_file_encoding(uploaded_file):

    """업로드된 파일 객체의 인코딩을 chardet으로 감지합니다."""
    if uploaded_file is None:
        return None
    
    # 1. 파일 포인터를 처음으로 되돌립니다.
    #    (read()를 호출하기 전에 파일의 시작 지점으로 이동)
    uploaded_file.seek(0)
    
    # 2. 파일 내용을 바이너리(바이트) 형태로 읽습니다.
    #    chardet은 인코딩 감지를 위해 바이너리 데이터가 필요합니다.
    raw_data = uploaded_file.read()
    
    # 3. 파일 포인터를 다시 처음으로 되돌립니다.
    #    (나중에 pandas 등이 파일을 읽을 수 있도록 준비)
    uploaded_file.seek(0)
    
    # 4. chardet으로 인코딩을 감지합니다.
    result = chardet.detect(raw_data)
    
    return result


def load_model():
    
    target_dir = './model'
    file_path = os.path.join(target_dir, 'churn_lgbm_pipeline.pkl')

    with open(file_path, 'rb') as f:
        model = pickle.load(f)

    return model
    

def create_sample_insights_charts():
    """메인 페이지용 인사이트 차트 생성"""
    
    # 차트 1: 이탈 요인 중요도 (샘플 데이터)
    features = ['고객만족도', '일일시청시간', '참여도', '구독기간', '지원문의건수', '월소득']
    importance = [0.25, 0.22, 0.18, 0.15, 0.12, 0.08]
    
    fig1 = go.Figure(data=[
        go.Bar(x=importance, y=features, orientation='h',
               marker=dict(color=['#E50914', '#B81D24', '#8B1538', '#6B0F2A', '#4A0A1C', '#2A050E']))
    ])
    
    fig1.update_layout(
        title="<b>주요 이탈 예측 요인</b>",
        title_font_size=20,
        title_font_color="#171717",
        xaxis_title="<b>중요도</b>",
        yaxis_title="<b>요인</b>",
        font=dict(color='#171717', size=20, family="Arial Black"),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=400,
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    # 차트 2: 구독 플랜별 이탈률 (샘플 데이터)
    plans = ['Basic', 'Standard', 'Premium']
    churn_rates = [31.8, 35.4, 32.8]
    colors = ['#E50914', '#B81D24', '#8B1538']
    
    fig2 = go.Figure(data=[
        go.Pie(labels=plans, values=churn_rates, hole=0.4,
               marker=dict(colors=colors, line=dict(color='#221F1F', width=3)))
    ])
    
    fig2.update_layout(
        title="<b>구독 플랜별 이탈률 (%)</b>",
        title_font_size=20,
        title_font_color='#221F1F',
        font=dict(color='#221F1F', size=14, family="Arial Black"),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=400,
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    return fig1, fig2

def preprocess_data(df_orgin):
    """데이터 전처리"""
    # 컬럼명 변경
    df = df_orgin.copy()
    
    # Churn status 컬럼명 변경
    df.rename(columns={'Churn status': 'Churn'}, inplace=True)

    # 10살 간격으로 연령대 컬럼 생성
    min_age = df['Age'].min()
    max_age = df['Age'].max()

    bin_from = int(np.floor(min_age / 10) * 10)
    bin_to = int(np.ceil(max_age / 10) * 10)

    bins = list(range(bin_from, bin_to + 10, 10))
    bins.append(99)
    labels = [i for i in bins[:-1]]

    df['Age_group'] = pd.cut(x=df['Age'], bins=bins, labels=labels, right=False)
    df.drop('Age', axis=1, inplace=True)

    # 지역별 가격 알아오기
    df_region_price = pd.read_csv('./data/region_price.csv')

    # 사용자 데이터와 지역별 평균 요금 데이터 결합
    df_merged = pd.merge(df, df_region_price, on='Region', how='left')


    # 실제 구독 요금 계산 컬럼 생성
    conditions = [
        (df_merged['Subscription Plan'] == 'Basic'),
        (df_merged['Subscription Plan'] == 'Standard'),
        (df_merged['Subscription Plan'] == 'Premium')
    ]
    choices = [
        df_merged['avg_region_price_basic'],
        df_merged['avg_region_price_standard'],
        df_merged['avg_region_price_premium']
    ]

    df_merged['User_Subscription_Price'] = np.select(conditions, choices, default=0)

    # 새로운 복합 컬럼 생성
    epsilon = 1e-6 # 0으로 나누는 것을 방지하기 위한 작은 값

    # 1. 소득 대비 요금
    df_merged['Price_Burden_Ratio'] = df_merged['User_Subscription_Price'] / (df_merged['Monthly Income ($)'] + epsilon)

    # 2. 요금별 시청시간(1달러당 얼마나 보는지)
    df_merged['Watch_Time_per_Dollar'] = df_merged['Daily Watch Time (Hours)'] / (df_merged['User_Subscription_Price'] + epsilon)

    # 3. 요금별 만족도
    df_merged['Satisfaction_per_Dollar'] = df_merged['Customer Satisfaction Score (1-10)'] / (df_merged['User_Subscription_Price'] + epsilon)

    # 4. 월 평균 문의 수
    df_merged['Queries_per_Month'] = df_merged['Support Queries Logged'] / (df_merged['Subscription Length (Months)'] + epsilon)

    # 무한대 값 처리
    df_merged.replace([np.inf, -np.inf], 0, inplace=True)

    return df_merged

def train_model(df):
    """머신러닝 모델 학습"""
    # 특성과 타겟 분리
    if '이탈여부' in df.columns:
        X = df.drop('이탈여부', axis=1)
        y = df['이탈여부']
        
        # 문자열을 숫자로 변환
        if y.dtype == 'object':
            le_target = LabelEncoder()
            y = le_target.fit_transform(y)
        
        # 모델 학습
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # 특성 중요도
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return model, feature_importance, X.columns
    else:
        # 이탈여부 컬럼이 없는 경우 예측용 데이터
        return None, None, df.columns

def predict_churn(model, df):
    """이탈 확률 예측"""

    x = df.drop('Churn', axis=1)
    y = df['Churn']
    # loaded_pred = loaded_pipeline.predict(x)
    proba = model.predict_proba(x)
    
    
    return proba[:, 1]

def create_result_charts(df, churn_proba, feature_importance=None):
    """결과 페이지용 차트 생성"""
    charts = {}
    
    # --- 1. 데이터 준비 및 스케일 조정 ---

    # 예시 데이터 (실제 데이터는 churn_proba를 사용하세요)
    # churn_proba가 0.0 ~ 1.0 사이의 값이라고 가정합니다.
    # 데이터를 100배하여 0~100 범위로 변환
    churn_proba_scaled = churn_proba.round(1) * 100 

    # X축 구간 설정: 0.1 단위는 스케일 조정 후 10 단위가 됩니다.
    # 0부터 100까지 10 단위로 구간을 설정 (0, 10, 20, ..., 100)
    # size=10은 10% 단위의 구간 폭을 의미합니다.
    custom_xbins = dict(start=-10, end=110, size=10)

    # --- 2. Plotly 히스토그램 생성 및 설정 ---

    fig1 = go.Figure(data=[
        go.Histogram(
            x=churn_proba_scaled,  # 스케일 조정된 데이터 사용
            xbins=custom_xbins,    # 0.1 단위에 해당하는 10 단위 구간 설정
            marker=dict(color='#E50914', line=dict(color='#221F1F', width=2))
        )
    ])

    # 레이아웃 업데이트
    fig1.update_layout(
        title="<b>고객별 이탈 확률 분포</b>",
        title_font_size=20,
        title_font_color='#221F1F',
        # X축 제목은 이제 '이탈 확률 (%)'로 변경하는 것이 좋습니다.
        xaxis_title="<b>이탈 확률 (%)</b>", 
        yaxis_title="<b>고객 수</b>",
        font=dict(color='#221F1F', size=14, family="Arial Black"),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=400
    )

    # --- 3. X축 수치 포맷을 퍼센트로 지정 ---

    # x축 수치에 '%' 기호를 붙입니다.
    # ticksuffix='%'를 사용하면 X축 틱 레이블 뒤에 '%'가 붙습니다.
    fig1.update_xaxes(
        tickformat=".0f",     # 소수점 없이 정수로 표시
        ticksuffix="%"       # 숫자 뒤에 % 추가
    )

    charts['분포'] = fig1
    
    # 2. 이탈 요인 중요도 (특성 중요도가 있는 경우)
    if feature_importance is not None:
        top_features = feature_importance.head(8).sort_values('importance', ascending=True)
        fig2 = go.Figure(data=[
            go.Bar(y=top_features['feature_ko'], x=top_features['importance'], orientation='h',
                   marker=dict(color='#E50914', line=dict(color='#221F1F', width=2)))
        ])
        fig2.update_layout(
            title="<b>이탈 예측 주요 요인</b>",
            title_font_size=20,
            title_font_color='#221F1F',
            xaxis_title="<b>중요도</b>",
            yaxis_title="<b>요인</b>",
            font=dict(color='#221F1F', size=14, family="Arial Black"),
            plot_bgcolor='white',
            paper_bgcolor='white',
            height=400
        )
        charts['중요도'] = fig2
    
    # 3. 구독플랜별 이탈률 (데이터가 있는 경우)
    if '구독플랜' in df.columns:
        plan_churn = pd.DataFrame({
            '구독플랜': df['구독플랜'],
            '이탈확률': churn_proba
        }).groupby('구독플랜')['이탈확률'].mean().sort_values(ascending=False)
        
        fig3 = go.Figure(data=[
            go.Bar(x=plan_churn.index, y=plan_churn.values,
                   marker=dict(color=['#E50914', '#B81D24', '#8B1538']))
        ])
        fig3.update_layout(
            title="<b>구독플랜별 평균 이탈 확률</b>",
            title_font_size=20,
            title_font_color='#221F1F',
            xaxis_title="<b>구독플랜</b>",
            yaxis_title="<b>평균 이탈 확률</b>",
            font=dict(color='#221F1F', size=14, family="Arial Black"),
            plot_bgcolor='white',
            paper_bgcolor='white',
            height=400
        )
        charts['플랜별'] = fig3
    
    # 4. 만족도 vs 참여도 산점도
    if '고객만족도_1_10' in df.columns and '참여도_1_10' in df.columns:
        risk_level = ['안전' if p < 0.3 else '주의' if p < 0.7 else '위험' for p in churn_proba]
        colors = ['green' if r == '안전' else 'orange' if r == '주의' else '#E50914' for r in risk_level]
        
        fig4 = go.Figure(data=[
            go.Scatter(x=df['고객만족도_1_10'], y=df['참여도_1_10'],
                      mode='markers',
                      marker=dict(color=colors, size=8, line=dict(color='#221F1F', width=1)),
                      text=[f'이탈확률: {p:.2f}' for p in churn_proba],
                      hovertemplate='만족도: %{x}<br>참여도: %{y}<br>%{text}<extra></extra>')
        ])
        fig4.update_layout(
            title="<b>고객만족도 vs 참여도 (이탈 위험도별)</b>",
            title_font_size=20,
            title_font_color='#221F1F',
            xaxis_title="<b>고객만족도</b>",
            yaxis_title="<b>참여도</b>",
            font=dict(color='#221F1F', size=14, family="Arial Black"),
            plot_bgcolor='white',
            paper_bgcolor='white',
            height=400
        )
        charts['만족도_참여도'] = fig4
    
    return charts

def main():
    # 페이지 상태 초기화
    if 'page' not in st.session_state:
        st.session_state.page = 'main'
    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'model' not in st.session_state:
        st.session_state.model = None
    if 'predictions' not in st.session_state:
        st.session_state.predictions = None
    
    # 페이지 상단 스크롤을 위한 앵커
    st.markdown('<div id="top-anchor"></div>', unsafe_allow_html=True)
    
    # 헤더
    st.markdown("""
    <div class="netflix-header">
        <h1 class="netflix-title">🎬 NETFLIX</h1>
        <p class="netflix-subtitle">회원 이탈 예측 분석 시스템</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.page == 'main':
        show_main_page()
    elif st.session_state.page == 'results':
        show_results_page()

def show_main_page():
    """메인 페이지"""
    
    st.markdown("## 📊 모델 인사이트")
    
    # 인사이트 차트
    fig1, fig2 = create_sample_insights_charts()
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            # st.markdown('<div class="chart-box">', unsafe_allow_html=True)
            st.plotly_chart(fig1, use_container_width=True)
            # st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            # st.markdown('<div class="chart-box">', unsafe_allow_html=True)
            st.plotly_chart(fig2, use_container_width=True)
            # st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 파일 업로드 섹션
    st.markdown("## 📁 데이터 업로드")
    st.markdown("### Netflix 회원 데이터를 업로드하여 이탈 위험을 분석해보세요!")
    st.markdown("**지원 형식**: Excel (.xlsx, .xls), CSV (.csv)")
    
    uploaded_file = st.file_uploader(
        "엑셀 또는 CSV 파일을 선택하세요",
        type=['xlsx', 'xls', 'csv'],
        help="Netflix 회원 데이터가 포함된 엑셀(.xlsx, .xls) 또는 CSV(.csv) 파일을 업로드하세요."
    )

    
    
    if uploaded_file is not None:
        try:

            encoding = get_file_encoding(uploaded_file)


            # 파일 확장자 확인 및 파일 읽기
            file_extension = uploaded_file.name.split('.')[-1].lower()
            
            # raise Exception()

            if file_extension == 'csv':
                # CSV 파일 읽기
                df = pd.read_csv(uploaded_file, encoding=encoding['encoding'])
            elif file_extension in ['xlsx', 'xls']:
                # 엑셀 파일 읽기
                df = pd.read_excel(uploaded_file)
            else:
                st.error("❌ 지원하지 않는 파일 형식입니다. CSV 또는 엑셀 파일을 업로드해주세요.")
                return
            
            st.success(f"✅ {file_extension.upper()} 파일이 성공적으로 업로드되었습니다! ({len(df):,}행 {len(df.columns)}열)")
            
            # 데이터 미리보기
            with st.expander("📋 데이터 미리보기"):
                st.dataframe(df.head(), use_container_width=True)
            
            # 분석 시작 버튼
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🎯 이탈 분석 시작", use_container_width=True):
                    # 오버레이 모달 시작
                    overlay_placeholder = st.empty()
                    
                    # 단계별 진행
                    with overlay_placeholder.container():
                        st.markdown("""
                        <div class="loading-overlay">
                            <div class="loading-modal">
                                <div class="loading-logo">📊</div>
                                <div class="loading-text" id="loading-text">데이터 전처리 중...</div>
                                <div class="loading-progress">
                                    <div class="loading-progress-bar" id="progress-bar" style="width: 20%;"></div>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    time.sleep(1.5)
                    
                    # 데이터 전처리
                    df_processed = preprocess_data(df)
                    
                    # 2단계 - 이탈 확률 예측
                    with overlay_placeholder.container():
                        st.markdown("""
                        <div class="loading-overlay">
                            <div class="loading-modal">
                                <div class="loading-logo">🎯</div>
                                <div class="loading-text">이탈 확률 예측 중...</div>
                                <div class="loading-progress">
                                    <div class="loading-progress-bar" style="width: 40%;"></div>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    time.sleep(1.5)

                    feature_importance = pd.DataFrame({
                        'importance': [238, 221, 22, 20, 20, 20, 19, 19, 17, 16, 16, 15, 15, 12, 11, 11, 11, 9, 9, 8, 7, 7],
                        'feature': [
                            'Subscription Length (Months)', 
                            'Customer Satisfaction Score (1-10)', 
                            'Daily Watch Time (Hours)', 
                            'Engagement Rate (1-10)', 
                            'Device Used Most Often', 
                            'Genre Preference', 
                            'Region', 
                            'Payment History (On-Time/Delayed)', 
                            'Subscription Plan', 
                            'Support Queries Logged', 
                            'Monthly Income ($)', 
                            'Promotional Offers Used', 
                            'Number of Profiles Created', 
                            'Age_group', 
                            'avg_region_price_basic', 
                            'avg_region_price_standard', 
                            'avg_region_price_premium', 
                            'User_Subscription_Price', 
                            'Price_Burden_Ratio', 
                            'Watch_Time_per_Dollar', 
                            'Satisfaction_per_Dollar', 
                            'Queries_per_Month'
                        ],
                        'feature_ko': [
                            '구독기간(개월)', 
                            '고객만족도(1~10)', 
                            '일일시청시간', 
                            '참여도(1~10)', 
                            '주이용기기', 
                            '선호장르', 
                            '지역', 
                            '결제이력(정시/지연)', 
                            '구독플랜', 
                            '지원문의 건수', 
                            '월소득(달러)', 
                            '프로모션 사용횟수', 
                            '생성프로필수', 
                            '나이', 
                            'avg_region_price_basic', 
                            'avg_region_price_standard', 
                            'avg_region_price_premium', 
                            'User_Subscription_Price', 
                            'Price_Burden_Ratio', 
                            'Watch_Time_per_Dollar', 
                            'Satisfaction_per_Dollar', 
                            'Queries_per_Month'
                        ]
                    }).sort_values('importance', ascending=False)


                    model = load_model()
                    
                    # 모델 학습 또는 예측
                    # predict_churn
                    predictions = predict_churn(model, df_processed)

                    # model, feature_importance, feature_columns = train_model(df_processed)
                    
                    # 3단계 - 팝콘 튀기는 중
                    with overlay_placeholder.container():
                        st.markdown("""
                        <div class="loading-overlay">
                            <div class="loading-modal">
                                <div class="loading-logo">🍿</div>
                                <div class="loading-text">팝콘 튀기는 중...</div>
                                <div class="loading-progress">
                                    <div class="loading-progress-bar" style="width: 60%;"></div>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    time.sleep(1.5)

                    # 4단계 - 시연 준비
                    with overlay_placeholder.container():
                        st.markdown("""
                        <div class="loading-overlay">
                            <div class="loading-modal">
                                <div class="loading-logo">🎥</div>
                                <div class="loading-text">시연 준비 중...</div>
                                <div class="loading-progress">
                                    <div class="loading-progress-bar" style="width: 80%;"></div>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    time.sleep(1.5)
                    
                    # 5단계 - 분석 완료
                    with overlay_placeholder.container():
                        st.markdown("""
                        <div class="loading-overlay">
                            <div class="loading-modal">
                                <div class="loading-logo">✅</div>
                                <div class="loading-text">분석 완료!</div>
                                <div class="loading-progress">
                                    <div class="loading-progress-bar" style="width: 100%;"></div>
                                </div>
                            </div>
                        </div>
                        <script>
                            function scrollToTop() {
                                // 여러 방법으로 스크롤 시도
                                window.parent.document.body.scrollTop = 0;
                                window.parent.document.documentElement.scrollTop = 0;
                                
                                // Streamlit 컨테이너들 찾아서 스크롤
                                const containers = [
                                    'section.main',
                                    '.main',
                                    '[data-testid="stAppViewContainer"]',
                                    '[data-testid="stApp"]'
                                ];
                                
                                containers.forEach(selector => {
                                    const element = window.parent.document.querySelector(selector);
                                    if (element) {
                                        element.scrollTop = 0;
                                        element.scrollLeft = 0;
                                    }
                                });
                                
                                // 앵커로 이동 시도
                                const anchor = window.parent.document.querySelector('#top-anchor');
                                if (anchor) {
                                    anchor.scrollIntoView({ behavior: 'instant', block: 'start' });
                                }
                                
                                // 브라우저 히스토리 조작으로 스크롤 리셋
                                if (window.parent.history.replaceState) {
                                    window.parent.history.replaceState(null, null, window.parent.location.href);
                                }
                            }
                            
                            // 즉시 실행 및 지연 실행
                            scrollToTop();
                            setTimeout(scrollToTop, 50);
                            setTimeout(scrollToTop, 100);
                            setTimeout(scrollToTop, 200);
                        </script>
                        """, unsafe_allow_html=True)
                    
                    time.sleep(0.5)
                    
                    # 오버레이 제거
                    overlay_placeholder.empty()
                    
                    # 세션 상태에 저장
                    st.session_state.data = df_processed
                    st.session_state.model = model
                    st.session_state.predictions = predictions
                    st.session_state.feature_importance = feature_importance
                    st.session_state.page = 'results'
                    

                    # # 페이지 상단으로 스크롤하는 개선된 JavaScript 코드
                    # st.components.v1.html("""
                    #     <script>
                    #         function scrollToTop() {
                    #             // 여러 방법으로 스크롤 시도
                    #             window.parent.document.body.scrollTop = 0;
                    #             window.parent.document.documentElement.scrollTop = 0;
                                
                    #             // Streamlit 컨테이너들 찾아서 스크롤
                    #             const containers = [
                    #                 'section.main',
                    #                 '.main',
                    #                 '[data-testid="stAppViewContainer"]',
                    #                 '[data-testid="stApp"]'
                    #             ];
                                
                    #             containers.forEach(selector => {
                    #                 const element = window.parent.document.querySelector(selector);
                    #                 if (element) {
                    #                     element.scrollTop = 0;
                    #                     element.scrollLeft = 0;
                    #                 }
                    #             });
                                
                    #             // 앵커로 이동 시도
                    #             const anchor = window.parent.document.querySelector('#top-anchor');
                    #             if (anchor) {
                    #                 anchor.scrollIntoView({ behavior: 'instant', block: 'start' });
                    #             }
                                
                    #             // 브라우저 히스토리 조작으로 스크롤 리셋
                    #             if (window.parent.history.replaceState) {
                    #                 window.parent.history.replaceState(null, null, window.parent.location.href);
                    #             }
                    #         }
                            
                    #         // 즉시 실행 및 지연 실행
                    #         scrollToTop();
                    #         setTimeout(scrollToTop, 50);
                    #         setTimeout(scrollToTop, 100);
                    #         setTimeout(scrollToTop, 200);
                    #     </script>
                    # """, height=0)
                    
                    st.rerun()
        
        except Exception as e:
            st.error(f"❌ 파일 처리 중 오류가 발생했습니다: {str(e)}")

def show_results_page():
    """결과 페이지"""
    
    df = st.session_state.data
    predictions = st.session_state.predictions
    feature_importance = st.session_state.feature_importance
    
    # 핵심 지표
    st.markdown("## 📈 분석 결과 요약")
    
    total_customers = len(df)
    high_risk_customers = len([p for p in predictions if p > 0.7])
    churn_risk_rate = (high_risk_customers / total_customers) * 100
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">예측대상 고객수</div>
            <div class="metric-value">{total_customers:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">이탈 위험고객</div>
            <div class="metric-value">{high_risk_customers:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">이탈 위험률</div>
            <div class="metric-value">{churn_risk_rate:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 차트 섹션
    st.markdown("## 📊 상세 분석")
    
    charts = create_result_charts(df, predictions, feature_importance)
    
    # 차트 배치
    if len(charts) >= 2:
        col1, col2 = st.columns(2)
        chart_items = list(charts.items())
        
        with col1:
            if '분포' in charts:
                with st.container():
                    # st.markdown('<div class="chart-box">', unsafe_allow_html=True)
                    st.plotly_chart(charts['분포'], use_container_width=True)
                    # st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            if '중요도' in charts:
                with st.container():
                    # st.markdown('<div class="chart-box">', unsafe_allow_html=True)
                    st.plotly_chart(charts['중요도'], use_container_width=True)
                    # st.markdown('</div>', unsafe_allow_html=True)
        
        # 추가 차트들
        remaining_charts = {k: v for k, v in charts.items() if k not in ['분포', '중요도']}
        if remaining_charts:
            for chart_name, chart_fig in remaining_charts.items():
                with st.container():
                    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
                    st.plotly_chart(chart_fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 이탈 위험 고객 리스트
    st.markdown("## 🚨 이탈 위험 고객 리스트")
    
    # 이탈 확률 추가
    df_with_prob = df.copy()
    df_with_prob['이탈확률'] = predictions
    df_with_prob['위험도'] = ['높음' if p > 0.7 else '보통' if p > 0.4 else '낮음' for p in predictions]

    for (col_name, col_name_ko) in COLUMN_MAPPING.items():
        if col_name in df_with_prob.columns:
            df_with_prob[col_name_ko] = df_with_prob[col_name]
    
    # df_with_prob['별칭'] = df_with_prob.apply(lambda row: generate_random_name(), axis=1)
    df_with_prob['월소득(달러)'].astype(object)
    df_with_prob['월소득(달러)'] = df_with_prob['월소득(달러)'].apply(lambda x: '{:,.0f}'.format(x))
    
    # 높은 위험도 고객만 필터링
    high_risk_df = df_with_prob[df_with_prob['이탈확률'] > 0.7].sort_values('이탈확률', ascending=False)


    if not high_risk_df.empty:

        st.dataframe(
            high_risk_df[['고객명', '이탈확률', '위험도', '나이대', '월소득(달러)', '구독플랜']].head(20),
            use_container_width=True
        )
        
        # 고객 상세 정보
        st.markdown("## 👤 고객 상세 분석")
        
        # 고객 선택
        customer_options = []
        for i, (idx, row) in enumerate(high_risk_df.head(10).iterrows()):
            customer_options.append(f"고객 {i+1} ({row['고객명']}) (이탈확률: {row['이탈확률']:.2%})")
        selected_customer = st.selectbox("분석할 고객을 선택하세요:", customer_options)
        
        if selected_customer:
            import re
            # clean_text = selected_customer.replace(',', '')
            # customer_idx = int(clean_text.split()[1]) - 1
            match = re.search(r'고객 (\d+)', selected_customer)
            customer_idx = int(match.group(1)) - 1 if match else 0
            
            customer_data = high_risk_df.iloc[customer_idx]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 📋 기본 정보")
                basic_info = {}
                for col in df.columns[:8]:  # 처음 8개 컬럼
                    if col in customer_data:
                        basic_info[col] = customer_data[col]
                
                for key, value in basic_info.items():
                    st.write(f"**{key}**: {value}")
            
            with col2:
                st.markdown("### 📊 추가 정보")
                additional_info = {}
                for col in df.columns[8:]:  # 나머지 컬럼
                    if col in customer_data:
                        additional_info[col] = customer_data[col]
                
                for key, value in additional_info.items():
                    st.write(f"**{key}**: {value}")
            
            # 이탈 위험 요인 분석
            st.markdown("### ⚠️ 주요 이탈 위험 요인")
            
            risk_factors = []
            
            if 'Customer Satisfaction Score (1-10)' in customer_data and customer_data['Customer Satisfaction Score (1-10)'] < 5:
                risk_factors.append("📉 낮은 고객만족도")
            
            if 'Daily Watch Time (Hours)' in customer_data and customer_data['Daily Watch Time (Hours)'] < 1:
                risk_factors.append("⏰ 낮은 시청시간")
            
            if 'Engagement Rate (1-10)' in customer_data and customer_data['Engagement Rate (1-10)'] < 5:
                risk_factors.append("📱 낮은 참여도")
            
            if 'Support Queries Logged' in customer_data and customer_data['Support Queries Logged'] > 5:
                risk_factors.append("🎧 빈번한 고객지원 문의")
            
            if risk_factors:
                for factor in risk_factors:
                    st.warning(factor)
            else:
                st.info("특별한 위험 요인이 감지되지 않았습니다.")
    
    else:
        st.info("현재 이탈 위험이 높은 고객이 없습니다.")
    
    # 메인 페이지로 돌아가기 버튼
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏠 메인 페이지로 돌아가기", use_container_width=True):
            st.session_state.page = 'main'
            
            # 페이지 상단으로 스크롤
            st.components.v1.html("""
                <script>
                    function scrollToTop() {
                        window.parent.document.body.scrollTop = 0;
                        window.parent.document.documentElement.scrollTop = 0;
                        
                        const containers = [
                            'section.main',
                            '.main',
                            '[data-testid="stAppViewContainer"]',
                            '[data-testid="stApp"]'
                        ];
                        
                        containers.forEach(selector => {
                            const element = window.parent.document.querySelector(selector);
                            if (element) {
                                element.scrollTop = 0;
                                element.scrollLeft = 0;
                            }
                        });
                        
                        const anchor = window.parent.document.querySelector('#top-anchor');
                        if (anchor) {
                            anchor.scrollIntoView({ behavior: 'instant', block: 'start' });
                        }
                    }
                    
                    scrollToTop();
                    setTimeout(scrollToTop, 50);
                    setTimeout(scrollToTop, 100);
                </script>
            """, height=0)
            
            st.rerun()

if __name__ == "__main__":
    main()