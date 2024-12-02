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
st.set_page_config(page_title="My Webpage", page_icon="💻", layout="wide")

# Load local CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Ensure the file exists at the specified path.")

local_css("style/style.css")

# Load Lottie animation
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Load images
img_contact_form = None
img_github = None
try:
    img_contact_form = Image.open("jeremiahh.jpg")
    img_github = Image.open("jeremiahh.jpg")
except FileNotFoundError as e:
    st.error(f"Image file not found: {e}")

# Header section
with st.container():
    st.subheader("Hi, I am Jeremiah Serna")
    st.title("The Computer Engineering Journey: Follow My Blog for Insights and Inspiration")
    st.write(
        """
        Welcome to my blog! Are you curious about Computer Engineering? I'm here to share my journey, from coding challenges to exciting breakthroughs. Join me as we explore the world of technology together, from cutting-edge innovations to the everyday problem-solving that shapes our digital world. Whether you're a beginner or a seasoned pro, there's something here for everyone.
        """
    )
    st.write("[Contact me via Gmail ](mailto:jeremiahserna33@gmail.com)")

# First-year perspective section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("First-Year Insights into Computer Programming")
        st.write(
            """
            Starting university brought a blend of anticipation and curiosity. Diving into programming felt like unlocking a hidden code to the digital world. From simple logic to complex algorithms, it’s been a thrilling journey of discovery!
            """
        )
        st.write("[Learn more >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Lottie animation could not load. Please check the URL.")

# Insights and reflections
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if img_contact_form:
            st.image(img_contact_form, caption="Debugging: Take everything as a challenge")
        else:
            st.error("Image not loaded.")
    with text_column:
        st.write(
            """
            Speaking of courses, oh, the rollercoaster of emotions that comes with programming assignments! The thrill of solving problems mixed with the occasional dread of tackling bugs kept me on my toes. Debugging became my mental workout, and nothing compares to the euphoria of squashing a stubborn bug after hours of trial and error.  

            The challenge of balancing academics, social life, and personal growth is real, but it’s a dance I’ve learned to master with the help of organization and time management—my ultimate companions on this journey.  

            The freshman year of computer engineering is a whirlwind adventure—a blend of curiosity, obstacles, and countless moments of discovery.  

            Every snippet of code I write brings me closer to unraveling the fascinating intricacies of technology and innovation.  

            So, to all aspiring freshmen or budding tech enthusiasts, I invite you to embark on this incredible journey. Together, let’s decode the mysteries of computer engineering, one project and one bug at a time!  
            """
        )

# Pros and cons of programming
with st.container():
    st.write("---")
    st.subheader("PROS AND CONS")
    st.write("### PROS:")
    st.write("""
    1. Diverse career opportunities with high earning potential.
    2. Strengthens logical reasoning and structured thinking.
    3. Empowers creativity through designing and coding projects.
    4. Flexible work styles, including freelance and remote options.
    5. Endless opportunities to learn and grow in a fast-evolving field.
    6. Join a supportive and innovative global tech community.
    """)
    st.write("### CONS:")
    st.write("""
    1. Can be daunting for newcomers due to complex concepts.
    2. Long hours of screen time can strain health and posture.
    3. Debugging challenges can be mentally exhausting.
    4. Constant need to stay updated with emerging trends and tools.
    5. Risk of feeling isolated in solitary work settings.
    6. Managing large-scale projects requires significant effort and focus.
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
        st.markdown(contact_form.replace("{your-form-id}", "YOUR_ACTUAL_FORM_ID"), unsafe_allow_html=True)
    with right_column:
        st.empty()


    


   
