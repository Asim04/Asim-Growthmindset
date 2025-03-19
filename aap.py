import streamlit as st

# Page configuration
st.set_page_config(page_title="Growth mindsrt project", page_icon="★")

# Title with a green-colored line below it
st.title("☪    Growth Mindset Web App  ")

st.markdown(
    """
    <hr style="border: 2px solid green; margin-top: 0px; margin-bottom: 20px;">
    """,
    unsafe_allow_html=True
)

# Header and introduction
st.header("🚀 Welcome to Your Growth Journey!")
st.write("""Embrace challanges, learn from mistakes, and unlock your full potential.
          This Ai-powered helps you build s **growth mindset** with reflection,
          challanges, and achivements!🌟 """)


# Quote section
st.header("💡 Today's Growth Mindset Quotes")
st.write('"Success is not final, failer is not fatal: it is the courage to continue that count." -Winton Charchill."')

st.header("🔧 What's Your Challanges Todays?")
user_input = st.text_input("Describe a Challnge You're facing.:")


# Condition for user input
if user_input:
    st.success(f"💪You're facing: {user_input}.  Keep pusing forward towords your goal!🚀")
else:
    st.warning("Tell us about you challange to get started!")

# Reflection
st.header(" Reflect on Your Learning ")
reflection = st.text_area("Write Your reflection here: ")

if reflection:
    st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past you experince help you Growth! shear your difficulties")


# Acheviement 
st.header("🏆 Celebrate You'r Wins!")
acheviement = st.text_input("Shear Something you've recently accomplihed:")

if acheviement:
    st.success("🌠 Amazing! You Achived: {acheviement}")
else:
    st.info("Big or small, every achevimment counts! Share one now 😍")


# Footer
st.write("- - -")
st.write("🚀 keep beliving in yourself. Growth is Journey, not a destination! 🌟")
st.write(" © create by Muhammad Asim khan ")