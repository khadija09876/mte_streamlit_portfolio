import streamlit as st
from urllib.parse import quote

# ============================================================
# MTE — AIR CONDITIONING & REFRIGERATION
# Professional Streamlit Company Portfolio
# ============================================================

st.set_page_config(
    page_title="MTE | Air Conditioning & Refrigeration",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# COMPANY CONFIGURATION
# ============================================================

COMPANY_NAME = "MTE"
COMPANY_EN = "MTE Air Conditioning & Refrigeration"
COMPANY_AR = "مؤسسة MTE للتبريد والتكييف"

# ------------------------------------------------------------
# CONTACT DETAILS
# Replace these placeholders with the REAL company details.
# ------------------------------------------------------------

EMAIL = "info@mte-ac.com"

PHONE_1 = "0"
PHONE_2 = "0"

ADDRESS_EN = (
    "Al Rabwah, Abi Dhar Al Ghafari Street, "
    "Riyadh, Saudi Arabia"
)

ADDRESS_AR = (
    "الرياض، حي الربوة، شارع أبي ذر الغفاري، "
    "المملكة العربية السعودية"
)

# ============================================================
# CONTACT LINKS
# ============================================================

MAP_QUERY = quote(ADDRESS_EN)

MAP_URL = (
    f"https://www.google.com/maps/search/?api=1"
    f"&query={MAP_QUERY}"
)

EMAIL_URL = f"mailto:{EMAIL}"

PHONE_URL_1 = f"tel:{PHONE_1}"
PHONE_URL_2 = f"tel:{PHONE_2}"

WHATSAPP_NUMBER = (
    PHONE_1
    .replace("+", "")
    .replace(" ", "")
    .replace("-", "")
)

WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}"

# ============================================================
# TRANSLATIONS
# ============================================================

T = {
    "en": {
        "nav_home": "Home",
        "nav_about": "About Us",
        "nav_services": "Services",
        "nav_projects": "Our Work",
        "nav_contact": "Contact",

        "hero_badge": "Professional HVAC Solutions",
        "hero_title": "Reliable Cooling. Comfortable Spaces.",
        "hero_text": (
            "Professional air-conditioning and refrigeration "
            "solutions for residential, commercial and industrial "
            "environments."
        ),

        "view_services": "Explore Services",
        "contact_us": "Contact Us",

        "about_kicker": "ABOUT MTE",
        "about_title": "Professional HVAC & Refrigeration Services",
        "about_text": (
            "MTE specializes in air-conditioning and refrigeration "
            "services, providing practical solutions for installation, "
            "maintenance, troubleshooting and reliable cooling performance."
        ),

        "service_kicker": "MTE SERVICES",
        "service_title": "Our Services",
        "service_intro": (
            "Complete HVAC support from installation and repair "
            "to preventive maintenance."
        ),

        "s1": "Air Conditioning",
        "s1d": (
            "Installation, servicing, troubleshooting and performance "
            "checks for air-conditioning systems."
        ),

        "s2": "Refrigeration",
        "s2d": (
            "Cooling and refrigeration support for commercial "
            "and specialized environments."
        ),

        "s3": "Preventive Maintenance",
        "s3d": (
            "Scheduled inspections designed to reduce breakdowns "
            "and improve system life."
        ),

        "s4": "Repair & Troubleshooting",
        "s4d": (
            "System diagnostics, fault identification and practical "
            "repair solutions."
        ),

        "s5": "HVAC Installation",
        "s5d": (
            "Professional installation support with attention "
            "to safety and system efficiency."
        ),

        "s6": "System Inspection",
        "s6d": (
            "Performance checks, airflow review and general "
            "HVAC condition assessment."
        ),

        "projects_kicker": "CAPABILITIES",
        "projects_title": "What We Work On",

        "p1": "Residential Cooling",
        "p2": "Commercial HVAC",
        "p3": "Refrigeration Systems",
        "p4": "Maintenance Programs",

        "why_kicker": "OUR APPROACH",
        "why_title": "Why MTE",

        "w1": "Professional Service",
        "w1d": "Clear communication and service-focused support.",

        "w2": "Practical Solutions",
        "w2d": (
            "Solutions focused on reliable operation "
            "and customer requirements."
        ),

        "w3": "Maintenance Mindset",
        "w3d": (
            "Preventive care to help systems operate "
            "efficiently and reliably."
        ),

        "request_kicker": "QUICK CONTACT",
        "request_title": "Request a Service",

        "name": "Your Name",
        "service": "Service Required",
        "message": "Message",

        "select_service": "Select a service",

        "send": "Prepare Email Request",

        "contact_kicker": "GET IN TOUCH",
        "contact_title": "Contact MTE",
        "contact_text": (
            "Need a quotation, maintenance visit or technical "
            "assistance? Get in touch."
        ),

        "email": "Email Us",
        "call1": "Call Now",
        "call2": "Call Number 2",
        "directions": "Get Directions",
        "whatsapp": "WhatsApp",

        "address": "Address",
        "phone": "Phone",
        "email_label": "Email",

        "success": (
            "Your email application should open with "
            "a prepared service request."
        ),

        "footer": (
            "MTE Air Conditioning & Refrigeration — "
            "Professional HVAC Solutions"
        ),

        "note": (
            "Update the contact details in the CONFIGURATION "
            "section before deployment."
        ),

        "language": "Language",
        "english": "English",
        "arabic": "العربية",
    },

    "ar": {
        "nav_home": "الرئيسية",
        "nav_about": "من نحن",
        "nav_services": "خدماتنا",
        "nav_projects": "أعمالنا",
        "nav_contact": "اتصل بنا",

        "hero_badge": "حلول تكييف وتبريد احترافية",
        "hero_title": "تبريد موثوق. مساحات أكثر راحة.",
        "hero_text": (
            "حلول احترافية للتكييف والتبريد للمنازل "
            "والمنشآت التجارية والبيئات الصناعية."
        ),

        "view_services": "استكشف الخدمات",
        "contact_us": "تواصل معنا",

        "about_kicker": "عن MTE",
        "about_title": "خدمات التكييف والتبريد الاحترافية",
        "about_text": (
            "تتخصص MTE في خدمات التكييف والتبريد، مع التركيز "
            "على التركيب والصيانة واستكشاف الأعطال وتحقيق "
            "أداء تبريد موثوق."
        ),

        "service_kicker": "خدمات MTE",
        "service_title": "خدماتنا",
        "service_intro": (
            "دعم متكامل لأنظمة التكييف والتبريد من التركيب "
            "والإصلاح إلى الصيانة الوقائية."
        ),

        "s1": "التكييف",
        "s1d": (
            "تركيب وصيانة وفحص واستكشاف أعطال "
            "أنظمة التكييف."
        ),

        "s2": "التبريد",
        "s2d": (
            "دعم أنظمة التبريد للمنشآت التجارية "
            "والبيئات المتخصصة."
        ),

        "s3": "الصيانة الوقائية",
        "s3d": (
            "فحوصات دورية تساعد على تقليل الأعطال "
            "وإطالة عمر النظام."
        ),

        "s4": "الإصلاح واستكشاف الأعطال",
        "s4d": (
            "تشخيص الأنظمة وتحديد الأعطال وتقديم "
            "حلول عملية للإصلاح."
        ),

        "s5": "تركيب أنظمة HVAC",
        "s5d": (
            "دعم احترافي للتركيب مع الاهتمام بالسلامة "
            "وكفاءة النظام."
        ),

        "s6": "فحص الأنظمة",
        "s6d": (
            "فحص الأداء وتدفق الهواء والحالة العامة "
            "لنظام التكييف."
        ),

        "projects_kicker": "مجالات العمل",
        "projects_title": "ما نقوم به",

        "p1": "التبريد السكني",
        "p2": "التكييف التجاري",
        "p3": "أنظمة التبريد",
        "p4": "برامج الصيانة",

        "why_kicker": "نهجنا",
        "why_title": "لماذا MTE",

        "w1": "خدمة احترافية",
        "w1d": "تواصل واضح ودعم يركز على الخدمة.",

        "w2": "حلول عملية",
        "w2d": (
            "حلول تركز على التشغيل الموثوق "
            "واحتياجات العميل."
        ),

        "w3": "نهج الصيانة",
        "w3d": (
            "العناية الوقائية للمساعدة في تشغيل "
            "الأنظمة بكفاءة."
        ),

        "request_kicker": "تواصل سريع",
        "request_title": "طلب خدمة",

        "name": "الاسم",
        "service": "الخدمة المطلوبة",
        "message": "الرسالة",

        "select_service": "اختر الخدمة",

        "send": "تجهيز طلب بالبريد",

        "contact_kicker": "تواصل معنا",
        "contact_title": "اتصل بـ MTE",
        "contact_text": (
            "تحتاج إلى عرض سعر أو زيارة صيانة أو "
            "مساعدة فنية؟ تواصل معنا."
        ),

        "email": "راسلنا",
        "call1": "اتصل الآن",
        "call2": "الاتصال بالرقم 2",
        "directions": "الاتجاهات",
        "whatsapp": "واتساب",

        "address": "العنوان",
        "phone": "الهاتف",
        "email_label": "البريد الإلكتروني",

        "success": (
            "سيتم فتح تطبيق البريد مع طلب خدمة جاهز."
        ),

        "footer": (
            "MTE للتكييف والتبريد — حلول HVAC احترافية"
        ),

        "note": (
            "قم بتعديل بيانات الاتصال في قسم CONFIGURATION "
            "قبل النشر."
        ),

        "language": "اللغة",
        "english": "English",
        "arabic": "العربية",
    },
}

# ============================================================
# SESSION LANGUAGE
# ============================================================

if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ============================================================
# SIDEBAR LANGUAGE
# ============================================================

with st.sidebar:
    st.markdown("### 🌐 Language")

    selected_language = st.radio(
        "Portfolio Language",
        ["English", "العربية"],
        index=(
            0
            if st.session_state.lang == "en"
            else 1
        ),
        label_visibility="collapsed",
    )

    st.session_state.lang = (
        "en"
        if selected_language == "English"
        else "ar"
    )

lang = st.session_state.lang
t = T[lang]
is_ar = lang == "ar"

direction_class = "rtl" if is_ar else ""

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800;900&display=swap'
);

:root {
    --blue: #123b8f;
    --blue-dark: #08245d;
    --blue-light: #edf3fd;
    --red: #e32127;
    --red-dark: #b9151b;
    --ink: #172033;
    --muted: #64748b;
    --line: #dbe3ef;
    --soft: #f5f8fc;
}

html {
    scroll-behavior: smooth;
}

html,
body,
[class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {
    background: #ffffff;
}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* Hide Streamlit default chrome */

#MainMenu,
footer,
header {
    visibility: hidden;
}

/* ============================================================
   HEADER
   ============================================================ */

.mte-header {
    border-bottom: 3px solid var(--blue);
    padding: 12px 0 15px 0;
    margin-bottom: 18px;
}

.mte-brand-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 25px;
}

.brand-left {
    color: var(--blue);
    font-weight: 800;
    line-height: 1.25;
}

.brand-left .company-name {
    font-size: 1.05rem;
    font-weight: 900;
}

.brand-left .red {
    color: var(--red);
    font-size: 0.95rem;
    font-weight: 800;
}

.brand-left .small {
    color: #5671a6;
    font-size: 0.70rem;
    font-weight: 600;
    margin-top: 3px;
}

/* MTE Logo */

.mte-logo {
    width: 125px;
    height: 65px;
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
    box-shadow: 0 4px 12px rgba(18, 59, 143, 0.10);
    flex-shrink: 0;
}

.brand-right {
    text-align: right;
    color: var(--blue);
    line-height: 1.25;
}

.brand-right .arabic {
    font-family: "Cairo", sans-serif;
    font-weight: 800;
    font-size: 0.95rem;
}

.brand-right .arabic-red {
    color: var(--red);
    font-family: "Cairo", sans-serif;
    font-size: 1.05rem;
    font-weight: 800;
}

.brand-right .arabic-small {
    font-family: "Cairo", sans-serif;
    font-size: 0.75rem;
    color: #5671a6;
}

/* ============================================================
   NAVIGATION
   ============================================================ */

.nav-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 10px 0 25px 0;
}

.nav-pills a {
    text-decoration: none;
    color: var(--blue);
    border: 1px solid #c9d6ea;
    border-radius: 7px;
    padding: 7px 15px;
    font-size: 0.84rem;
    font-weight: 700;
    background: white;
    transition: 0.2s ease;
}

.nav-pills a:hover {
    color: white;
    background: var(--blue);
    border-color: var(--blue);
}

/* ============================================================
   HERO
   ============================================================ */

.hero {
    border: 1px solid #d7e1ef;
    border-top: 6px solid var(--red);
    border-radius: 13px;
    padding: 42px;
    background:
        linear-gradient(
            135deg,
            #ffffff 0%,
            #f5f8fd 100%
        );
    box-shadow:
        0 10px 35px rgba(18, 59, 143, 0.08);
    margin-bottom: 25px;
}

.badge {
    display: inline-block;
    color: var(--blue);
    background: #eaf0fb;
    border: 1px solid #c9d8ef;
    border-radius: 999px;
    padding: 7px 13px;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}

.hero h1 {
    color: var(--blue-dark);
    font-size: clamp(2rem, 5vw, 3.5rem);
    line-height: 1.05;
    margin: 17px 0 12px 0;
    font-weight: 900;
}

.hero h1 span {
    color: var(--red);
}

.hero p {
    color: var(--muted);
    font-size: 1rem;
    line-height: 1.8;
    max-width: 760px;
}

/* ============================================================
   SECTION
   ============================================================ */

.section {
    scroll-margin-top: 30px;
    margin: 55px 0 25px 0;
}

.section-kicker {
    color: var(--red);
    text-transform: uppercase;
    font-weight: 900;
    letter-spacing: 1.3px;
    font-size: 0.72rem;
    margin-bottom: 5px;
}

.section-title {
    color: var(--blue-dark);
    font-size: 2rem;
    font-weight: 900;
    margin: 0 0 8px 0;
}

.section-subtitle {
    color: var(--muted);
    line-height: 1.7;
    margin-bottom: 20px;
}

/* ============================================================
   CARDS
   ============================================================ */

.card {
    height: 100%;
    background: #ffffff;
    border: 1px solid var(--line);
    border-top: 4px solid var(--blue);
    border-radius: 10px;
    padding: 22px;
    box-shadow:
        0 7px 25px rgba(15, 35, 70, 0.055);
    transition: 0.2s ease;
}

.card:hover {
    border-top-color: var(--red);
    box-shadow:
        0 12px 30px rgba(18, 59, 143, 0.10);
    transform: translateY(-2px);
}

.card-icon {
    width: 45px;
    height: 45px;
    border-radius: 8px;
    background: #edf3fd;
    color: var(--blue);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    margin-bottom: 14px;
}

.card h3 {
    color: var(--blue-dark);
    margin: 0 0 8px 0;
    font-size: 1.06rem;
}

.card p {
    color: var(--muted);
    line-height: 1.65;
    font-size: 0.90rem;
}

/* ============================================================
   STATS
   ============================================================ */

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
    font-size: 1.6rem;
    font-weight: 900;
}

.stat span {
    color: var(--muted);
    font-size: 0.78rem;
}

/* ============================================================
   CONTACT SECTION
   ============================================================ */

.contact-box {
    background:
        linear-gradient(
            145deg,
            #08245d 0%,
            #123b8f 100%
        );
    color: white;
    border-radius: 14px;
    padding: 32px;
    min-height: 360px;
    box-shadow:
        0 14px 40px rgba(8, 36, 93, 0.18);
    border-left: 5px solid var(--red);
}

.contact-box-title {
    color: white;
    font-size: 1.65rem;
    font-weight: 900;
    margin-bottom: 8px;
}

.contact-box-description {
    color: #d9e4f8;
    line-height: 1.7;
    font-size: 0.91rem;
    margin-bottom: 20px;
}

.contact-item {
    padding: 14px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.13);
}

.contact-item:last-child {
    border-bottom: none;
}

.contact-label {
    color: #9db9ed;
    font-size: 0.67rem;
    text-transform: uppercase;
    font-weight: 900;
    letter-spacing: 1px;
    margin-bottom: 5px;
}

.contact-value {
    color: white;
    font-size: 0.91rem;
    line-height: 1.6;
    word-break: break-word;
}

/* Right contact card */

.contact-action-card {
    background: #ffffff;
    border: 1px solid var(--line);
    border-top: 5px solid var(--red);
    border-radius: 14px;
    padding: 30px;
    min-height: 215px;
    margin-bottom: 15px;
    box-shadow:
        0 8px 28px rgba(15, 35, 70, 0.07);
}

.action-title {
    color: var(--blue);
    font-size: 2.25rem;
    font-weight: 900;
    letter-spacing: 1px;
}

.action-subtitle {
    color: var(--red);
    font-size: 0.86rem;
    font-weight: 800;
    margin-top: 3px;
}

.action-line {
    width: 55px;
    height: 3px;
    background: var(--blue);
    margin: 16px 0;
}

.contact-action-card p {
    color: var(--muted);
    line-height: 1.7;
    font-size: 0.88rem;
}

/* ============================================================
   STREAMLIT BUTTONS
   ============================================================ */

.stLinkButton > a,
.stButton > button {
    border-radius: 7px !important;
    font-weight: 700 !important;
    min-height: 42px !important;
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

/* ============================================================
   FORM
   ============================================================ */

div[data-testid="stForm"] {
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 22px;
    background: #fafcff;
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    border-top: 1px solid var(--line);
    margin-top: 65px;
    padding: 25px 0 8px 0;
    text-align: center;
    color: #718096;
    font-size: 0.8rem;
}

.footer strong {
    color: var(--blue);
}

/* ============================================================
   RTL
   ============================================================ */

.rtl {
    direction: rtl;
    text-align: right;
    font-family: "Cairo", sans-serif;
}

/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .hero {
        padding: 28px 22px;
    }

    .mte-brand-row {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .brand-right {
        text-align: center;
    }

    .mte-logo {
        order: -1;
    }

    .nav-pills {
        justify-content: center;
    }

    .contact-box {
        min-height: auto;
    }

    .contact-action-card {
        min-height: auto;
    }
}

</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    f"""
<div class="mte-header {direction_class}">
    <div class="mte-brand-row">

        <div class="brand-left">
            <div class="company-name">
                {COMPANY_EN}
            </div>

            <div class="red">
                Air Conditioning &amp; Refrigeration
            </div>

            <div class="small">
                Professional HVAC Services
            </div>
        </div>

        <div class="mte-logo">
            MTE
        </div>

        <div class="brand-right">

            <div class="arabic">
                مؤسسة MTE
            </div>

            <div class="arabic-red">
                للتبريد والتكييف
            </div>

            <div class="arabic-small">
                حلول تكييف وتبريد
            </div>

        </div>

    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# NAVIGATION
# ============================================================

st.markdown(
    f"""
<div class="nav-pills {direction_class}">

    <a href="#home">
        {t["nav_home"]}
    </a>

    <a href="#about">
        {t["nav_about"]}
    </a>

    <a href="#services">
        {t["nav_services"]}
    </a>

    <a href="#projects">
        {t["nav_projects"]}
    </a>

    <a href="#contact">
        {t["nav_contact"]}
    </a>

</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================

st.markdown(
    '<div id="home"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="hero {direction_class}">

    <span class="badge">
        ❄️ {t["hero_badge"]}
    </span>

    <h1>
        {t["hero_title"]}
    </h1>

    <p>
        {t["hero_text"]}
    </p>

</div>
""",
    unsafe_allow_html=True,
)

hero_c1, hero_c2, hero_c3 = st.columns(3)

with hero_c1:
    st.link_button(
        "📞 " + t["call1"],
        PHONE_URL_1,
        use_container_width=True,
    )

with hero_c2:
    st.link_button(
        "✉️ " + t["email"],
        EMAIL_URL,
        use_container_width=True,
    )

with hero_c3:
    st.link_button(
        "📍 " + t["directions"],
        MAP_URL,
        use_container_width=True,
    )

# ============================================================
# ABOUT
# ============================================================

st.markdown(
    '<div id="about"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="section {direction_class}">

    <div class="section-kicker">
        {t["about_kicker"]}
    </div>

    <div class="section-title">
        {t["about_title"]}
    </div>

    <div class="section-subtitle">
        {t["about_text"]}
    </div>

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

for col, (big, small) in zip(
    [a1, a2, a3, a4],
    stats,
):

    with col:

        st.markdown(
            f"""
<div class="stat">

    <strong>
        {big}
    </strong>

    <span>
        {small}
    </span>

</div>
""",
            unsafe_allow_html=True,
        )

# ============================================================
# SERVICES
# ============================================================

st.markdown(
    '<div id="services"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="section {direction_class}">

    <div class="section-kicker">
        {t["service_kicker"]}
    </div>

    <div class="section-title">
        {t["service_title"]}
    </div>

    <div class="section-subtitle">
        {t["service_intro"]}
    </div>

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

    for col, (icon, title, description) in zip(
        cols,
        services[start:start + 3],
    ):

        with col:

            st.markdown(
                f"""
<div class="card {direction_class}">

    <div class="card-icon">
        {icon}
    </div>

    <h3>
        {title}
    </h3>

    <p>
        {description}
    </p>

</div>
""",
                unsafe_allow_html=True,
            )

    st.write("")

# ============================================================
# WORK AREAS / PROJECTS
# ============================================================

st.markdown(
    '<div id="projects"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="section {direction_class}">

    <div class="section-kicker">
        {t["projects_kicker"]}
    </div>

    <div class="section-title">
        {t["projects_title"]}
    </div>

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

project_columns = st.columns(4)

for col, (icon, title) in zip(
    project_columns,
    project_items,
):

    with col:

        st.markdown(
            f"""
<div class="card {direction_class}">

    <div class="card-icon">
        {icon}
    </div>

    <h3>
        {title}
    </h3>

</div>
""",
            unsafe_allow_html=True,
        )

# ============================================================
# WHY MTE
# ============================================================

st.markdown(
    f"""
<div class="section {direction_class}">

    <div class="section-kicker">
        {t["why_kicker"]}
    </div>

    <div class="section-title">
        {t["why_title"]}
    </div>

</div>
""",
    unsafe_allow_html=True,
)

why_items = [
    ("✓", t["w1"], t["w1d"]),
    ("✓", t["w2"], t["w2d"]),
    ("✓", t["w3"], t["w3d"]),
]

why_columns = st.columns(3)

for col, (icon, title, description) in zip(
    why_columns,
    why_items,
):

    with col:

        st.markdown(
            f"""
<div class="card {direction_class}">

    <div class="card-icon">
        {icon}
    </div>

    <h3>
        {title}
    </h3>

    <p>
        {description}
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

# ============================================================
# SERVICE REQUEST
# ============================================================

st.markdown(
    f"""
<div class="section {direction_class}">

    <div class="section-kicker">
        {t["request_kicker"]}
    </div>

    <div class="section-title">
        {t["request_title"]}
    </div>

</div>
""",
    unsafe_allow_html=True,
)

with st.form("service_request_form"):

    form_c1, form_c2 = st.columns(2)

    with form_c1:

        customer_name = st.text_input(
            t["name"]
        )

    with form_c2:

        service_options = [
            t["select_service"],
            t["s1"],
            t["s2"],
            t["s3"],
            t["s4"],
            t["s5"],
            t["s6"],
        ]

        selected_service = st.selectbox(
            t["service"],
            service_options,
        )

    customer_message = st.text_area(
        t["message"],
        height=120,
    )

    submitted = st.form_submit_button(
        t["send"],
        type="primary",
        use_container_width=True,
    )

if submitted:

    if (
        not customer_name.strip()
        or selected_service == t["select_service"]
    ):

        st.warning(
            "Please enter your name and select a service."
        )

    else:

        email_subject = quote(
            "MTE Service Request"
        )

        email_body = quote(
            f"""
Hello MTE,

Name: {customer_name}

Service Required: {selected_service}

Message:
{customer_message or "No additional message."}

Thank you.
""".strip()
        )

        request_url = (
            f"mailto:{EMAIL}"
            f"?subject={email_subject}"
            f"&body={email_body}"
        )

        st.success(
            t["success"]
        )

        st.link_button(
            "✉️ Open Email App",
            request_url,
            use_container_width=True,
        )

# ============================================================
# CONTACT
# ============================================================

st.markdown(
    '<div id="contact"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="section {direction_class}">

    <div class="section-kicker">
        {t["contact_kicker"]}
    </div>

    <div class="section-title">
        {t["contact_title"]}
    </div>

    <div class="section-subtitle">
        {t["contact_text"]}
    </div>

</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Contact information + action panel
# ------------------------------------------------------------

contact_left, contact_right = st.columns(
    [1.25, 1],
    gap="large",
)

# ============================================================
# LEFT CONTACT CARD
# ============================================================

with contact_left:

    st.markdown(
        f"""
<div class="contact-box {direction_class}">

    <div class="contact-box-title">
        {COMPANY_NAME}
    </div>

    <div class="contact-box-description">
        {COMPANY_EN}
    </div>

    <div class="contact-item">

        <div class="contact-label">
            {t["address"]}
        </div>

        <div class="contact-value">
            {ADDRESS_AR if is_ar else ADDRESS_EN}
        </div>

    </div>

    <div class="contact-item">

        <div class="contact-label">
            {t["phone"]}
        </div>

        <div class="contact-value">
            {PHONE_1}
        </div>

        <div class="contact-value">
            {PHONE_2}
        </div>

    </div>

    <div class="contact-item">

        <div class="contact-label">
            {t["email_label"]}
        </div>

        <div class="contact-value">
            {EMAIL}
        </div>

    </div>

</div>
""",
        unsafe_allow_html=True,
    )

# ============================================================
# RIGHT ACTION CARD
# ============================================================

with contact_right:

    st.markdown(
        f"""
<div class="contact-action-card {direction_class}">

    <div class="action-title">
        MTE
    </div>

    <div class="action-subtitle">
        Air Conditioning &amp; Refrigeration
    </div>

    <div class="action-line"></div>

    <p>
        Professional HVAC support for installation,
        maintenance, repair and refrigeration services.
    </p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.link_button(
        "📞 " + t["call1"],
        PHONE_URL_1,
        use_container_width=True,
    )

    st.link_button(
        "💬 " + t["whatsapp"],
        WHATSAPP_URL,
        use_container_width=True,
    )

    st.link_button(
        "📍 " + t["directions"],
        MAP_URL,
        use_container_width=True,
    )

    st.link_button(
        "✉️ " + t["email"],
        EMAIL_URL,
        use_container_width=True,
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    f"""
<div class="footer {direction_class}">

    <strong>
        {t["footer"]}
    </strong>

    <br><br>

    <span style="font-size:0.72rem;">
        {t["note"]}
    </span>

</div>
""",
    unsafe_allow_html=True,
)
