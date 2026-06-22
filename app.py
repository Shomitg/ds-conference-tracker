import streamlit as st
import pandas as pd
import datetime
import numpy as np
import streamlit.components.v1 as components
# Page configuration
st.set_page_config(
    page_title="Best Buy Data Science Conference Tracker",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Custom CSS for Best Buy Brand Colors & Modern UX (theme-aware)
st.markdown("""
    <style>
    /* Theme-aware color tokens — defaults are light mode */
    :root {
        --bby-card-bg: #ffffff;
        --bby-card-border: #e9ecef;
        --bby-card-shadow: 0 2px 8px rgba(0,0,0,0.04);
        --bby-card-shadow-hover: 0 4px 12px rgba(0,0,0,0.08);
        --bby-text-primary: #212529;
        --bby-text-secondary: #6c757d;
        --bby-text-muted: #495057;
        --bby-divider: #f1f3f5;
        --bby-accent-blue: #0046be;
        --bby-accent-blue-bright: #0046be;
        --bby-accent-yellow: #ffbc0d;
        --bby-strategy-bg: #f8f9fa;
        --bby-tab-bg: #f8f9fa;
        --bby-tab-border: #e9ecef;
        --bby-badge-open-bg: #d4edda;
        --bby-badge-open-fg: #155724;
        --bby-badge-closed-bg: #f8d7da;
        --bby-badge-closed-fg: #721c24;
        --bby-badge-plan-bg: #fff3cd;
        --bby-badge-plan-fg: #856404;
        --bby-badge-countdown-bg: #e8f0fe;
        --bby-badge-countdown-fg: #1a73e8;
        --bby-info-bg: #e8f0fe;
        --bby-info-fg: #0046be;
        --bby-info-border: #0046be;
        --bby-warn-bg: #fff3cd;
        --bby-warn-fg: #856404;
        --bby-warn-border: #ffbc0d;
    }

    /* Dark mode overrides via system preference */
    @media (prefers-color-scheme: dark) {
        :root {
            --bby-card-bg: #1c1f26;
            --bby-card-border: #2d3139;
            --bby-card-shadow: 0 2px 8px rgba(0,0,0,0.4);
            --bby-card-shadow-hover: 0 6px 16px rgba(0,0,0,0.55);
            --bby-text-primary: #f1f3f5;
            --bby-text-secondary: #adb5bd;
            --bby-text-muted: #ced4da;
            --bby-divider: #2d3139;
            --bby-accent-blue-bright: #6aa1ff;
            --bby-strategy-bg: #22262e;
            --bby-tab-bg: #22262e;
            --bby-tab-border: #2d3139;
            --bby-badge-open-bg: rgba(40, 167, 69, 0.22);
            --bby-badge-open-fg: #6fdd84;
            --bby-badge-closed-bg: rgba(220, 53, 69, 0.22);
            --bby-badge-closed-fg: #f08591;
            --bby-badge-plan-bg: rgba(255, 188, 13, 0.22);
            --bby-badge-plan-fg: #ffd24d;
            --bby-badge-countdown-bg: rgba(106, 161, 255, 0.18);
            --bby-badge-countdown-fg: #8ab4ff;
            --bby-info-bg: rgba(106, 161, 255, 0.12);
            --bby-info-fg: #8ab4ff;
            --bby-info-border: #6aa1ff;
            --bby-warn-bg: rgba(255, 188, 13, 0.12);
            --bby-warn-fg: #ffd24d;
            --bby-warn-border: #ffd24d;
        }
    }

    /* Also honor Streamlit's explicit theme attribute when present */
    [data-theme="dark"] {
        --bby-card-bg: #1c1f26;
        --bby-card-border: #2d3139;
        --bby-card-shadow: 0 2px 8px rgba(0,0,0,0.4);
        --bby-card-shadow-hover: 0 6px 16px rgba(0,0,0,0.55);
        --bby-text-primary: #f1f3f5;
        --bby-text-secondary: #adb5bd;
        --bby-text-muted: #ced4da;
        --bby-divider: #2d3139;
        --bby-accent-blue-bright: #6aa1ff;
        --bby-strategy-bg: #22262e;
        --bby-tab-bg: #22262e;
        --bby-tab-border: #2d3139;
        --bby-badge-open-bg: rgba(40, 167, 69, 0.22);
        --bby-badge-open-fg: #6fdd84;
        --bby-badge-closed-bg: rgba(220, 53, 69, 0.22);
        --bby-badge-closed-fg: #f08591;
        --bby-badge-plan-bg: rgba(255, 188, 13, 0.22);
        --bby-badge-plan-fg: #ffd24d;
        --bby-badge-countdown-bg: rgba(106, 161, 255, 0.18);
        --bby-badge-countdown-fg: #8ab4ff;
        --bby-info-bg: rgba(106, 161, 255, 0.12);
        --bby-info-fg: #8ab4ff;
        --bby-info-border: #6aa1ff;
        --bby-warn-bg: rgba(255, 188, 13, 0.12);
        --bby-warn-fg: #ffd24d;
        --bby-warn-border: #ffd24d;
    }

    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Shift everything up by removing default Streamlit top padding */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
    }
    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0) !important;
        height: 0px !important;
    }
    
    /* Best Buy Premium Header Card — graphite/slate variant */
    .bby-header-card {
        position: relative;
        overflow: hidden;
        padding: 28px 36px 26px;
        margin-bottom: 22px;
        border-radius: 18px;
        color: #f4f5f7;
        background:
            radial-gradient(900px 260px at 105% -40%, rgba(255,188,13,0.20), transparent 60%),
            radial-gradient(700px 300px at -10% 130%, rgba(255,107,53,0.16), transparent 60%),
            linear-gradient(135deg, #1a1d24 0%, #14171d 45%, #0d0f14 100%);
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow:
            0 1px 0 rgba(255,255,255,0.08) inset,
            0 14px 38px rgba(0, 0, 0, 0.55),
            0 0 0 1px rgba(255,188,13,0.10);
    }
    .bby-header-card::before {
        content: "";
        position: absolute; inset: 0;
        background:
            repeating-linear-gradient(90deg, rgba(255,255,255,0.025) 0 1px, transparent 1px 22px),
            repeating-linear-gradient(0deg,  rgba(255,255,255,0.025) 0 1px, transparent 1px 22px);
        -webkit-mask-image: linear-gradient(180deg, rgba(0,0,0,0.55), rgba(0,0,0,0));
                mask-image: linear-gradient(180deg, rgba(0,0,0,0.55), rgba(0,0,0,0));
        pointer-events: none;
    }
    .bby-header-card::after {
        content: "";
        position: absolute;
        top: -60%; right: -20%;
        width: 60%; height: 220%;
        background: radial-gradient(closest-side, rgba(255,188,13,0.18), transparent 70%);
        filter: blur(18px);
        transform: rotate(-12deg);
        pointer-events: none;
    }
    .bby-header-inner {
        position: relative;
        z-index: 1;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .bby-eyebrow {
        display: flex; align-items: center; gap: 10px;
        font-size: 11px; font-weight: 700; letter-spacing: 1.6px;
        text-transform: uppercase; color: #d6d8de;
    }
    .bby-eyebrow .dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #6fdd84;
        box-shadow: 0 0 10px rgba(111,221,132,0.7);
    }
    .bby-eyebrow .chip {
        margin-left: auto;
        font-size: 10px; font-weight: 800; letter-spacing: 1.6px;
        padding: 3px 9px; border-radius: 999px;
        color: #0a1738;
        background: linear-gradient(135deg, #ffd24d, #ffbc0d);
        box-shadow: 0 0 12px rgba(255,188,13,0.45);
    }
    .bby-title {
        font-size: 38px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.6px;
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 14px;
        line-height: 1.05;
    }
    .bby-title-text {
        background: linear-gradient(90deg, #ffffff 0%, #f0e8d6 60%, #ffd24d 100%);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .bby-badge {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 5px 12px; border-radius: 8px;
        color: #0a1738;
        background: linear-gradient(135deg, #fff200 0%, #ffd24d 100%);
        font-weight: 900; font-size: 22px; letter-spacing: 0.5px;
        box-shadow:
            0 0 0 1px rgba(255,255,255,0.35) inset,
            0 6px 22px rgba(255,188,13,0.35);
    }
    .bby-subtitle {
        font-size: 15px;
        font-weight: 400;
        margin: 4px 0 0;
        color: #a9b5e0;
        max-width: 900px;
    }
    .bby-meta {
        display: flex; flex-wrap: wrap; gap: 8px;
        margin-top: 10px;
    }
    .bby-meta .pill {
        font-size: 11px; font-weight: 700; letter-spacing: 0.6px;
        padding: 5px 10px; border-radius: 999px;
        color: #ececef;
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
    }
    .bby-meta .pill b { color: #ffd24d; font-weight: 800; }

    @media (max-width: 720px) {
        .bby-header-card { padding: 22px 22px 20px; }
        .bby-title { font-size: 28px; gap: 10px; }
        .bby-badge { font-size: 18px; padding: 4px 10px; }
    }
    
    /* Modern KPI Cards */
    .kpi-container {
        display: flex;
        gap: 20px;
        margin-bottom: 30px;
    }
    .kpi-card {
        flex: 1;
        background: var(--bby-card-bg);
        border: 1px solid var(--bby-card-border);
        padding: 20px;
        border-radius: 12px;
        box-shadow: var(--bby-card-shadow);
        transition: transform 0.2s, box-shadow 0.2s;
        border-top: 4px solid var(--bby-accent-blue-bright);
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--bby-card-shadow-hover);
    }
    .kpi-title {
        font-size: 14px;
        color: var(--bby-text-secondary);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 5px;
    }
    .kpi-value {
        font-size: 30px;
        font-weight: 700;
        color: var(--bby-text-primary);
    }
    
    /* Styled Status Badges */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-open {
        background-color: var(--bby-badge-open-bg);
        color: var(--bby-badge-open-fg);
    }
    .badge-closed {
        background-color: var(--bby-badge-closed-bg);
        color: var(--bby-badge-closed-fg);
    }
    .badge-plan {
        background-color: var(--bby-badge-plan-bg);
        color: var(--bby-badge-plan-fg);
    }
    .badge-countdown {
        background-color: var(--bby-badge-countdown-bg);
        color: var(--bby-badge-countdown-fg);
        border: 1px solid var(--bby-badge-countdown-fg);
    }
    
    /* Conference Detail Card in List View */
    .conf-card {
        background: var(--bby-card-bg);
        border: 1px solid var(--bby-card-border);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: var(--bby-card-shadow);
        transition: border-color 0.2s, box-shadow 0.2s;
    }
    .conf-card:hover {
        border-color: var(--bby-accent-blue-bright);
        box-shadow: var(--bby-card-shadow-hover);
    }
    .conf-title-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 12px;
    }
    .conf-name {
        font-size: 21px;
        font-weight: 700;
        color: var(--bby-accent-blue-bright);
        text-decoration: none;
    }
    .conf-name:hover {
        text-decoration: underline;
    }
    .conf-meta-row {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        font-size: 13px;
        color: var(--bby-text-muted);
        margin-bottom: 15px;
        padding-bottom: 12px;
        border-bottom: 1px solid var(--bby-divider);
    }
    .meta-item {
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .meta-label {
        font-weight: 600;
        color: var(--bby-text-secondary);
    }
    .strategy-box {
        background-color: var(--bby-strategy-bg);
        border-left: 4px solid var(--bby-accent-yellow); /* Best Buy Yellow Accent */
        padding: 15px;
        border-radius: 0 8px 8px 0;
        margin-top: 10px;
        color: var(--bby-text-primary);
    }
    
    /* Strategic Blueprint info cards (used in Analytics tab) */
    .blueprint-card {
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid;
    }
    .blueprint-card h5 {
        font-weight: 700;
        margin-top: 0;
    }
    .blueprint-card p {
        font-size: 13px;
        line-height: 1.6;
        margin-bottom: 0;
    }
    .blueprint-info {
        background-color: var(--bby-info-bg);
        border-left-color: var(--bby-info-border);
    }
    .blueprint-info h5 { color: var(--bby-info-fg); }
    .blueprint-info p  { color: var(--bby-text-primary); }
    .blueprint-warn {
        background-color: var(--bby-warn-bg);
        border-left-color: var(--bby-warn-border);
    }
    .blueprint-warn h5 { color: var(--bby-warn-fg); }
    .blueprint-warn p  { color: var(--bby-text-primary); }

    /* Sidebar nav heading */
    .sidebar-nav-title {
        color: var(--bby-accent-blue-bright);
        font-weight: 700;
        margin-bottom: 5px;
    }
    .sidebar-nav-subtitle {
        color: var(--bby-text-secondary);
        font-size: 13px;
    }

    /* Style tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: var(--bby-tab-bg);
        color: var(--bby-text-primary);
        border-radius: 8px 8px 0px 0px;
        border: 1px solid var(--bby-tab-border);
        border-bottom: none;
        padding: 10px 20px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--bby-accent-blue) !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Define reference current date
CURRENT_DATE = datetime.date(2026, 6, 22)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    
    # Standardize & convert dates
    df['Abstract Deadline_dt'] = pd.to_datetime(df['Abstract Deadline'], errors='coerce').dt.date
    df['Full Paper Deadline_dt'] = pd.to_datetime(df['Full Paper / Speaker Deadline'], errors='coerce').dt.date
    df['Start Date_dt'] = pd.to_datetime(df['Conference Start Date'], errors='coerce').dt.date
    df['End Date_dt'] = pd.to_datetime(df['Conference End Date'], errors='coerce').dt.date
    
    # Calculate Dynamic Status and Countdowns
    dynamic_statuses = []
    days_to_deadline = []
    days_to_abstract = []
    
    for idx, row in df.iterrows():
        deadline = row['Full Paper Deadline_dt']
        abstract_dl = row['Abstract Deadline_dt']
        orig_status = str(row['Status'])
        
        # Full Paper Countdown
        if pd.isnull(deadline):
            dynamic_statuses.append(orig_status)
            days_to_deadline.append(np.nan)
        elif deadline < CURRENT_DATE:
            dynamic_statuses.append("CLOSED")
            days_to_deadline.append(np.nan)
        else:
            diff_days = (deadline - CURRENT_DATE).days
            days_to_deadline.append(diff_days)
            if "Rolling" in orig_status:
                dynamic_statuses.append("OPEN — Rolling")
            elif "Watch" in orig_status:
                dynamic_statuses.append("OPEN — Watch CFP")
            else:
                dynamic_statuses.append("OPEN")
                
        # Abstract Countdown (on the fly)
        if pd.isnull(abstract_dl):
            days_to_abstract.append(np.nan)
        elif abstract_dl < CURRENT_DATE:
            days_to_abstract.append(-1) # past / expired
        else:
            diff_abs = (abstract_dl - CURRENT_DATE).days
            days_to_abstract.append(diff_abs)
                
    df['Computed Status'] = dynamic_statuses
    df['Days to Deadline'] = days_to_deadline
    df['Days to Abstract'] = days_to_abstract
    
    # Formatted display columns
    df['Formatted Abstract'] = df['Abstract Deadline_dt'].apply(lambda x: x.strftime('%b %d, %Y') if not pd.isnull(x) else '—')
    df['Formatted Deadline'] = df['Full Paper Deadline_dt'].apply(lambda x: x.strftime('%b %d, %Y') if not pd.isnull(x) else '—')
    df['Formatted Dates'] = df.apply(
        lambda r: f"{r['Start Date_dt'].strftime('%b %d, %Y')} to {r['End Date_dt'].strftime('%b %d, %Y')}" 
        if not pd.isnull(r['Start Date_dt']) and not pd.isnull(r['End Date_dt']) else '—', 
        axis=1
    )
    
    # Help columns for nice display inside the Grid table
    df['Days to Abstract_disp'] = df['Days to Abstract'].apply(
        lambda x: f"{int(x)} Days" if pd.notnull(x) and x >= 0 else ("Passed" if x == -1 else "—")
    )
    df['Days to Deadline_disp'] = df['Days to Deadline'].apply(
        lambda x: f"{int(x)} Days" if pd.notnull(x) and x >= 0 else ("Passed" if pd.isnull(x) else "—")
    )
    
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()


# --- HEADER SECTION ---
st.markdown("""
    <div class="bby-header-card">
        <div class="bby-header-inner">
            <div class="bby-eyebrow">
                <span class="dot"></span>
                <span>Strategic Intelligence · FY26</span>
            </div>
            <h1 class="bby-title">
                <span class="bby-title-text">Data Science Conference Tracker</span>
            </h1>
            <div class="bby-meta">
                <span class="pill">🌐 Global + 🇮🇳 India Venues</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- NEAREST DEADLINE COUNTDOWN TIMER (HTML/JS) ---
upcoming_abstracts = df[df['Abstract Deadline_dt'] >= CURRENT_DATE]
if not upcoming_abstracts.empty:
    nearest_conf = upcoming_abstracts.sort_values(by='Abstract Deadline_dt').iloc[0]
    nearest_name = nearest_conf['Conference']
    nearest_date_str = nearest_conf['Abstract Deadline'] # "2026-07-15"
    nearest_date_formatted = nearest_conf['Formatted Abstract'] # "Jul 15, 2026"
    
    timer_html = f"""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@700;800&display=swap" rel="stylesheet">
    <div class="timer-wrap">
      <div class="timer-card">
        <div class="timer-glow"></div>
        <div class="timer-head">
          <span class="live-dot"></span>
          <span class="kicker">Nearest Upcoming Abstract Deadline</span>
          <span class="chip">LIVE</span>
        </div>
        <div class="timer-title">{nearest_name}</div>
        <div class="timer-sub">Abstract due <b>{nearest_date_formatted}</b> · 23:59 local</div>
        <div id="countdown-timer" class="timer-grid">
          <div class="time-block"><span id="days"    class="time-num">00</span><span class="time-lbl">Days</span></div>
          <span class="sep">:</span>
          <div class="time-block"><span id="hours"   class="time-num">00</span><span class="time-lbl">Hours</span></div>
          <span class="sep">:</span>
          <div class="time-block"><span id="minutes" class="time-num">00</span><span class="time-lbl">Minutes</span></div>
          <span class="sep">:</span>
          <div class="time-block"><span id="seconds" class="time-num">00</span><span class="time-lbl">Seconds</span></div>
        </div>
      </div>
    </div>

    <style>
      * {{ box-sizing: border-box; }}
      .timer-wrap {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        padding: 4px 2px 10px;
      }}
      .timer-card {{
        position: relative;
        background:
          radial-gradient(1200px 200px at 110% -40%, rgba(255,188,13,0.20), transparent 60%),
          radial-gradient(800px 220px at -10% 120%, rgba(106,161,255,0.22), transparent 60%),
          linear-gradient(135deg, #0a1738 0%, #0c1e4a 45%, #061233 100%);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 18px 26px 20px;
        color: #f4f7ff;
        overflow: hidden;
        box-shadow:
          0 1px 0 rgba(255,255,255,0.06) inset,
          0 10px 30px rgba(2, 10, 36, 0.45),
          0 0 0 1px rgba(255,188,13,0.10);
      }}
      .timer-card::before {{
        content: "";
        position: absolute; inset: 0;
        background:
          repeating-linear-gradient(90deg, rgba(255,255,255,0.025) 0 1px, transparent 1px 22px),
          repeating-linear-gradient(0deg,  rgba(255,255,255,0.025) 0 1px, transparent 1px 22px);
        mask-image: linear-gradient(180deg, rgba(0,0,0,0.5), rgba(0,0,0,0));
        pointer-events: none;
      }}
      .timer-glow {{
        position: absolute;
        top: -60%; right: -20%;
        width: 60%; height: 220%;
        background: radial-gradient(closest-side, rgba(255,188,13,0.18), transparent 70%);
        filter: blur(20px);
        transform: rotate(-12deg);
        pointer-events: none;
      }}
      .timer-head {{
        display: flex; align-items: center; gap: 10px;
        font-size: 11px; font-weight: 700; letter-spacing: 1.4px;
        text-transform: uppercase;
        color: #cfd8ff;
      }}
      .kicker {{ opacity: 0.9; }}
      .chip {{
        margin-left: auto;
        font-size: 10px; font-weight: 800; letter-spacing: 1.6px;
        padding: 3px 9px; border-radius: 999px;
        color: #0a1738;
        background: linear-gradient(135deg, #ffd24d, #ffbc0d);
        box-shadow: 0 0 12px rgba(255,188,13,0.45);
      }}
      .live-dot {{
        width: 9px; height: 9px; border-radius: 50%;
        background: #ff4d4f;
        box-shadow: 0 0 0 0 rgba(255,77,79,0.7);
        animation: pulse 1.6s ease-out infinite;
      }}
      @keyframes pulse {{
        0%   {{ box-shadow: 0 0 0 0   rgba(255,77,79,0.65); }}
        70%  {{ box-shadow: 0 0 0 12px rgba(255,77,79,0); }}
        100% {{ box-shadow: 0 0 0 0   rgba(255,77,79,0); }}
      }}
      .timer-title {{
        margin: 8px 0 2px;
        font-size: 20px; font-weight: 800; letter-spacing: -0.2px;
        background: linear-gradient(90deg, #ffffff 0%, #cfd8ff 70%, #ffd24d 100%);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
      }}
      .timer-sub {{
        font-size: 12px; color: #a9b5e0; margin-bottom: 12px;
      }}
      .timer-sub b {{ color: #ffd24d; font-weight: 700; }}

      .timer-grid {{
        display: flex; align-items: center; justify-content: center; gap: 8px;
      }}
      .time-block {{
        position: relative;
        display: flex; flex-direction: column; align-items: center;
        min-width: 72px; padding: 8px 12px 6px;
        background: linear-gradient(180deg, rgba(255,255,255,0.07), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 10px;
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        box-shadow: 0 1px 0 rgba(255,255,255,0.08) inset, 0 6px 14px rgba(0,0,0,0.25);
      }}
      .time-num {{
        font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace;
        font-size: 28px; font-weight: 800;
        line-height: 1;
        color: #ffffff;
        text-shadow: 0 0 18px rgba(106,161,255,0.45);
        font-variant-numeric: tabular-nums;
      }}
      .time-lbl {{
        margin-top: 4px;
        font-size: 9px; font-weight: 700; letter-spacing: 1.4px;
        text-transform: uppercase;
        color: #a9b5e0;
      }}
      .sep {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 26px; font-weight: 800;
        color: rgba(255,188,13,0.85);
        line-height: 1; transform: translateY(-6px);
        animation: blink 1s steps(2, start) infinite;
      }}
      @keyframes blink {{
        50% {{ opacity: 0.25; }}
      }}

      .timer-closed {{
        padding: 10px 14px; border-radius: 10px;
        font-size: 13px; font-weight: 800; letter-spacing: 1px;
        color: #fff; background: linear-gradient(135deg, #b3261e, #d93025);
        box-shadow: 0 6px 18px rgba(217,48,37,0.35);
      }}

      @media (max-width: 720px) {{
        .time-block {{ min-width: 58px; padding: 6px 8px 5px; }}
        .time-num   {{ font-size: 22px; }}
        .timer-title {{ font-size: 17px; }}
        .sep        {{ font-size: 20px; }}
      }}
    </style>

    <script>
      var targetDate = new Date('{nearest_date_str}T23:59:59').getTime();
      function updateTimer() {{
        var now = new Date().getTime();
        var distance = targetDate - now;
        if (distance < 0) {{
          document.getElementById("countdown-timer").innerHTML =
            "<div class='timer-closed'>WINDOW CLOSED — PIVOT TO FULL PAPER TRACK</div>";
          return;
        }}
        var days    = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours   = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        document.getElementById("days").innerText    = String(days).padStart(2, '0');
        document.getElementById("hours").innerText   = String(hours).padStart(2, '0');
        document.getElementById("minutes").innerText = String(minutes).padStart(2, '0');
        document.getElementById("seconds").innerText = String(seconds).padStart(2, '0');
      }}
      setInterval(updateTimer, 1000);
      updateTimer();
    </script>
    """
    components.html(timer_html, height=210)


# --- SIDEBAR CONTROL PANEL ---
FILTER_KEYS = ["flt_search", "flt_focus", "flt_status", "flt_track", "flt_difficulty", "flt_score", "flt_only_india"]

def _clear_filters():
    for k in FILTER_KEYS:
        st.session_state.pop(k, None)

st.sidebar.markdown("### 🔍 Search Conferences")
search_query = st.sidebar.text_input("", placeholder="Search conferences, locations, topics...", label_visibility="collapsed", key="flt_search")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 Filters")

# Focus Area Filter
focus_areas = ["All Focus Areas"] + sorted(list(df['Focus Area'].dropna().unique()))
selected_focus_area = st.sidebar.selectbox("Focus Area", focus_areas, key="flt_focus")

# Status Filter
status_options = ["All Statuses"] + sorted(list(df['Computed Status'].dropna().unique()))
selected_status = st.sidebar.selectbox("Submission Status", status_options, key="flt_status")

# Track Filter
track_options = ["All Tracks"] + sorted(list(df['Available Tracks'].dropna().unique()))
selected_track = st.sidebar.selectbox("Available Tracks", track_options, key="flt_track")

# Acceptance Difficulty Filter
difficulty_options = ["All Difficulty Levels"] + sorted(list(df['Acceptance Difficulty'].dropna().unique()))
selected_difficulty = st.sidebar.selectbox("Acceptance Difficulty", difficulty_options, key="flt_difficulty")

# Credibility Score Slider
min_score = int(df['Credibility Score'].str.split('/').str[0].astype(int).min())
max_score = int(df['Credibility Score'].str.split('/').str[0].astype(int).max())
score_range = st.sidebar.slider("Minimum Credibility Score", min_score, max_score, min_score, key="flt_score")

# Region/India Filter
only_india = st.sidebar.checkbox("Focus on India Venues 🇮🇳", value=False, key="flt_only_india")

# Reset Button
st.sidebar.button("Clear All Filters", use_container_width=True, on_click=_clear_filters)


# --- FILTER LOGIC ---
filtered_df = df.copy()

if search_query:
    filtered_df = filtered_df[
        filtered_df['Conference'].str.contains(search_query, case=False, na=False) |
        filtered_df['Location'].str.contains(search_query, case=False, na=False) |
        filtered_df['Action Required'].str.contains(search_query, case=False, na=False) |
        filtered_df['Best Fit For Team'].str.contains(search_query, case=False, na=False)
    ]

if selected_focus_area != "All Focus Areas":
    filtered_df = filtered_df[filtered_df['Focus Area'] == selected_focus_area]

if selected_status != "All Statuses":
    filtered_df = filtered_df[filtered_df['Computed Status'] == selected_status]

if selected_track != "All Tracks":
    filtered_df = filtered_df[filtered_df['Available Tracks'] == selected_track]

if selected_difficulty != "All Difficulty Levels":
    filtered_df = filtered_df[filtered_df['Acceptance Difficulty'] == selected_difficulty]

# Filter by Credibility Score
filtered_df['numeric_score'] = filtered_df['Credibility Score'].str.split('/').str[0].astype(int)
filtered_df = filtered_df[filtered_df['numeric_score'] >= score_range]
filtered_df = filtered_df.drop(columns=['numeric_score'])

# Filter by India Region
if only_india:
    filtered_df = filtered_df[filtered_df['Location'].str.contains("India", case=False, na=False)]

# --- SORTING LOGIC ---
# Group open conferences first (0) and closed last (1), then sort by Abstract Deadline ascending
filtered_df['Is Closed'] = (filtered_df['Computed Status'] == "CLOSED").astype(int)
filtered_df = filtered_df.sort_values(
    by=['Is Closed', 'Abstract Deadline_dt'],
    ascending=[True, True],
    na_position='last'
)
filtered_df = filtered_df.drop(columns=['Is Closed'])


# --- STATS ROW ---
total_cnt = len(df)
india_cnt = len(df[df['Location'].str.contains("India", case=False, na=False)])
open_cnt = len(df[df['Computed Status'].str.contains("OPEN", case=False, na=False)])
avg_cred = df['Credibility Score'].str.split('/').str[0].astype(int).mean()

st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card">
            <div class="kpi-title">📚 Total Tracked</div>
            <div class="kpi-value">{total_cnt} Venues ({india_cnt} in India)</div>
        </div>
        <div class="kpi-card" style="border-top-color: #28a745;">
            <div class="kpi-title">🟢 Deadlines Open</div>
            <div class="kpi-value">{open_cnt} Active</div>
        </div>
        <div class="kpi-card" style="border-top-color: #ffc107;">
            <div class="kpi-title">⏳ Nearest Deadline</div>
            <div class="kpi-value">
                {int(filtered_df['Days to Deadline'].min()) if filtered_df['Days to Deadline'].notnull().any() else 'N/A'} Days
            </div>
        </div>
        <div class="kpi-card" style="border-top-color: #17a2b8;">
            <div class="kpi-title">✨ Avg Credibility</div>
            <div class="kpi-value">{avg_cred:.1f} / 10</div>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- TABS ---
main_tab1, main_tab2, main_tab3 = st.tabs(["📋 Cards View", "🔍 Grid & Table View", "📊 Portal Analytics & Insights"])

# --- TAB 1: CARDS VIEW ---
with main_tab1:
    st.markdown("### 🏆 Comprehensive Strategic View")
    st.write("A visual card-based layout ideal for reading full strategical fits, deadlines, and action plans with countdowns.")
    
    if len(filtered_df) == 0:
        st.warning("No conferences match the selected filters. Please adjust filters in the sidebar.")
    else:
        for idx, row in filtered_df.iterrows():
            with st.container(border=True):
                # Header row: Title and Status/Countdown Badges
                col_header, col_badges = st.columns([3, 1])
                with col_header:
                    st.markdown(f"### **[{row['Conference']}]({row['Official Website']})**")
                    st.caption(f"🎯 **Focus Area:** {row['Focus Area']} | 🏷️ **Tracks:** {row['Available Tracks']}")
                
                with col_badges:
                    status_val = row['Computed Status']
                    if "OPEN" in status_val:
                        st.success(f"🟢 {status_val}")
                    elif "CLOSED" in status_val:
                        st.error(f"🔴 {status_val}")
                    else:
                        st.warning(f"🟡 {status_val}")
                        
                # Metadata row (Location, Dates, Credibility, Difficulty, Entry Fee)
                col_m1, col_m2, col_m3, col_m4 = st.columns(4)
                with col_m1:
                    st.markdown(f"📍 **Location:**\n{row['Location']}")
                with col_m2:
                    st.markdown(f"📅 **Dates:**\n{row['Formatted Dates']}")
                with col_m3:
                    st.markdown(f"💎 **Credibility Score:**\n`{row['Credibility Score']}`")
                with col_m4:
                    st.markdown(f"⚖️ **Acceptance Difficulty:**\n{row['Acceptance Difficulty']}")
                
                # Deadline Countdown Alerts
                col_d1, col_m_fee = st.columns([3, 1])
                with col_d1:
                    deadlines_str = f"⏳ **Abstract Deadline:** {row['Formatted Abstract']} "
                    if pd.notnull(row['Days to Abstract']) and row['Days to Abstract'] >= 0:
                        deadlines_str += f"(`{int(row['Days to Abstract'])} Days Left` ⚠️) "
                    
                    deadlines_str += f"\n\n⏳ **Full Paper / Speaker Deadline:** {row['Formatted Deadline']} "
                    if pd.notnull(row['Days to Deadline']):
                        deadlines_str += f"(`{int(row['Days to Deadline'])} Days Left` ⚠️)"
                    st.markdown(deadlines_str)
                with col_m_fee:
                    st.markdown(f"💵 **Entry Fee (Approx.):**\n{row['Entry Fee (Approx.)']}")
                
                # Strategic Recommendation Quote Box
                st.markdown(f"""
                    > **🎯 Best Fit for Best Buy:**
                    > {row['Best Fit For Team']}
                    > 
                    > *👉 **Action required:** {row['Action Required']}*
                """)
                
                # Link Button
                st.markdown(f"""
                    <div style="text-align: right; margin-top: -10px; margin-bottom: 10px;">
                        <a href="{row['Official Website']}" target="_blank" style="background-color: #0046be; color: white; padding: 8px 18px; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; display: inline-block; box-shadow: 0 2px 4px rgba(0,70,190,0.15);">🌐 Visit Official Site</a>
                    </div>
                """, unsafe_allow_html=True)

# --- TAB 2: GRID / TABLE VIEW ---
with main_tab2:
    st.markdown("### 🔍 Advanced Interactive Grid")
    st.write("Perfect for sorting, multi-column searching, and export to CSV/Excel.")
    
    # Color formatting function for status
    def color_status_html(val):
        if 'OPEN' in str(val).upper():
            return 'background-color: #d4edda; color: #155724; font-weight: bold'
        elif 'CLOSED' in str(val).upper():
            return 'background-color: #f8d7da; color: #721c24; font-weight: bold'
        elif 'PLAN' in str(val).upper():
            return 'background-color: #fff3cd; color: #856404; font-weight: bold'
        return ''

    try:
        styled_df_tab2 = filtered_df.style.map(color_status_html, subset=['Computed Status'])
    except AttributeError:
        styled_df_tab2 = filtered_df.style.applymap(color_status_html, subset=['Computed Status'])

    st.dataframe(
        styled_df_tab2,
        column_order=[
            'Conference', 'Focus Area', 'Location', 'Formatted Abstract', 'Days to Abstract_disp',
            'Formatted Deadline', 'Days to Deadline_disp', 'Formatted Dates', 'Computed Status', 
            'Available Tracks', 'Acceptance Difficulty', 'Credibility Score', 'Official Website'
        ],
        use_container_width=True,
        hide_index=True,
        column_config={
            "Conference": st.column_config.TextColumn("Conference Name", width="medium"),
            "Focus Area": st.column_config.TextColumn("Focus Area", width="small"),
            "Location": st.column_config.TextColumn("Location", width="small"),
            "Formatted Abstract": st.column_config.TextColumn("Abstract Deadline", width="small"),
            "Days to Abstract_disp": st.column_config.TextColumn("Abstract Countdown", width="small"),
            "Formatted Deadline": st.column_config.TextColumn("Submission Deadline", width="small"),
            "Days to Deadline_disp": st.column_config.TextColumn("Paper Countdown", width="small"),
            "Formatted Dates": st.column_config.TextColumn("Dates", width="small"),
            "Computed Status": st.column_config.TextColumn("Status", width="small"),
            "Available Tracks": st.column_config.TextColumn("Tracks", width="small"),
            "Acceptance Difficulty": st.column_config.TextColumn("Difficulty", width="small"),
            "Credibility Score": st.column_config.TextColumn("Credibility Score", width="small"),
            "Official Website": st.column_config.LinkColumn("Website", width="small")
        }
    )

    st.markdown("---")
    # Quick export button
    export_df = filtered_df.drop(columns=[
        'Abstract Deadline_dt', 'Full Paper Deadline_dt', 'Start Date_dt', 'End Date_dt',
        'Formatted Abstract', 'Formatted Deadline', 'Formatted Dates',
        'Days to Abstract_disp', 'Days to Deadline_disp', 'Days to Abstract', 'Days to Deadline'
    ], errors='ignore')
    csv_data = export_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Current Filtered Table to CSV",
        data=csv_data,
        file_name="best_buy_filtered_conferences.csv",
        mime="text/csv",
        use_container_width=True
    )

# --- TAB 3: ANALYTICS & INSIGHTS ---
with main_tab3:
    st.markdown("### 📊 Portal Analytics")
    st.write("High-level breakdown of conference data to align publishing quotas and team budgets.")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### 🎯 Distribution by Focus Area")
        focus_counts = df['Focus Area'].value_counts()
        st.bar_chart(focus_counts, color="#0046be")
        
    with col_chart2:
        st.markdown("#### ⚖️ Venues by Acceptance Level")
        difficulty_counts = df['Acceptance Difficulty'].value_counts()
        st.bar_chart(difficulty_counts, color="#ffbc0d")

    st.markdown("---")
    st.markdown("### 💡 Recommended Strategic Blueprint for Best Buy DS Teams")
    
    blueprint_col1, blueprint_col2 = st.columns(2)
    with blueprint_col1:
        st.markdown("""
            <div class="blueprint-card blueprint-info">
                <h5>🇮🇳 High ROI Local Indian Venues</h5>
                <p>
                    <b>CODS-COMAD 2027</b> (Kolkata) and <b>HiPC 2026/2027</b> (Bengaluru) are India's absolute gold standards. 
                    Submitting papers to these local venues offers <b>world-class credibility (ACM/IEEE index)</b> while optimizing travel and logistics costs for our local engineers.
                </p>
            </div>
        """, unsafe_allow_html=True)
    with blueprint_col2:
        st.markdown("""
            <div class="blueprint-card blueprint-warn">
                <h5>🌐 Global Multimodal & NLP Venues</h5>
                <p>
                    For visual search, try-on, and conversational AI, plan heavily for <b>ACL 2027</b> and <b>CVPR 2027</b>. 
                    Always aim to target the <b>Datasets & Benchmarks</b> or <b>Workshop tracks</b> first as they have significantly higher acceptance levels for industry teams.
                </p>
            </div>
        """, unsafe_allow_html=True)
