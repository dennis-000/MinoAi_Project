import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import os

# Page configuration
st.set_page_config(
    page_title="MinoAI | Fun NYC Price Finder",
    page_icon="✨",
    layout="wide"
)

# Fun & Friendly Modern UI CSS
st.markdown("""
    <style>
    /* Gradient Dark Background */
    .stApp {
        background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%);
        color: #f0f0f0 !important;
    }
    
    /* Global Text Visibility */
    .stMarkdown, p, span, label {
        color: #e0e0e0 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Sidebar - Soft Black */
    [data-testid="stSidebar"] {
        background-color: #0c0c0e !important;
        border-right: 1px solid #FF5A5F;
    }

    /* Magic Title */
    .magic-title {
        background: linear-gradient(90deg, #FF5A5F, #FFB400, #FF5A5F);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 5rem;
        font-weight: 900;
        letter-spacing: -2px;
        margin-bottom: 0px;
        animation: shine 3s linear infinite;
    }
    
    @keyframes shine {
        to { background-position: 200% center; }
    }
    
    .magic-subtitle {
        color: #FFB400 !important;
        font-size: 1.6rem;
        font-weight: 300;
        margin-top: -15px;
        margin-bottom: 40px;
    }

    /* Friendly Input Cards */
    div[data-testid="stVerticalBlock"] > div:has(div.stSelectbox) {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255, 90, 95, 0.2);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    /* The "Magical" Button */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 4em;
        background: linear-gradient(45deg, #FF5A5F 0%, #FFB400 100%);
        color: white !important;
        font-size: 1.5rem;
        font-weight: 900;
        border: none;
        box-shadow: 0 10px 25px rgba(255, 90, 95, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 15px 35px rgba(255, 90, 95, 0.6);
        color: white !important;
    }
    
    /* Result Box - The "Big Reveal" */
    .big-reveal {
        background: radial-gradient(circle, #252525 0%, #151515 100%);
        padding: 60px;
        border-radius: 40px;
        text-align: center;
        border: 4px solid #FF5A5F;
        box-shadow: 0 0 50px rgba(255, 90, 95, 0.3);
        margin-top: 30px;
        animation: pop 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    @keyframes pop {
        0% { transform: scale(0.8); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }

    .price-tag {
        font-size: 7rem;
        font-weight: 950;
        color: #ffffff; 
        margin: 0;
        text-shadow: 0 0 30px rgba(255, 90, 95, 0.5);
    }

    /* Fun Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 30px;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.3rem;
        font-weight: 700;
        color: #888 !important;
    }
    .stTabs [aria-selected="true"] {
        color: #FF5A5F !important;
        border-bottom: 3px solid #FF5A5F !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the deployment package
@st.cache_resource
def load_model():
    model_path = 'minoai_deployment_v1.joblib'
    if not os.path.exists(model_path):
        return None, "Wait, the AI brain is missing! 🧠"
    try:
        return joblib.load(model_path), None
    except Exception as e:
        return None, f"Our AI is having a nap... Error: {str(e)}"

package, error_msg = load_model()

# Sidebar - Friendly & Fun
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/2560px-Airbnb_Logo_B%C3%A9lo.svg.png", width=120)
    st.markdown("---")
    st.markdown("### 👋 Hey Dennis!")
    st.write("Welcome to your magical pricing tool. Let's find some deals!")
    st.markdown("---")
    st.subheader("🤖 How smart is this?")
    st.write("I've studied **48,000+** NYC homes. I know the market better than a real estate agent!")
    st.progress(20, text="Magic Meter: 20%")

# Main Header
st.markdown('<p class="magic-title">MinoAI ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="magic-subtitle">Pick a neighborhood, find your price, win the market!</p>', unsafe_allow_html=True)

if error_msg:
    st.error(error_msg)
    st.stop()

model = package['model']
scaler = package['scaler']
le = package['label_encoder']
freq_mapping = package['freq_mapping']
features = package['features']

# Simple & Fun Tabs
tab_predict, tab_win, tab_brain = st.tabs(["� Price Finder", "🏆 Win More", "🧠 The Brain"])

with tab_predict:
    st.markdown("### �️ Step 1: Tell us about the place")
    
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            borough = st.selectbox("Which Borough?", le.classes_, help="Where in NYC?")
            room_type = st.selectbox("What's the space?", ["Entire home/apt", "Private room", "Shared room"], help="Is it a full house or just a bed?")
            availability = st.slider("Availability (Days/Year)", 0, 365, 200)
        with c2:
            neighbourhood = st.selectbox("Neighborhood", sorted(list(freq_mapping.index)))
            min_nights = st.number_input("Minimum Nights to Stay", 1, 30, 1)
            host_listings = st.number_input("How many homes does the host have?", 1, 100, 1)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📍 Step 2: Where exactly is it?")
    with st.container():
        raw_c1, raw_c2 = st.columns(2)
        with raw_c1:
            lat = st.number_input("North/South (Latitude)", value=40.7128, format="%.5f")
        with raw_c2:
            lon = st.number_input("East/West (Longitude)", value=-74.0060, format="%.5f")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### ⭐ Step 3: Reputation")
    with st.container():
        stat_c1, stat_c2 = st.columns(2)
        with stat_c1:
            reviews = st.number_input("Total Number of Reviews", 0, 1000, 25)
        with stat_c2:
            reviews_month = st.number_input("New Reviews Per Month", 0.0, 20.0, 1.5)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Large Magic Button
    if st.button("✨ FIND THE PERFECT PRICE ✨"):
        with st.status("🔮 Consulting the data spirits...", expanded=False):
            time.sleep(1.2)
            
            # Prepare Input
            input_data = {
                'latitude': lat, 'longitude': lon, 'minimum_nights': min_nights,
                'number_of_reviews': reviews, 'reviews_per_month': reviews_month,
                'calculated_host_listings_count': host_listings, 'availability_365': availability,
                'neighbourhood_group_encoded': le.transform([borough])[0],
                'neighbourhood_frequency': freq_mapping.get(neighbourhood, 0),
                'reviews_per_availability': reviews / (availability + 1),
                'high_availability': 1 if availability > 180 else 0,
                'has_reviews': 1 if reviews > 0 else 0,
                'room_type_Private room': 1 if room_type == "Private room" else 0,
                'room_type_Shared room': 1 if room_type == "Shared room" else 0
            }
            
            input_df = pd.DataFrame([input_data])[features]
            
            # Scale
            numerical_to_scale = ['latitude', 'longitude', 'minimum_nights', 'number_of_reviews', 
                                 'reviews_per_month', 'calculated_host_listings_count', 'availability_365',
                                 'reviews_per_availability', 'neighbourhood_frequency']
            input_df[numerical_to_scale] = scaler.transform(input_df[numerical_to_scale])
            
            prediction = model.predict(input_df)[0]
            
            st.markdown(f"""
                <div class="big-reveal">
                    <p style="color: #FFB400; letter-spacing: 5px; font-weight: bold;">MAGIC PRICE FOUND!</p>
                    <p class="price-tag">${prediction:.2f}</p>
                    <p style="color: #ffffff; opacity: 0.6; font-size: 1.1rem;">Recommended Nightly Rate for {neighbourhood}</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
            st.snow()

with tab_win:
    st.markdown("### 🏆 How to beat the market")
    collist1, collist2 = st.columns(2)
    with collist1:
        st.info("🏡 **Full House = Full Pockets**\n\nRenting out an entire apartment pays **2x more** than a private room. Our AI predicts a huge jump if you can offer the whole space!")
        st.success("📍 **Location is King**\n\nManhattan listings have a higher 'Floor Price'. Even small studios there can earn more than large houses in other boroughs!")
    with collist2:
        st.warning("⭐ **The 'Review' Magic**\n\nHaving just **ONE** review is better than zero. It moves you from 'Unknown' to 'Trusted' in the AI's eyes.")
        st.error("📅 **Be Available**\n\nHosts who stay open for more than **180 days** a year get much more love from our pricing model.")

with tab_brain:
    st.markdown("### 🧠 How I think...")
    st.write("I'm a **Random Forest** AI. I don't just guess—I look at thousands of examples to find patterns.")
    st.markdown("#### My Logic Stats:")
    colb1, colb2, colb3 = st.columns(3)
    colb1.metric("Homes Studied", "48,895")
    colb2.metric("Market Rules", "14")
    colb3.metric("Clarity", "20%")
    st.markdown("---")
    st.write("I am specialized for the **New York City** market. I help you find the sweet spot between being too cheap and too expensive!")

# Friendly Footer
st.markdown("<p style='text-align: center; color: #888; margin-top: 50px;'>MinoAI NYC | Built with ✨ by Dennis | v1.0</p>", unsafe_allow_html=True)
