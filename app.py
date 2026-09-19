import streamlit as st
from urllib.parse import quote

# ============================================================
# MTE — Air Conditioning & Refrigeration
# Self-contained Streamlit company portfolio
# ============================================================

st.set_page_config(
    page_title="MTE | Air Conditioning & Refrigeration",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------
# COMPANY CONFIGURATION
# ------------------------------------------------------------
COMPANY_NAME = "MTE"
COMPANY_EN = "MTE Air Conditioning & Refrigeration"
COMPANY_AR = "مؤسسة MTE للتبريد والتكييف"

PHONE_1 = "0500000000"
PHONE_2 = "0570000000"

ADDRESS_EN = "Al Rabwah, Al Dhahr Al Ghafari Street, Riyadh, Saudi Arabia"
ADDRESS_AR = "الرياض، حي الربوة، شارع ابن ذي الغفار، المملكة العربية السعودية"

MAP_QUERY = quote(ADDRESS_EN)
MAP_URL = f"https://www.google.com/maps/search/?api=1&query={MAP_QUERY}"
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
        "nav_contact": "Contact Us",
        "hero_badge": "Professional HVAC Solutions",
        "hero_title": "Reliable Cooling. Comfortable Spaces.",
        "hero_text": "Professional air-conditioning and refrigeration solutions for residential, commercial and industrial environments.",
        "about_title": "About MTE",
        "about_text": "MTE specializes in air-conditioning and refrigeration services, with a practical focus on installation, maintenance, troubleshooting and dependable cooling performance.",
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
        "contact_text": "Need a quotation, maintenance visit or technical assistance? Get in touch via call or WhatsApp.",
        "call1": "Call Now",
        "call2": "Call Number 2",
        "directions": "Get Directions",
        "whatsapp": "WhatsApp",
        "address": "Address",
        "phone": "Phone",
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
        "w2d": "حلول تركز على التشغيل الموثوق وااحتياجات العميل.",
        "w3": "نهج الصيانة",
        "w3d": "العناية الوقائية للمساعدة في تشغيل الأنظمة بكفاءة.",
        "contact_title": "تواصل مع MTE",
        "contact_text": "تحتاج إلى عرض سعر أو زيارة صيانة أو مساعدة فنية؟ تواصل معنا عبر الاتصال أو الواتساب.",
        "call1": "اتصل الآن",
        "call2": "الاتصال بالرقم 2",
        "directions": "الاتجاهات",
        "whatsapp": "واتساب",
        "address": "العنوان",
        "phone": "الهاتف",
        "footer": "MTE للتكييف والتبريد — حلول HVAC احترافية",
        "note": "قم بتعديل أرقام الاتصال في قسم CONFIGURATION قبل النشر.",
    },
}

# ------------------------------------------------------------
# SESSION & LANGUAGE SWITCHER
# ------------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "en"

if "page" not in st.session_state:
    st.session_state.page = "Home"

with st.sidebar:
    st.markdown("### 🌐 Select Language / اختر اللغة")
    lang_choice = st.radio(
        "Language",
        ["English", "العربية"],
        index=0 if st.session_state.lang == "en" else 1,
        key="language_selector"
    )
    
    # Correct state assignment
    st.session_state.lang = "en" if lang_choice == "English" else "ar"

lang = st.session_state.lang
t = T[lang]
is_ar = lang == "ar"

# ------------------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --blue: #123b8f;
    --blue-dark: #08245d;
    --red: #e32127;
    --ink: #172033;
    --muted: #64748b;
    --line: #dbe3ef;
    --soft: #f5f8fc;
}

html, body, [class*="css"] { font-family: "Inter", "Cairo", sans-serif; }

#MainMenu, footer, header { visibility: hidden; }

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
    flex-wrap: wrap;
}

.brand-left {
    color: var(--blue);
    font-weight: 800;
    line-height: 1.2;
}

.brand-left .red { color: var(--red); font-size: 1.02rem; }

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
    margin: 0 auto;
}

.brand-right {
    text-align: right;
    color: var(--blue);
    line-height: 1.25;
}

.hero {
    border: 1px solid #d7e1ef;
    border-top: 6px solid var(--red);
    border-radius: 12px;
    padding: 38px 42px;
    background: linear-gradient(135deg, #ffffff 0%, #f5f8fd 100%);
    box-shadow: 0 10px 35px rgba(18,59,143,.08);
    margin-bottom: 24px;
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
}

.card {
    height: 100%;
    background: #fff;
    border: 1px solid var(--line);
    border-top: 4px solid var(--blue);
    border-radius: 10px;
    padding: 22px;
    box-shadow: 0 7px 25px rgba(15,35,70,.055);
    margin-bottom: 12px;
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

.contact-box {
    background: var(--blue-dark);
    color: white;
    border-radius: 12px;
    padding: 32px;
    box-shadow: 0 14px 40px rgba(8,36,93,.18);
    margin-bottom: 20px;
}

.rtl { direction: rtl; text-align: right; }
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# HEADER & BRANDING
# ------------------------------------------------------------
direction_class = "rtl" if is_ar else ""

st.markdown(
    f"""<div class="mte-header {direction_class}">
    <div class="mte-brand-row">
        <div class="brand-left">
            <div>{COMPANY_EN}</div>
            <div class="red">Air Conditioning &amp; Refrigeration</div>
        </div>
        <div class="mte-logo">MTE</div>
        <div class="brand-right">
            <div>مؤسسة MTE</div>
            <div style="color:var(--red); font-weight:800;">للتبريد والتكييف</div>
        </div>
    </div>
</div>""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# NAVIGATION BAR (WORKING STREAMLIT TABS)
# ------------------------------------------------------------
nav_options = [
    t["nav_home"],
    t["nav_about"],
    t["nav_services"],
    t["nav_projects"],
    t["nav_contact"],
]

selected_tab = st.radio(
    "Navigation",
    nav_options,
    horizontal=True,
    label_visibility="collapsed",
    key="main_nav_tabs"
)

st.divider()

# ------------------------------------------------------------
# PAGE CONTENT ROUTING
# ------------------------------------------------------------

# 1. HOME SECTION
if selected_tab == t["nav_home"]:
    st.markdown(
        f"""<div class="hero {direction_class}">
        <span class="badge">❄️ {t['hero_badge']}</span>
        <h1 style="color: var(--blue-dark); font-size: 2.2rem; margin: 15px 0;">{t['hero_title']}</h1>
        <p style="color: var(--muted); font-size: 1.1rem; line-height: 1.6;">{t['hero_text']}</p>
    </div>""",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("📞 " + t["call1"], PHONE_URL_1, use_container_width=True)
    with c2:
        st.link_button("💬 " + t["whatsapp"], WHATSAPP_URL, use_container_width=True)
    with c3:
        st.link_button("📍 " + t["directions"], MAP_URL, use_container_width=True)

# 2. ABOUT US SECTION
elif selected_tab == t["nav_about"]:
    st.markdown(
        f"""<div class="{direction_class}">
        <h2 style="color: var(--blue-dark);">{t['about_title']}</h2>
        <p style="color: var(--muted); font-size: 1.1rem;">{t['about_text']}</p>
    </div>""",
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
                f'<div style="text-align:center; padding:20px; background:#f5f8fc; border-radius:10px; border:1px solid #dbe3ef;">'
                f'<strong style="color:var(--blue); font-size:1.5rem; display:block;">{big}</strong>'
                f'<span style="color:var(--muted); font-size:0.85rem;">{small}</span></div>',
                unsafe_allow_html=True,
            )

# 3. SERVICES SECTION
elif selected_tab == t["nav_services"]:
    st.markdown(
        f"""<div class="{direction_class}">
        <h2 style="color: var(--blue-dark);">{t['service_title']}</h2>
        <p style="color: var(--muted);">{t['service_intro']}</p>
    </div>""",
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
        for col, (icon, title, desc) in zip(cols, services[start : start + 3]):
            with col:
                st.markdown(
                    f"""<div class="card {direction_class}">
            <div class="card-icon">{icon}</div>
            <h3 style="color:var(--blue-dark);">{title}</h3>
            <p style="color:var(--muted); font-size:0.9rem;">{desc}</p>
        </div>""",
                    unsafe_allow_html=True,
                )

# 4. PROJECTS SECTION
elif selected_tab == t["nav_projects"]:
    st.markdown(
        f"""<div class="{direction_class}">
        <h2 style="color: var(--blue-dark);">{t['projects_title']}</h2>
    </div>""",
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
                f"""<div class="card {direction_class}">
        <div class="card-icon">{icon}</div>
        <h3 style="color:var(--blue-dark);">{title}</h3>
    </div>""",
                unsafe_allow_html=True,
            )

# 5. CONTACT SECTION
elif selected_tab == t["nav_contact"]:
    address_val = ADDRESS_AR if is_ar else ADDRESS_EN

    st.markdown(
        f"""<div class="contact-box {direction_class}">
        <h2 style="color:white; margin-bottom:10px;">{t['contact_title']}</h2>
        <p style="color:#d9e4f8; margin-bottom:20px;">{t['contact_text']}</p>
        <div style="margin-bottom:15px;">
            <div style="color:#9db9ed; font-size:0.8rem; font-weight:bold;">{t['address']}</div>
            <div style="color:white; font-size:1rem;">{address_val}</div>
        </div>
        <div>
            <div style="color:#9db9ed; font-size:0.8rem; font-weight:bold;">{t['phone']}</div>
            <div style="color:white; font-size:1rem;">{PHONE_1} &nbsp; | &nbsp; {PHONE_2}</div>
        </div>
    </div>""",
        unsafe_allow_html=True,
    )

    cc1, cc2, cc3 = st.columns(3)
    with cc1:
        st.link_button("📞 " + t["call1"], PHONE_URL_1, use_container_width=True)
    with cc2:
        st.link_button("💬 " + t["whatsapp"], WHATSAPP_URL, use_container_width=True)
    with cc3:
        st.link_button("🗺️ " + t["directions"], MAP_URL, use_container_width=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.divider()
st.markdown(
    f"""<div style="text-align:center; color:#718096; font-size:0.85rem;" class="{direction_class}">
    {t['footer']}
</div>""",
    unsafe_allow_html=True,
)
