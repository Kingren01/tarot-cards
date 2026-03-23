import streamlit as st
import pandas as pd
from pptx_generator import generate_pptx
import time

# --- STYLING TAROT THEME ---
st.set_page_config(page_title=Tarot Cards  Displacement Hub, layout=wide)

st.markdown(
    style
    .main { background-color #1a1814; color #f5f2ec; }  Dark Ink & Paper Theme 
    .stButtonbutton { background-color #c84b2f; color white; border-radius 0px; border 1px solid #d4d0c8; }
    .card-container { border 1.5px solid #d4d0c8; padding 20px; margin-bottom 20px; background #1a1814; }
    .tarot-title { font-family 'Fraunces', serif; color #b8860b; font-size 32px; font-weight 700; }
    style
    , unsafe_allow_index=True)

st.markdown('div class=tarot-title🃏 TAROT CARDSdiv', unsafe_allow_index=True)
st.caption(The Strategic Oracle for Competitive Displacement — Agilisium Arena Edition)

# --- DATA PERSISTENCE (LOCAL STORAGE) ---
# We use a CSV to ensure your 'Readings' stay saved after a refresh
DB_FILE = tarot_vault.csv

def load_data()
    try
        return pd.read_csv(DB_FILE)
    except FileNotFoundError
        return pd.DataFrame(columns=[Account, Competitor, Disruption, Impact, Date])

def save_data(new_row)
    df = load_data()
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DB_FILE, index=False)

# --- SIDEBAR DRAW A NEW CARD (INPUT) ---
with st.sidebar
    st.header(Draw a New Card)
    target_account = st.text_input(Target Account Name)
    competitor = st.selectbox(Incumbent (The Shadow), [Accenture, Deloitte LS, TCS, Infosys])
    
    if st.button(Reveal the Strategy)
        with st.spinner(Consulting the FDX Oracle...)
            # This is where your CrewAI logic integrates
            time.sleep(2) 
            score = 85.0 # Simulated CrewAI output
            
            new_entry = {
                Account target_account,
                Competitor competitor,
                Disruption score,
                Impact 3x Faster Deployment Cycle via Data Vigor,
                Date time.strftime(%Y-%m-%d)
            }
            save_data(new_entry)
            st.success(fThe fate of {target_account} has been revealed.)

# --- MAIN DASHBOARD THE SPREAD ---
st.subheader(The Strategic Spread (Ranked Opportunities))

vault_df = load_data()
if not vault_df.empty
    # Ranking accounts by Disruption Score is a key Front Office requirement
    vault_df = vault_df.sort_values(by=Disruption, ascending=False)

    for idx, row in vault_df.iterrows()
        with st.container()
            st.markdown(f---)
            c1, c2, c3 = st.columns([3, 2, 2])
            with c1
                st.markdown(f### {row['Account']})
                st.caption(fIncumbent {row['Competitor']}  Analyzed {row['Date']})
            with c2
                st.metric(Disruption Potential, f{row['Disruption']}%)
            with c3
                st.write(Oracle's Insight)
                st.write(row['Impact'])
                
                # Integration for Deliverables 01 & 04
                if st.button(fGenerate Deck for {row['Account']}, key=fbtn_{idx})
                    st.info(PowerPoint generation triggered...)
else
    st.info(No cards drawn yet. Use the sidebar to begin your first displacement reading.)