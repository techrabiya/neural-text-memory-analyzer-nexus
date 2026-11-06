import streamlit as st

st.set_page_config(
    page_title="Advanced Multi-Layer AI Neural Memory & Text Analyzer",
    page_icon="🧠",
    layout="wide",
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #00ffcc;
        font-family: 'Courier New', monospace;
    }
    .main-title {
        color: #00ffcc;
        text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
        text-align: center;
        font-weight: bold;
        font-size: 2.2rem;
        margin-bottom: 20px;
    }
    .card {
        background-color: #121826;
        border: 1px solid #00ffcc;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00ffcc, #0077ff);
        color: #0b0f19;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px 24px;
        box-shadow: 0 0 10px #00ffcc;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #0077ff, #00ffcc);
        box-shadow: 0 0 20px #00ffcc;
        color: #ffffff;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-title">⚡ ADVANCED MULTI-LAYER AI NEURAL MEMORY & TEXT ANALYZER ⚡</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="card">
    <p style="color: #a0aec0; font-size: 1.1rem;">
    Yeh futuristic Streamlit app aapke text aur memory inputs ko analyze karta hai. 
    Neeche diye gaye fields mein apna paragraph aur keyword enter karein.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

col1, col2 = st.columns([2, 1])

with col1:
  st.markdown(
      "<h3 style='color: #00ffcc;'>📝 Text Input Matrix</h3>",
      unsafe_allow_html=True,
  )
  text_input = st.text_area(
      "Enter large paragraph or article:",
      height=200,
      placeholder="Yahan apna lamba paragraph ya article type ya paste karein...",
  )

with col2:
  st.markdown(
      "<h3 style='color: #00ffcc;'>🔑 Keyword Matrix</h3>",
      unsafe_allow_html=True,
  )
  keyword_input = st.text_input(
      "Enter target keyword:",
      placeholder="Jaise: AI, memory, data...",
  )

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 INITIALIZE NEURAL ANALYSIS"):
  if not text_input.strip() or not keyword_input.strip():
    st.warning("Warning: Neural matrix cannot process empty data!")
  else:
    words = text_input.split()
    total_words = len(words)

    clean_text = text_input.lower()
    clean_keyword = keyword_input.strip().lower()

    keyword_count = clean_text.count(clean_keyword)

    if total_words > 0:
      density = (keyword_count / total_words) * 100
    else:
      density = 0.0

    unique_words = len(set(words))
    complexity_score = min(
        100.0,
        round(
            (unique_words / max(1, total_words)) * 50
            + (len(text_input) / 100) * 2.5
            + (keyword_count * 5),
            2,
        ),
    )

    st.markdown("---")
    st.markdown(
        "<h2 style='color: #00ffcc;'>📊 Neural Analysis Results</h2>",
        unsafe_allow_html=True,
    )

    res_col1, res_col2, res_col3, res_col4 = st.columns(4)

    with res_col1:
      st.metric(label="Total Words", value=total_words)

    with res_col2:
      st.metric(label=f"Keyword Matches ('{keyword_input}')", value=keyword_count)

    with res_col3:
      st.metric(label="Keyword Density", value=f"{density:.2f}%")

    with res_col4:
      st.metric(label="AI Complexity Score", value=f"{complexity_score}/100")

    st.markdown(
        """
        <div class="card" style="margin-top: 20px;">
            <p style="color: #00ffcc; font-weight: bold;">✨ Neural Network Status: Optimized & Verified Successfully!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
