import streamlit as st
import base64
from urllib.parse import quote

# ============================================================
# MTE — Air Conditioning & Refrigeration
# Self-contained Streamlit company portfolio
# ============================================================

st.set_page_config(
    page_title="MTE | Air Conditioning & Refrigeration",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# COMPANY CONFIGURATION
# Edit only these values if you need to update contact details.
# ------------------------------------------------------------
COMPANY_NAME = "MTE"
COMPANY_EN = "MTE Air Conditioning & Refrigeration"
COMPANY_AR = "مؤسسة MTE للتبريد والتكييف"

EMAIL = "info@mte-ac.com"  # Replace with the company's real email
PHONE_1 = "0599905221"      # Replace with the exact number from your business card
PHONE_2 = "0507635181"      # Replace with the exact number from your business card

ADDRESS_EN = "Al Rabwah, Al Dhahr Al Ghafari Street, Riyadh, Saudi Arabia"
ADDRESS_AR = "الرياض، حي الربوة، شارع ابن ذي الغفار، المملكة العربية السعودية"

MAP_QUERY = quote(ADDRESS_EN)
MAP_URL = f"https://www.google.com/maps/search/?api=1&query={MAP_QUERY}"
EMAIL_URL = f"mailto:{EMAIL}"
PHONE_URL_1 = f"tel:{PHONE_1}"
PHONE_URL_2 = f"tel:{PHONE_2}"
WHATSAPP_URL = f"https://wa.me/{PHONE_1.replace('+', '').replace(' ', '').replace('-', '')}"

# ------------------------------------------------------------
# TRANSLATIONS
# ------------------------------------------------------------
T = {
    "en": {
        "nav_home": "Home",
        "nav_about": "About Us",
        "nav_services": "Services",
        "nav_projects": "Projects",
        "nav_contact": "Contact",
        "hero_badge": "Professional HVAC Solutions",
        "hero_title": "Reliable Cooling. Comfortable Spaces.",
        "hero_text": (
            "Professional air-conditioning and refrigeration solutions "
            "for residential, commercial and industrial environments."
        ),
        "view_services": "Explore Services",
        "contact_us": "Contact Us",
        "about_title": "About MTE",
        "about_text": (
            "MTE specializes in air-conditioning and refrigeration services, "
            "with a practical focus on installation, maintenance, troubleshooting "
            "and dependable cooling performance."
        ),
        "service_title": "Our Services",
        "service_intro": "Complete HVAC support from installation to preventive maintenance.",
        "s1": "Air Conditioning",
        "s1d": "Installation, servicing, troubleshooting and performance checks for AC systems.",
        "s2": "Refrigeration",
        "s2d": "Cooling and refrigeration support for commercial and specialized environments.",
        "s3": "Preventive Maintenance",
        "s3d": "Scheduled inspections designed to reduce breakdowns and improve system life.",
        "s4": "Repair & Troubleshooting",
        "s4d": "System diagnostics, fault identification and practical repair solutions.",
        "s5": "HVAC Installation",
        "s5d": "Professional installation support with attention to safety and system efficiency.",
        "s6": "System Inspection",
        "s6d": "Performance checks, airflow review and general HVAC condition assessment.",
        "projects_title": "What We Work On",
        "p1": "Residential Cooling",
        "p2": "Commercial HVAC",
        "p3": "Refrigeration Systems",
        "p4": "Maintenance Programs",
        "why_title": "Why Choose MTE",
        "w1": "Professional Service",
        "w1d": "Clear communication and service-focused support.",
        "w2": "Practical Solutions",
        "w2d": "Solutions focused on reliable operation and customer needs.",
        "w3": "Maintenance Mindset",
        "w3d": "Preventive care to help systems operate efficiently.",
        "contact_title": "Contact MTE",
        "contact_text": "Need a quotation, maintenance visit or technical assistance? Get in touch.",
        "email": "Email Us",
        "call1": "Call Now",
        "call2": "Call Number 2",
        "directions": "Get Directions",
        "whatsapp": "WhatsApp",
        "address": "Address",
        "phone": "Phone",
        "email_label": "Email",
        "request_title": "Request a Service",
        "name": "Your Name",
        "service": "Service Required",
        "message": "Message",
        "send": "Prepare Email Request",
        "success": "Your email app should open with a prepared service request.",
        "select_service": "Select a service",
        "translation": "Language",
        "english": "English",
        "arabic": "العربية",
        "footer": "MTE Air Conditioning & Refrigeration — Professional HVAC Solutions",
        "note": "Replace the contact placeholders in the CONFIGURATION section before deployment.",
    },
    "ar": {
        "nav_home": "الرئيسية",
        "nav_about": "من نحن",
        "nav_services": "خدماتنا",
        "nav_projects": "أعمالنا",
        "nav_contact": "اتصل بنا",
        "hero_badge": "حلول تكييف وتبريد احترافية",
        "hero_title": "تبريد موثوق. مساحات أكثر راحة.",
        "hero_text": "حلول احترافية للتكييف والتبريد للمنازل والمنشآت التجارية والبيئات الصناعية.",
        "view_services": "استكشف الخدمات",
        "contact_us": "تواصل معنا",
        "about_title": "عن MTE",
        "about_text": "تتخصص MTE في خدمات التكييف والتبريد، مع التركيز على التركيب والصيانة واستكشاف الأعطال وتحقيق أداء تبريد موثوق.",
        "service_title": "خدماتنا",
        "service_intro": "دعم متكامل لأنظمة التكييف والتبريد من التركيب إلى الصيانة الوقائية.",
        "s1": "التكييف",
        "s1d": "تركيب وصيانة وفحص واستكشاف أعطال أنظمة التكييف.",
        "s2": "التبريد",
        "s2d": "دعم أنظمة التبريد للمنشآت التجارية والبيئات المتخصصة.",
        "s3": "الصيانة الوقائية",
        "s3d": "فحوصات دورية تساعد على تقليل الأعطال وإطالة عمر النظام.",
        "s4": "الإصلاح واستكشاف الأعطال",
        "s4d": "تشخيص الأنظمة وتحديد الأعطال وتقديم حلول عملية للإصلاح.",
        "s5": "تركيب أنظمة HVAC",
        "s5d": "دعم احترافي للتركيب مع الاهتمام بالسلامة وكفاءة النظام.",
        "s6": "فحص الأنظمة",
        "s6d": "فحص الأداء وتدفق الهواء والحالة العامة لنظام التكييف.",
        "projects_title": "مجالات العمل",
        "p1": "تبريد سكني",
        "p2": "تكييف تجاري",
        "p3": "أنظمة التبريد",
        "p4": "برامج الصيانة",
        "why_title": "لماذا MTE",
        "w1": "خدمة احترافية",
        "w1d": "تواصل واضح ودعم يركز على الخدمة.",
        "w2": "حلول عملية",
        "w2d": "حلول تركز على التشغيل الموثوق واحتياجات العميل.",
        "w3": "نهج الصيانة",
        "w3d": "العناية الوقائية للمساعدة في تشغيل الأنظمة بكفاءة.",
        "contact_title": "تواصل مع MTE",
        "contact_text": "تحتاج إلى عرض سعر أو زيارة صيانة أو مساعدة فنية؟ تواصل معنا.",
        "email": "راسلنا",
        "call1": "اتصل الآن",
        "call2": "الاتصال بالرقم 2",
        "directions": "الاتجاهات",
        "whatsapp": "واتساب",
        "address": "العنوان",
        "phone": "الهاتف",
        "email_label": "البريد الإلكتروني",
        "request_title": "طلب خدمة",
        "name": "الاسم",
        "service": "الخدمة المطلوبة",
        "message": "الرسالة",
        "send": "تجهيز طلب بالبريد",
        "success": "سيتم فتح تطبيق البريد مع طلب خدمة جاهز.",
        "select_service": "اختر الخدمة",
        "translation": "اللغة",
        "english": "English",
        "arabic": "العربية",
        "footer": "MTE للتكييف والتبريد — حلول HVAC احترافية",
        "note": "قم بتعديل أرقام الاتصال والبريد في قسم CONFIGURATION قبل النشر.",
    },
}

# ------------------------------------------------------------
# SESSION LANGUAGE
# ------------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# Sidebar language control
with st.sidebar:
    st.markdown("### 🌐 Language")
    selected = st.radio(
        "Portfolio Language",
        ["English", "العربية"],
        index=0 if st.session_state.lang == "en" else 1,
        label_visibility="collapsed",
    )
    st.session_state.lang = "en" if selected == "English" else "ar"

lang = st.session_state.lang
t = T[lang]
is_ar = lang == "ar"

# ------------------------------------------------------------
# CUSTOM CSS — INSPIRED BY THE PROVIDED MTE BUSINESS CARD
# White background + deep blue typography + red accents + MTE oval.
# ------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --blue: #123b8f;
    --blue-dark: #08245d;
    --red: #e32127;
    --red-dark: #b9151b;
    --ink: #172033;
    --muted: #64748b;
    --line: #dbe3ef;
    --soft: #f5f8fc;
}

html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
}

html {
    scroll-behavior: smooth;
}

.stApp {
    background: #ffffff;
}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }

/* Header */
.mte-header {
    border-bottom: 3px solid var(--blue);
    padding: 12px 0 14px 0;
    margin-bottom: 18px;
}

.mte-brand-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
}

.brand-left {
    color: var(--blue);
    font-weight: 800;
    letter-spacing: .4px;
    line-height: 1.2;
}

.brand-left .red {
    color: var(--red);
    font-size: 1.02rem;
}

.brand-left .small {
    font-size: .72rem;
    font-weight: 600;
    color: #335aa5;
}

.mte-logo {
    width: 128px;
    height: 66px;
    border: 5px solid var(--blue);
    outline: 4px solid var(--red);
    outline-offset: -10px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--red);
    font-size: 2rem;
    font-weight: 900;
    background: white;
    box-shadow: 0 3px 10px rgba(18,59,143,.10);
}

.brand-right {
    text-align: right;
    color: var(--blue);
    line-height: 1.25;
}

.brand-right .arabic {
    font-family: "Cairo", sans-serif;
    font-weight: 800;
    font-size: .95rem;
}

.brand-right .arabic-red {
    color: var(--red);
    font-size: 1.05rem;
    font-weight: 800;
}

/* Navigation */
.nav-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 10px 0 20px 0;
}

.nav-pills a {
    text-decoration: none;
    color: var(--blue);
    border: 1px solid #c9d6ea;
    border-radius: 7px;
    padding: 7px 14px;
    font-size: .86rem;
    font-weight: 600;
    background: white;
}

.nav-pills a:hover {
    color: white;
    background: var(--blue);
    border-color: var(--blue);
}

/* Hero */
.hero {
    border: 1px solid #d7e1ef;
    border-top: 6px solid var(--red);
    border-radius: 12px;
    padding: 38px 42px;
    background: linear-gradient(135deg, #ffffff 0%, #f5f8fd 100%);
    box-shadow: 0 10px 35px rgba(18,59,143,.08);
    margin-bottom: 34px;
}

.badge {
    display: inline-block;
    color: var(--blue);
    background: #eaf0fb;
    border: 1px solid #c9d8ef;
    border-radius: 999px;
    padding: 6px 12px;
    font-size: .78rem;
    font-weight: 800;
    letter-spacing: .3px;
    text-transform: uppercase;
}

.hero h1 {
    color: var(--blue-dark);
    font-size: clamp(2rem, 5vw, 3.6rem);
    line-height: 1.04;
    margin: 16px 0 12px 0;
    font-weight: 850;
}

.hero h1 span {
    color: var(--red);
}

.hero p {
    color: var(--muted);
    font-size: 1.03rem;
    line-height: 1.75;
    max-width: 760px;
}

/* Section headings */
.section {
    scroll-margin-top: 30px;
    margin: 50px 0;
}

.section-kicker {
    color: var(--red);
    text-transform: uppercase;
    font-weight: 800;
    letter-spacing: 1.2px;
    font-size: .75rem;
    margin-bottom: 4px;
}

.section-title {
    color: var(--blue-dark);
    font-size: 2rem;
    font-weight: 850;
    margin: 0 0 7px 0;
}

.section-subtitle {
    color: var(--muted);
    margin-bottom: 24px;
}

/* Cards */
.card {
    height: 100%;
    background: #fff;
    border: 1px solid var(--line);
    border-top: 4px solid var(--blue);
    border-radius: 10px;
    padding: 22px;
    box-shadow: 0 7px 25px rgba(15,35,70,.055);
}

.card:hover {
    border-top-color: var(--red);
    box-shadow: 0 12px 30px rgba(18,59,143,.10);
}

.card-icon {
    width: 44px;
    height: 44px;
    border-radius: 8px;
    background: #edf3fd;
    color: var(--blue);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    margin-bottom: 13px;
}

.card h3 {
    color: var(--blue-dark);
    margin: 0 0 8px 0;
    font-size: 1.08rem;
}

.card p {
    color: var(--muted);
    line-height: 1.65;
    font-size: .91rem;
}

/* Stats */
.stat {
    text-align: center;
    padding: 22px 12px;
    background: var(--soft);
    border: 1px solid var(--line);
    border-radius: 10px;
}

.stat strong {
    display: block;
    color: var(--blue);
    font-size: 1.7rem;
    font-weight: 850;
}

.stat span {
    color: var(--muted);
    font-size: .8rem;
}

/* Contact */
.contact-box {
    background: var(--blue-dark);
    color: white;
    border-radius: 12px;
    padding: 32px;
    box-shadow: 0 14px 40px rgba(8,36,93,.18);
}

.contact-box h2 {
    color: white;
}

.contact-box p {
    color: #d9e4f8;
    line-height: 1.7;
}

.contact-item {
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,.12);
}

.contact-label {
    color: #9db9ed;
    font-size: .72rem;
    text-transform: uppercase;
    font-weight: 800;
    letter-spacing: .8px;
}

.contact-value {
    color: white;
    font-size: .92rem;
    margin-top: 3px;
}

/* Streamlit buttons */
.stLinkButton > a, .stButton > button {
    border-radius: 7px !important;
    font-weight: 700 !important;
}

.stLinkButton > a {
    border: 1px solid #b9c9e2 !important;
    color: var(--blue) !important;
    background: white !important;
}

.stLinkButton > a:hover {
    border-color: var(--blue) !important;
    background: #edf3fd !important;
}

.stButton > button[kind="primary"] {
    background: var(--red) !important;
    border: 1px solid var(--red) !important;
    color: white !important;
}

.stButton > button[kind="primary"]:hover {
    background: var(--red-dark) !important;
}

/* Form */
div[data-testid="stForm"] {
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 22px;
    background: #fafcff;
}

/* Footer */
.footer {
    border-top: 1px solid var(--line);
    margin-top: 60px;
    padding: 22px 0 5px 0;
    text-align: center;
    color: #718096;
    font-size: .8rem;
}

.rtl {
    direction: rtl;
    text-align: right;
    font-family: "Cairo", sans-serif;
}

@media (max-width: 700px) {
    .hero { padding: 28px 22px; }
    .mte-brand-row { flex-direction: column; align-items: flex-start; }
    .brand-right { text-align: left; }
    .mte-logo { align-self: center; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
direction_class = "rtl" if is_ar else ""

st.markdown(
    f"""
<div class="mte-header {direction_class}">
    <div class="mte-brand-row">
        <div class="brand-left">
            <div>{COMPANY_EN}</div>
            <div class="red">Air Conditioning &amp; Refrigeration</div>
            <div class="small">Professional HVAC Services</div>
        </div>
        <div class="mte-logo">MTE</div>
        <div class="brand-right">
            <div class="arabic">مؤسسة MTE</div>
            <div class="arabic-red">للتبريد والتكييف</div>
            <div>حلول تكييف وتبريد</div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Navigation links
st.markdown(
    f"""
<div class="nav-pills {'rtl' if is_ar else ''}">
    <a href="#home">{t['nav_home']}</a>
    <a href="#about">{t['nav_about']}</a>
    <a href="#services">{t['nav_services']}</a>
    <a href="#projects">{t['nav_projects']}</a>
    <a href="#contact">{t['nav_contact']}</a>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# HERO
# ------------------------------------------------------------
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

st.markdown(
    f"""
<div class="hero {'rtl' if is_ar else ''}">
    <span class="badge">❄️ {t['hero_badge']}</span>
    <h1>{t['hero_title'].replace(" ", " ", 1)}</h1>
    <p>{t['hero_text']}</p>
</div>
""",
    unsafe_allow_html=True,
)

hero_c1, hero_c2, hero_c3 = st.columns(3)
with hero_c1:
    st.link_button("📞 " + t["call1"], PHONE_URL_1, use_container_width=True)
with hero_c2:
    st.link_button("✉️ " + t["email"], EMAIL_URL, use_container_width=True)
with hero_c3:
    st.link_button("📍 " + t["directions"], MAP_URL, use_container_width=True)

# ------------------------------------------------------------
# ABOUT
# ------------------------------------------------------------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown(
    f"""
<div class="section {'rtl' if is_ar else ''}">
    <div class="section-kicker">MTE</div>
    <div class="section-title">{t['about_title']}</div>
    <div class="section-subtitle">{t['about_text']}</div>
</div>
""",
    unsafe_allow_html=True,
)

a1, a2, a3, a4 = st.columns(4)
stats = [
    ("HVAC", "Specialized"),
    ("AC", "Solutions"),
    ("24/7", "Service Mindset"),
    ("MTE", "Professional"),
]
for col, (big, small) in zip([a1, a2, a3, a4], stats):
    with col:
        st.markdown(
            f'<div class="stat"><strong>{big}</strong><span>{small}</span></div>',
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------
# SERVICES
# ------------------------------------------------------------
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
st.markdown(
    f"""
<div class="section {'rtl' if is_ar else ''}">
    <div class="section-kicker">MTE SERVICES</div>
    <div class="section-title">{t['service_title']}</div>
    <div class="section-subtitle">{t['service_intro']}</div>
</div>
""",
    unsafe_allow_html=True,
)

services = [
    ("❄️", t["s1"], t["s1d"]),
    ("🧊", t["s2"], t["s2d"]),
    ("🛠️", t["s3"], t["s3d"]),
    ("🔧", t["s4"], t["s4d"]),
    ("🏢", t["s5"], t["s5d"]),
    ("📋", t["s6"], t["s6d"]),
]

for start in range(0, len(services), 3):
    cols = st.columns(3)
    for col, (icon, title, desc) in zip(cols, services[start:start + 3]):
        with col:
            st.markdown(
                f"""
<div class="card {'rtl' if is_ar else ''}">
    <div class="card-icon">{icon}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
</div>
""",
                unsafe_allow_html=True,
            )
    st.write("")

# ------------------------------------------------------------
# PROJECT / WORK AREAS
# ------------------------------------------------------------
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown(
    f"""
<div class="section {'rtl' if is_ar else ''}">
    <div class="section-kicker">CAPABILITIES</div>
    <div class="section-title">{t['projects_title']}</div>
</div>
""",
    unsafe_allow_html=True,
)

project_items = [
    ("🏠", t["p1"]),
    ("🏬", t["p2"]),
    ("🧊", t["p3"]),
    ("⚙️", t["p4"]),
]
pcols = st.columns(4)
for col, (icon, title) in zip(pcols, project_items):
    with col:
        st.markdown(
            f"""
<div class="card {'rtl' if is_ar else ''}">
    <div class="card-icon">{icon}</div>
    <h3>{title}</h3>
</div>
""",
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------
# WHY US
# ------------------------------------------------------------
st.markdown(
    f"""
<div class="section {'rtl' if is_ar else ''}">
    <div class="section-kicker">OUR APPROACH</div>
    <div class="section-title">{t['why_title']}</div>
</div>
""",
    unsafe_allow_html=True,
)

why_items = [
    ("✓", t["w1"], t["w1d"]),
    ("✓", t["w2"], t["w2d"]),
    ("✓", t["w3"], t["w3d"]),
]
wcols = st.columns(3)
for col, (icon, title, desc) in zip(wcols, why_items):
    with col:
        st.markdown(
            f"""
<div class="card {'rtl' if is_ar else ''}">
    <div class="card-icon">{icon}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
</div>
""",
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------
# SERVICE REQUEST
# ------------------------------------------------------------
st.markdown(
    f"""
<div class="section {'rtl' if is_ar else ''}">
    <div class="section-kicker">QUICK CONTACT</div>
    <div class="section-title">{t['request_title']}</div>
</div>
""",
    unsafe_allow_html=True,
)

with st.form("service_request_form"):
    c1, c2 = st.columns(2)
    with c1:
        customer_name = st.text_input(t["name"])
    with c2:
        service_options = [
            t["select_service"],
            t["s1"],
            t["s2"],
            t["s3"],
            t["s4"],
            t["s5"],
            t["s6"],
        ]
        selected_service = st.selectbox(t["service"], service_options)

    customer_message = st.text_area(t["message"], height=120)
    submitted = st.form_submit_button(t["send"], type="primary", use_container_width=True)

if submitted:
    if not customer_name.strip() or selected_service == t["select_service"]:
        st.warning("Please enter your name and select a service.")
    else:
        body = (
            f"Hello MTE,%0D%0A%0D%0A"
            f"Name: {customer_name}%0D%0A"
            f"Service: {selected_service}%0D%0A"
            f"Message: {customer_message or 'No additional message.'}%0D%0A%0D%0A"
            f"Thank you."
        )
        request_url = f"mailto:{EMAIL}?subject={quote('MTE Service Request')}&body={body}"
        st.success(t["success"])
        st.link_button("✉️ Open Email App", request_url, use_container_width=True)

# ------------------------------------------------------------
# CONTACT
# ------------------------------------------------------------
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.markdown(
    f"""
<div class="section {'rtl' if is_ar else ''}">
    <div class="contact-box">
        <div class="section-kicker" style="color:#e86b70;">GET IN TOUCH</div>
        <h2>{t['contact_title']}</h2>
        <p>{t['contact_text']}</p>

        <div class="contact-item">
            <div class="contact-label">{t['address']}</div>
            <div class="contact-value">{ADDRESS_AR if is_ar else ADDRESS_EN}</div>
        </div>
        <div class="contact-item">
            <div class="contact-label">{t['phone']}</div>
            <div class="contact-value">{PHONE_1} &nbsp; | &nbsp; {PHONE_2}</div>
        </div>
        <div class="contact-item">
            <div class="contact-label">{t['email_label']}</div>
            <div class="contact-value">{EMAIL}</div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

cc1, cc2, cc3, cc4 = st.columns(4)
with cc1:
    st.link_button("✉️ " + t["email"], EMAIL_URL, use_container_width=True)
with cc2:
    st.link_button("📞 " + t["call1"], PHONE_URL_1, use_container_width=True)
with cc3:
    st.link_button("💬 " + t["whatsapp"], WHATSAPP_URL, use_container_width=True)
with cc4:
    st.link_button("🗺️ " + t["directions"], MAP_URL, use_container_width=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown(
    f"""
<div class="footer {'rtl' if is_ar else ''}">
    {t['footer']}<br>
    <span style="font-size:.72rem;">{t['note']}</span>
</div>
""",
    unsafe_allow_html=True,
)
