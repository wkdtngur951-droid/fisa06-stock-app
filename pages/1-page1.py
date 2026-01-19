import streamlit as st

# 출력
st.header('#출력')

st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''') # 수식
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True
st.markdown('---') 
st.markdown('---')     

hello = 1

print('hello')
st.text(hello)
st.code("print('hello')")
st.code(print('hello'))

st.markdown('---') 
st.markdown('---') 

import pandas as pd
data = pd.DataFrame([{'key':[1,2,3]}])

#입력
st.header('#입력')


s = st.button('Hit me')
if s:
    print(s)

st.data_editor(data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
data1 = '안녕'
st.download_button('On the dl', data1)


st.title("사진 찍고 저장하기")


picture = st.camera_input("Take a picture")

if picture:
    st.download_button(
        label="이미지 다운로드 (png)",
        data=picture,
        file_name="captured_image.png",
        mime="image/png"
    )




st.color_picker('Pick a color')

st.markdown('---') 
st.markdown('---') 




ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

st.image(img_list, ani_list, width=300)

