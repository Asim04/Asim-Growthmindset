import streamlit as st

st.set_page_config(page_title="Growth mindsrt project", project_icon="★")

st.title("Growth Mindset Challanging: Web App with streamlit ")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challanges, learn from mistakes, and unlock your full potential. This Ai-power help")


# Quote section
st.header("💡 Today's Growth Mindset Quotes")
st.write('"Success is not final, failer is not fatal: it is the courage to continue that count." -Winton Charchill."')

st.header("🔧 What's Your Challanges Todays?")
user_input = st.text_input("Describe a Challnge You're facing.:")


# Condition
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