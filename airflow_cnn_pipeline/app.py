from predict import get_score

try:
    import io
    from enum import Enum
    from io import BytesIO, StringIO
    from typing import Union
    import cv2
    import numpy as np
    import pandas as pd
    import streamlit as st
    # from predict import get_score
except Exception as e:
    print(e)

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""


class FileUpload(object):

    def __init__(self):
        self.fileTypes = ["png", "jpg"]

    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.title('Acne Classifier')
        st.markdown(STYLE, unsafe_allow_html=True)
        file = st.file_uploader("Upload file", type=self.fileTypes)
        show_file = st.empty()
        if not file:
            show_file.info("Please upload a file of type: " + ", ".join(["png", "jpg"]))
            return

        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        cv2.imwrite('out.jpg', opencv_image)
        df = get_score()

        df2 = df.set_index('Issue')
        st.dataframe(df2)
        st.bar_chart(df2)

        if isinstance(file, BytesIO):
            show_file.image(file)
        else:
            data = pd.read_csv(file)
            st.dataframe(data.head(10))
        file.close()


if __name__ == "__main__":
    helper = FileUpload()
    helper.run()
