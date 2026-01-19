import streamlit as st


# 입구 파일, 이후 pages 폴더 안에 파일들 페이지로


ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# Text_input을 활용해서 검색창 만들기
# 검색창에 ani list 안 일부 단어가 일치하면 이미지 출력

txt = st.text_input('Search image',width=300)

if txt:
    for i in range(len(ani_list)):
        if txt in ani_list[i]:
            st.image(img_list[i],ani_list[i], width=300)
            