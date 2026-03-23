import streamlit as st
import pandas as pd
import time
from crewai import Agent, Task, Crew, Process
from pptx_generator import generate_pptx # Ensure this file is NOT 0 KB
from pydantic import BaseModel
from typing import List

# --- AGILISIUM DOMAIN MODELS ---
class Slide(BaseModel):
    title: str
    hero_metric: str
    key_points: List[str]

class DisplacementCanvas(BaseModel):
    specific_pain_point: str
    measurable_outcome: str
    production_pathway: str

class UIOutput(BaseModel):
    account_name: str
    competitor_name: str
    displacement_score: float
    priority_ranking: int
    canvas: DisplacementCanvas
    executive_summary: str
    slides: List[Slide]

# --- UI THEME: TAROT CARDS ---
st.set_page_config(page_title="Tarot Cards | Agilisium Arena", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #1a1814; color: #f5f2ec; }
    .stButton>button { background-color: #c84b2f; color: white; border-radius: 0px; }
    .tarot-title { font-family: 'Fraunces', serif; color: #b8860b; font-size: 42px; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="tarot-title">🃏 TAROT CARDS</div>', unsafe_allow_html=True)
st.caption("The Strategic Oracle for Competitive Displacement")

# --- CREWAI SETUP ---
def run_oracle(target, competitor):
    # Agents defined with Agilisium FDX Backstory
    researcher = Agent(
        role='Agilisium FDX Market Intelligence',
        goal=f'Identify gaps in {competitor}\'s delivery at {target}',
        backstory='Expert in Life Sciences value chains and modern DataOps.',
        verbose=True,
        allow_delegation=False
    )
    
    builder = Agent(
        role='Displacement Case Builder',
        goal='Create a 5-slide displacement strategy',
        backstory='Master of Agilisium differentiation and FDX standards.',
        verbose=True,
        allow_delegation=False
    )

    task = Task(
        description=f"Build a displacement case for {target} against {competitor}. Map Agilisium's Data Vigor and GenInsights.",
        agent=builder,
        expected_output="A structured UIOutput object.",
        output_pydantic=UIOutput
    )

    crew = Crew(agents=[researcher, builder], tasks=[task], process=Process.sequential)
    return crew.kickoff()

# --- SIDEBAR & MAIN LOGIC ---
with st.sidebar:
    st.header("Draw a Card")
    target = st.text_input("Target Account")
    comp = st.selectbox("Incumbent", ["Accenture", "Deloitte LS", "TCS"])
    
    if st.button("Reveal Fate"):
        if not st.secrets.get("OPENAI_API_KEY"):
            st.error("Oracle is powerless! Add OPENAI_API_KEY to Streamlit Secrets.")
        else:
            result = run_oracle(target, comp)
            # Save to CSV Logic here...
            st.session_state.last_result = result

# --- DISPLAY THE SPREAD ---
if 'last_result' in st.session_state:
    res = st.session_state.last_result
    st.markdown(f"## The Reading for {res.account_name}")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Disruption Score", f"{res.displacement_score}%")
    with col2:
        pptx_file = generate_pptx(res)
        st.download_button("📥 Download Strategy Deck", data=pptx_file, file_name="strategy.pptx")
