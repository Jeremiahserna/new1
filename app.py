from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set page configuration
st.set_page_config(page_title="Programming is Fun", page_icon="💻", layout="wide")

# Load local CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Make sure the path is correct.")

local_css("style/style.css")

# Load Lottie animation
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Load images
try:
    img_contact_form = Image.open("image/nn.jpg")
    img_github = Image.open("images/nn.jpg")
except FileNotFoundError:
    st.error("Image file not found. Make sure the paths are correct.")

# Header section
with st.container():
    st.subheader("Hi, I am Haidee Grace")
    st.title("Discover How Fun Computer Engineering Can Be!")
    st.write(
        """
        Welcome to my blog! Join me as I explore the exciting world of Computer Engineering.
        I'll share insights, challenges, and the joys of being a Computer Engineering student.
        """
    )
    st.write("[Message me on Gmail >](mailto:haidergrace2@gmail.com)")

# First-year perspective section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Computer Programming: First-Year Perspective")
        st.write(
            """
            Stepping into university was a mix of excitement and nerves. 
            Learning programming felt like discovering a new secret language.
            From binary to algorithms, it’s been an adventure worth experiencing!
            """
        )
        st.write("[Learn more >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Lottie animation could not load.")

# Insights and reflections
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, caption="Debugging: The Ultimate Puzzle")
    with text_column:
        st.write(
            """
            Programming assignments are thrilling and sometimes challenging. 
            Debugging feels like a daily workout, but the satisfaction of solving a problem is unmatched.
            Balancing academics, personal time, and social life is a juggling act, but organization is key.
            """
        )

# Pros and cons of programming
with st.container():
    st.write("---")
    st.subheader("PROS AND CONS")
    st.write("### PROS:")
    st.write("""
    1. Lucrative career opportunities with high demand for programmers.
    2. Develop logical thinking and problem-solving skills.
    3. Creativity in building unique solutions.
    4. Flexibility in work environments, including remote work.
    5. Continuous learning in a dynamic field.
    6. Connect with a global community of developers.
    """)
    st.write("### CONS:")
    st.write("""
    1. Steep learning curve for beginners.
    2. Sedentary work may impact physical health.
    3. Debugging can be time-consuming and frustrating.
    4. Rapid technological changes require continuous learning.
    5. Isolation in some work environments.
    6. Managing code complexity in large projects.
    """)

# Contact form section
with st.container():
    st.write("---")
    st.header("For Comments:")
    st.write("##")
    
    contact_form = """
    <form action="https://formspree.io/f/{your-form-id}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()