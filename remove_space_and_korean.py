'''
한글 및 공백 제거
'''
import os
import re

def remove_non_ascii_and_space(text):
    ''' 
    정규표현식을 사용하여 한글 및 공백 문자 제거
    '''
    return re.sub(r'[^\x00-\x7F]', '', text).replace(' ', '')

def replace_kor_to_eng(text):
    ''' 
    정규표현식을 사용하여 한글 단어를 영어로 대체
    '''
    return re.sub(r'[가-힣]+', '', text).replace(' ', '')

def replace_kor_to_eng_folder(folder_path):
    ''' 
    폴더 내의 모든 파일을 조사하고 그림 파일명을 수정
    '''
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # 그림 파일 확장자인 경우 수정
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.tif')):
                new_filename = replace_kor_to_eng(filename)
                os.rename(file_path, os.path.join(folder_path, new_filename))
                print(f"Renamed: {filename} -> {new_filename}")