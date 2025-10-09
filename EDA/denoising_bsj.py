# 문자열 유사 매칭으로 노이즈 정상화
from difflib import get_close_matches

def find_similarity(df, column, correct_categories):
    print(f"{column}: {correct_categories}")
    df[column].fillna('unknown', inplace=True)

    for i in range(len(df[column])):
        data = df[column].iloc[i]
        if data != 'unknown':
            word_normalized = data.replace('_', ' ')

            matches = get_close_matches(word_normalized, correct_categories, n=1, cutoff=0.6)
        
            if matches:
                df[column].iloc[i] = matches[0]
    
    print(df[column].isnull().sum())
    print(df[column].unique())
    
    return df