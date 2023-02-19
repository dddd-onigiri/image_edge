import streamlit as st
import numpy as np
import cv2

st.title('イメージエッジa')

# 画像をアップロード
image_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if image_file is not None:
    # アップロードされた画像を読み込み
    img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), 1)

    # 画像をグレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # エッジ検出
    edges = cv2.Canny(gray, 100, 200)

    # エッジ画像を表示
    st.image(edges, caption='Edge detection', use_column_width=True)
