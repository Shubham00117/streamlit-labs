import streamlit as st
import pandas as pd
import numpy as np
import os

# Get path for banner.png relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
banner_path = os.path.join(script_dir, "banner.png")

# Prepare sample data
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=["Col A", "Col B", "Col C"]
)

sample_dict = {
    "Project": "StreamLit Basics",
    "Status": "Learning",
    "Methods": 12
}

# 1. st.write
st.header("1. st.write()")
st.write("This is `st.write()`. It handles multiple types of content like text, dataframes, and more.")

# 2. st.title
st.header("2. st.title()")
st.title("This is a Page Title")

# 3. st.header
st.header("3. st.header()")
st.header("This is a Section Header")

# 4. st.subheader
st.header("4. st.subheader()")
st.subheader("This is a Sub-section Header")

# 5. st.markdown
st.header("5. st.markdown()")
st.markdown("Streamlit supports **Markdown** for _stylized_ text, lists, and [links](https://streamlit.io).")

# 6. st.caption
st.header("6. st.caption()")
st.caption("This is a caption used for small, secondary text.")

# 7. st.code
st.header("7. st.code()")
st.code("""
import streamlit as st
st.write("Hello World")
""", language="python")

# 8. st.dataframe
st.header("8. st.dataframe()")
st.dataframe(df)

# 9. st.table
st.header("9. st.table()")
st.table(df)

# 10. st.metric
st.header("10. st.metric()")
st.metric(label="Active Sessions", value="1,234", delta="+12%")

# 11. st.image
st.header("11. st.image()")
if os.path.exists(banner_path):
    st.image(banner_path, caption="Demo Image")
else:
    st.warning("banner.png not found. Please ensure it's in the same directory.")

# 12. st.json
st.header("12. st.json()")
st.json(sample_dict)
