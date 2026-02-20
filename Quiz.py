import streamlit as st

st.title("🎵 What's Your Music Personality?")
st.write("Answer a few questions to discover your music profile!")

q1 = st.multiselect("What are your favorite genres? (Select all that apply)", #NEW
    ["Pop", "Rap", "House", "Indie", "Jazz", "Other"])

q2 = st.radio("What streaming platform do you use?", #NEW
    ["Spotify", "Apple Music", "YouTube Music", "TIDAL", "SoundCloud", "Other"])

q3 = st.number_input("On average, how many hours do you spend on a music platform per week?",
    min_value=0, max_value=168, value=0)

yearly_days = round((q3 * 52) / 24, 1)
st.write(f"🎧 This is the amount of days that you spend per year listening to music: **{yearly_days} days**")

q4 = st.radio("How do you usually discover new music?",
    ["Through social media (TikTok, Instagram, etc.)",
     "Friend or family recommendations",
     "Curated playlists / algorithm",
     "Radio or podcasts",
     "Live events / concerts",
     "Other"])

q5 = st.number_input("How many concerts or live music events do you attend per year?",
    min_value=0, max_value=365, value=0)

concert_hours = q5 * 3
st.write(f"🎤 That means you've spent roughly **{concert_hours} hours** of your life at live shows this year!")

if st.button("Get My Music Profile!"):
    if not q1:
        st.write("Select at least one genre to get your full profile!")
    elif "Jazz" in q1:
        st.subheader("You're a Jazz Fan")
        st.image("images/musicGenres/jazz.jpeg")
        st.balloons() #NEW
    elif "Indie" in q1:
        st.subheader("You're an Indie Fan")
        st.image("images/musicGenres/indie.jpeg")
        st.balloons()
    elif "Rap" in q1:
        st.subheader("You're a Rap Fan")
        st.image("images/musicGenres/rap.jpg")
        st.balloons()
    elif "House" in q1:
        st.subheader("You're a House Fan")
        st.image("images/musicGenres/house.jpg")
        st.balloons()
    elif "Pop" in q1:
        st.subheader("You're a Pop Fan")
        st.image("images/musicGenres/pop.jpg")
        st.balloons()
    else:
        st.subheader("You're a Music Explorer")

   

    st.progress(100) #NEW
