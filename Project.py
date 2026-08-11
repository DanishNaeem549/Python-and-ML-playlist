import streamlit as st

st.set_page_config(
    page_title="DrivePro Academy | Professional Driving Lessons",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --navy:#101B2D;
    --navy2:#182842;
    --navy3:#22314C;
    --gold:#C08A28;
    --gold2:#E4B45A;
    --cream:#EDEAE2;
    --white:#F7F4EE;
    --text:#182842;
    --muted:#667085;
    --border:#D8D3C5;
}

html { scroll-behavior:smooth; }
.stApp {
    background:var(--white);
    color:var(--text);
    font-family:'Manrope',sans-serif;
}
.block-container {
    max-width:1280px;
    padding-top:0.5rem;
    padding-bottom:0;
}
header[data-testid="stHeader"] { background:transparent; }
#MainMenu, footer { visibility:hidden; }

h1,h2,h3,h4 {
    font-family:'Fraunces',serif !important;
    color:var(--navy) !important;
}
h1 { font-size:clamp(3rem,6vw,5.8rem) !important; line-height:.96 !important; }
h2 { font-size:clamp(2.1rem,4vw,3.5rem) !important; }
h3 { font-size:1.35rem !important; }
p,li { color:var(--text); }
a { text-decoration:none !important; }

.hero {
    background:var(--navy);
    border-radius:0 0 28px 28px;
    padding:70px 7%;
    color:white;
    margin-bottom:0;
}
.hero h1, .hero h2, .hero p { color:white !important; }
.hero h1 span { color:var(--gold2); }
.eyebrow {
    color:var(--gold) !important;
    text-transform:uppercase;
    letter-spacing:.16em;
    font-weight:800;
    font-size:.75rem;
}
.hero .eyebrow { color:var(--gold2) !important; }
.hero-sub {
    max-width:650px;
    font-size:1.05rem;
    line-height:1.8;
    opacity:.85;
}
.hero-actions { margin:28px 0; }
.btn {
    display:inline-block;
    padding:13px 22px;
    border-radius:8px;
    font-weight:800;
    margin-right:8px;
    transition:.2s;
}
.btn-accent { background:var(--gold); color:white !important; }
.btn-ghost { border:1px solid rgba(255,255,255,.4); color:white !important; }
.btn:hover { transform:translateY(-2px); }
.stats {
    display:flex;
    gap:42px;
    margin-top:38px;
    flex-wrap:wrap;
}
.stats strong {
    display:block;
    font-family:'Fraunces',serif;
    color:white;
    font-size:1.8rem;
}
.stats span { color:#CBD2DE; font-size:.82rem; }

.scene {
    min-height:470px;
    border-radius:24px;
    overflow:hidden;
    position:relative;
    background:linear-gradient(#101B2D,#22314C);
}
.scene svg { width:100%; height:100%; min-height:470px; display:block; }
.float {
    position:absolute;
    background:rgba(247,244,238,.96);
    color:var(--navy);
    border-radius:12px;
    padding:12px 15px;
    box-shadow:0 15px 35px rgba(0,0,0,.2);
}
.float strong { display:block; font-family:'Fraunces',serif; font-size:1.35rem; }
.float small { color:#667085; }
.float-rating { top:28px; left:20px; }
.float-exp { bottom:75px; left:20px; }
.float-count { bottom:25px; right:20px; }
.float-cta {
    position:absolute;
    right:20px;
    top:25px;
    background:rgba(16,27,45,.92);
    color:white;
    border:1px solid rgba(255,255,255,.15);
    border-radius:12px;
    padding:15px;
}
.float-cta p { color:white !important; margin:2px 0; }
.stars { color:var(--gold); letter-spacing:2px; }

.trust {
    background:var(--cream);
    display:grid;
    grid-template-columns:repeat(4,1fr);
    border-radius:0 0 18px 18px;
    margin-bottom:70px;
}
.trust-item { padding:26px; text-align:center; border-right:1px solid var(--border); }
.trust-item:last-child { border:0; }
.trust-item strong { display:block; font-family:'Fraunces',serif; font-size:1.8rem; color:var(--navy); }
.trust-item span:last-child { color:var(--muted); font-size:.8rem; }

.section { padding:75px 5%; }
.section-alt { background:var(--cream); border-radius:24px; }
.center { text-align:center; }
.section-sub { max-width:700px; margin:0 auto 35px; color:var(--muted); text-align:center; }

.cards {
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:18px;
}
.card, .price-card, .review-card, .feature, .instructor, .value-card {
    background:white;
    border:1px solid var(--border);
    border-radius:16px;
    padding:25px;
    box-shadow:0 8px 25px rgba(16,27,45,.05);
}
.card { display:flex; flex-direction:column; }
.card p { color:var(--muted); min-height:68px; }
.icon {
    width:50px; height:50px; border-radius:50%;
    display:grid; place-items:center;
    background:var(--cream); color:var(--gold);
    font-size:1.4rem; margin-bottom:12px;
}
.price { font-family:'Fraunces',serif; font-size:2.3rem; font-weight:700; color:var(--navy); }
.price small { font-family:'Manrope'; font-size:.8rem; color:var(--muted); }
.outline {
    display:block; text-align:center; border:1px solid var(--navy);
    color:var(--navy) !important; padding:10px; border-radius:7px;
    font-weight:800; margin-top:auto;
}
.feature-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin-top:35px; }
.feature { background:transparent; }
.check { color:var(--gold); font-size:1.5rem; font-weight:800; }
.feature p { color:var(--muted); }

.instructor-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:22px; }
.instructor-photo {
    height:180px; border-radius:12px;
    display:grid; place-items:center;
    background:linear-gradient(135deg,var(--navy3),var(--gold));
    color:white; font:700 3.4rem 'Fraunces';
}
.instructor-body { padding-top:18px; }
.role { color:var(--gold) !important; font-weight:700; }
.badge {
    display:inline-block; background:var(--cream);
    padding:6px 10px; border-radius:30px; font-size:.75rem;
    margin:10px 0 18px; font-weight:700;
}

.pricing { display:grid; grid-template-columns:repeat(3,1fr); gap:22px; max-width:950px; margin:35px auto; }
.price-card { position:relative; }
.featured { border:2px solid var(--gold); transform:translateY(-8px); }
.tag {
    position:absolute; right:18px; top:18px;
    background:var(--gold); color:white; padding:5px 9px;
    border-radius:20px; font-size:.7rem; font-weight:800;
}
.price-list { padding-left:18px; color:var(--muted); line-height:2; }

.booking {
    background:var(--navy);
    border-radius:24px;
    padding:65px 6%;
}
.booking h2, .booking p, .booking li { color:white !important; }
.booking .eyebrow { color:var(--gold2) !important; }
.booking-points { line-height:2; margin:25px 0; }
.booking-call a { color:var(--gold2) !important; }

.journey { background:white; }
.timeline {
    display:grid; grid-template-columns:repeat(6,1fr);
    gap:14px; list-style:none; padding:0; margin-top:40px;
}
.timeline li {
    border-top:3px solid var(--gold);
    padding-top:15px;
}
.marker {
    display:inline-grid; place-items:center;
    width:38px; height:38px; border-radius:50%;
    background:var(--navy); color:white; font-size:.8rem; font-weight:800;
}
.timeline p { color:var(--muted); font-size:.85rem; }

.review-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; }
.review-card p { color:var(--muted); line-height:1.7; }
.review-name { color:var(--navy) !important; font-weight:800; }
.rating-summary { text-align:center; margin-top:35px; }
.rating-summary strong { font-family:'Fraunces'; font-size:2rem; margin:0 10px; }

.value-grid { display:grid; grid-template-columns:1fr 1fr; gap:25px; max-width:900px; margin:35px auto; }
.value-card li { list-style:none; padding:8px 0; }
.value-card ul { padding:0; }
.before { border-color:#d9b4b4; }
.after { border-color:#b9d3c0; }
.value-cta { text-align:center; }

.faq { max-width:850px; margin:auto; }
details {
    background:white; border-bottom:1px solid var(--border);
    padding:18px 5px;
}
summary { cursor:pointer; font-weight:800; color:var(--navy); }
details p { color:var(--muted); line-height:1.7; padding:10px 20px 0 0; }

.area-grid { display:grid; grid-template-columns:1.1fr .9fr; gap:30px; align-items:center; }
.map {
    min-height:330px; border-radius:18px; background:#EDEAE2;
    border:1px solid var(--border); position:relative; overflow:hidden;
}
.map:before, .map:after {
    content:""; position:absolute; border:2px dashed var(--gold);
    border-radius:50%; width:70%; height:45%; left:15%; top:25%;
    transform:rotate(-15deg);
}
.map:after { width:45%; height:70%; left:30%; top:10%; transform:rotate(40deg); }
.city {
    position:absolute; z-index:2; width:12px; height:12px;
    border-radius:50%; background:var(--navy);
}
.city span { position:absolute; left:17px; top:-5px; white-space:nowrap; font-weight:800; font-size:.78rem; }
.c1 { left:25%; top:30%; } .c2 { left:55%; top:22%; }
.c3 { left:42%; top:60%; } .c4 { left:70%; top:42%; }
.area-list { columns:2; line-height:2.2; font-weight:700; }

.contact-grid { display:grid; grid-template-columns:1fr 1fr; gap:35px; max-width:950px; margin:35px auto; }
.contact-details { padding:20px; }
.contact-block { margin-bottom:25px; }
.contact-block h3 { margin-bottom:4px; }
.contact-block p, .contact-block a { color:var(--muted) !important; }
.social { display:flex; gap:10px; }
.social span {
    width:38px; height:38px; display:grid; place-items:center;
    border-radius:50%; background:var(--navy); color:white; font-weight:800;
}

.final {
    background:var(--navy);
    color:white;
    text-align:center;
    padding:75px 20px;
    border-radius:24px;
}
.final h2, .final p { color:white !important; }
.final p { opacity:.8; }

.footer {
    background:var(--navy);
    color:white;
    margin-top:30px;
    padding:50px 6% 20px;
    border-radius:24px 24px 0 0;
}
.footer h3, .footer p, .footer a { color:white !important; }
.footer p, .footer a { opacity:.72; }
.footer-grid { display:grid; grid-template-columns:2fr 1fr 1fr 1fr; gap:30px; }
.footer ul { list-style:none; padding:0; line-height:2; }
.footer-bottom {
    border-top:1px solid rgba(255,255,255,.15);
    margin-top:30px; padding-top:18px;
    display:flex; justify-content:space-between;
}

div[data-testid="stForm"] {
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.12);
    border-radius:16px;
    padding:20px;
}
.stButton > button, div[data-testid="stFormSubmitButton"] button {
    background:var(--gold) !important;
    color:white !important;
    border:0 !important;
    border-radius:8px !important;
    font-weight:800 !important;
}
input, textarea, select {
    border-radius:8px !important;
}

@media (max-width:1000px) {
    .cards { grid-template-columns:repeat(2,1fr); }
    .feature-grid { grid-template-columns:repeat(2,1fr); }
    .timeline { grid-template-columns:repeat(3,1fr); }
    .trust { grid-template-columns:repeat(2,1fr); }
    .trust-item:nth-child(2) { border-right:0; }
}
@media (max-width:700px) {
    .hero { padding:45px 6%; }
    .cards,.feature-grid,.instructor-grid,.pricing,.review-grid,.value-grid,.area-grid,.contact-grid,.footer-grid {
        grid-template-columns:1fr;
    }
    .timeline { grid-template-columns:1fr 1fr; }
    .trust { grid-template-columns:1fr 1fr; }
    .stats { gap:20px; }
    .featured { transform:none; }
    .scene { margin-top:25px; }
    .footer-bottom { display:block; }
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Navigation
# -----------------------------
st.markdown("""
<div style="display:flex;align-items:center;justify-content:space-between;padding:18px 2%;border-bottom:1px solid #D8D3C5;">
    <a href="#home" style="font:700 1.35rem Fraunces;color:#101B2D !important;">
        ◯ DrivePro <em>Academy</em>
    </a>
    <div style="display:flex;gap:18px;align-items:center;flex-wrap:wrap;">
        <a href="#lessons">Lessons</a>
        <a href="#instructors">Instructors</a>
        <a href="#pricing">Pricing</a>
        <a href="#reviews">Reviews</a>
        <a href="#faq">FAQ</a>
        <a href="#contact">Contact</a>
        <a href="#booking" class="btn btn-accent">Book a Lesson</a>
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Hero
# -----------------------------
st.markdown("""
<section class="hero" id="home">
<div class="hero-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center;">
<div>
<p class="eyebrow">Est. 2016 · DVSA Approved Instructors</p>
<h1>Learn to Drive <span>With Confidence</span></h1>
<p class="hero-sub">Professional driving lessons with qualified instructors, flexible scheduling, and a simple path from your first lesson to your driving test.</p>
<div class="hero-actions">
<a href="#booking" class="btn btn-accent">Book Your First Lesson</a>
<a href="#pricing" class="btn btn-ghost">View Lesson Packages</a>
</div>
<div class="stats">
<div><strong>4.9/5</strong><span>Student rating</span></div>
<div><strong>10+</strong><span>Years experience</span></div>
<div><strong>500+</strong><span>Students trained</span></div>
</div>
</div>
<div class="scene">
<svg viewBox="0 0 560 620" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#101B2D"/><stop offset="55%" stop-color="#182842"/><stop offset="100%" stop-color="#22314C"/>
</linearGradient>
<linearGradient id="road" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#0C1420"/><stop offset="100%" stop-color="#1B2740"/>
</linearGradient>
</defs>
<rect width="560" height="620" fill="url(#sky)"/>
<circle cx="440" cy="120" r="46" fill="#F3D9A0" opacity=".9"/>
<g opacity=".5">
<rect x="60" y="330" width="90" height="130" fill="#0C1420"/>
<rect x="160" y="290" width="60" height="170" fill="#0C1420"/>
<rect x="230" y="350" width="80" height="110" fill="#0C1420"/>
</g>
<rect y="470" width="560" height="150" fill="url(#road)"/>
<path d="M0 470L230 470L120 620H0Z" fill="#233350"/>
<path d="M560 470L330 470L440 620H560Z" fill="#233350"/>
<g fill="#C08A28">
<rect x="264" y="480" width="10" height="34" rx="3"/><rect x="270" y="530" width="12" height="38" rx="3"/><rect x="278" y="586" width="14" height="42" rx="3"/>
</g>
<g transform="translate(190,392)">
<ellipse cx="120" cy="118" rx="150" ry="16" fill="#050A12" opacity=".45"/>
<path d="M6 96Q2 60 46 46L70 20Q86 6 112 6H182Q206 6 218 24L236 52Q262 58 264 88V100Q264 110 254 110H18Q6 110 6 96Z" fill="#F7F4EE"/>
<path d="M74 44L94 22Q102 14 116 14H150V46Z" fill="#182842"/>
<path d="M158 46V14H182Q198 14 206 26L220 46Z" fill="#182842"/>
<rect x="4" y="86" width="262" height="14" fill="#C08A28"/>
<circle cx="70" cy="112" r="26" fill="#101B2D"/><circle cx="70" cy="112" r="11" fill="#EDEAE2"/>
<circle cx="212" cy="112" r="26" fill="#101B2D"/><circle cx="212" cy="112" r="11" fill="#EDEAE2"/>
</g>
</svg>
<div class="float float-rating"><span class="stars">★★★★★</span><strong>4.9/5</strong><small>Student Rating</small></div>
<div class="float float-exp"><strong>10+</strong><small>Years Experience</small></div>
<div class="float float-count"><strong>500+</strong><small>Students Trained</small></div>
<div class="float-cta"><p><b>Ready to start driving?</b></p><p>Book your first lesson today.</p><a href="#booking" class="btn btn-accent">Book Now</a></div>
</div>
</div>
</section>
""", unsafe_allow_html=True)

# Trust bar
st.markdown("""
<div class="trust">
<div class="trust-item"><span class="stars">★★★★★</span><strong>4.9/5</strong><span>Rating</span></div>
<div class="trust-item"><strong>500+</strong><span>Happy Students</span></div>
<div class="trust-item"><strong>94%</strong><span>Student Satisfaction</span></div>
<div class="trust-item"><strong>10+</strong><span>Years Experience</span></div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Lessons
# -----------------------------
st.markdown("""
<section class="section" id="lessons">
<p class="eyebrow center">Our Lessons</p>
<h2 class="center">Driving Lessons Designed Around You</h2>
<p class="section-sub">Whichever stage you're at, there's a structured lesson plan to match.</p>
<div class="cards">
<div class="card"><div class="icon">✓</div><h3>First Driving Lesson</h3><p>Perfect for beginners taking their first step behind the wheel.</p><div class="price">£35</div><a class="outline" href="#pricing">Learn More</a></div>
<div class="card"><div class="icon">🚗</div><h3>Standard Driving Lessons</h3><p>Build confidence and improve your driving skills with structured lessons.</p><div class="price">£45</div><a class="outline" href="#pricing">Learn More</a></div>
<div class="card"><div class="icon">→</div><h3>Intensive Driving Course</h3><p>Accelerate your learning with a focused driving program.</p><div class="price">£399</div><a class="outline" href="#pricing">Learn More</a></div>
<div class="card"><div class="icon">▤</div><h3>Test Preparation</h3><p>Prepare for your practical driving test with targeted instruction.</p><div class="price">£45</div><a class="outline" href="#pricing">Learn More</a></div>
<div class="card"><div class="icon">↻</div><h3>Refresher Lessons</h3><p>Refresh your driving skills and build confidence on the road.</p><div class="price">£40</div><a class="outline" href="#pricing">Learn More</a></div>
</div>
</section>
""", unsafe_allow_html=True)


# Why choose us
st.markdown("""
<section class="section section-alt">
<p class="eyebrow center">Why DrivePro</p>
<h2 class="center">Everything You Need to Become a Confident Driver</h2>
<div class="feature-grid">
<div class="feature"><span class="check">✓</span><h3>Qualified Instructors</h3><p>DVSA-approved instructors with years of teaching experience.</p></div>
<div class="feature"><span class="check">✓</span><h3>Flexible Scheduling</h3><p>Evening, weekend and after-school slots that fit your life.</p></div>
<div class="feature"><span class="check">✓</span><h3>Modern Vehicles</h3><p>Learn in dual-control, well-maintained manual and automatic cars.</p></div>
<div class="feature"><span class="check">✓</span><h3>High Student Satisfaction</h3><p>94% of students rate their lessons as excellent.</p></div>
<div class="feature"><span class="check">✓</span><h3>Personalized Learning</h3><p>A lesson plan built around your pace, goals and experience.</p></div>
<div class="feature"><span class="check">✓</span><h3>Local Test Route Knowledge</h3><p>In-depth familiarity with local test centres and routes.</p></div>
</div>
</section>
""", unsafe_allow_html=True)


# -----------------------------
# Instructors
# -----------------------------
st.markdown("""
<section class="section" id="instructors">
<p class="eyebrow center">Our Team</p>
<h2 class="center">Meet Your Instructors</h2>
<p class="section-sub">Patient, DVSA-qualified instructors who make every lesson count.</p>
<div class="instructor-grid">
<div class="instructor"><div class="instructor-photo">SW</div><div class="instructor-body"><h3>Sarah Williams</h3><p class="role">Senior Driving Instructor</p><p><span class="stars">★★★★★</span> 4.9 · 8 Years Experience</p><span class="badge">Manual & Automatic</span><a class="outline" href="#booking">Book With Instructor</a></div></div>
<div class="instructor"><div class="instructor-photo">JC</div><div class="instructor-body"><h3>James Carter</h3><p class="role">Driving Instructor</p><p><span class="stars">★★★★★</span> 4.8 · 6 Years Experience</p><span class="badge">Manual Only</span><a class="outline" href="#booking">Book With Instructor</a></div></div>
<div class="instructor"><div class="instructor-photo">MB</div><div class="instructor-body"><h3>Michael Brown</h3><p class="role">Senior Driving Instructor</p><p><span class="stars">★★★★★</span> 5.0 · 10 Years Experience</p><span class="badge">Manual & Automatic</span><a class="outline" href="#booking">Book With Instructor</a></div></div>
</div>
</section>
""", unsafe_allow_html=True)


# -----------------------------
# Pricing
# -----------------------------
st.markdown("""
<section class="section section-alt" id="pricing">
<p class="eyebrow center">Pricing</p>
<h2 class="center">Simple, Transparent Pricing</h2>
<p class="section-sub">No hidden fees. Choose the package that fits your goals.</p>
</section>
""", unsafe_allow_html=True)

pricing_col1, pricing_col2, pricing_col3 = st.columns(3)
pricing_cards = [
    ("First Lesson", "£35", "60 minutes", ["One-to-one lesson", "Initial assessment", "Basic controls", "Road safety fundamentals"], False),
    ("Standard", "£45", "60 minutes", ["One-to-one instruction", "Personalized learning plan", "Progress tracking", "Flexible scheduling"], True),
    ("Intensive", "£399", "10-hour package", ["10 hours training", "Personalized schedule", "Test preparation", "Progress tracking"], False),
]
for col, (title, price, meta, items, featured) in zip([pricing_col1, pricing_col2, pricing_col3], pricing_cards):
    with col:
        tag = '<span class="tag">Most Popular</span>' if featured else ''
        html_items = ''.join(f'<li>{x}</li>' for x in items)
        st.markdown(f"""
        <div class="price-card {'featured' if featured else ''}">
            {tag}<h3>{title}</h3><div class="price">{price}</div>
            <p style="color:#667085">{meta}</p>
            <ul class="price-list">{html_items}</ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Book a Lesson" if featured else ("Book First Lesson" if title == "First Lesson" else "Choose Package"), key=f"price_{title}"):
            st.session_state["booking_message"] = f"{title} selected."


# -----------------------------
# Booking
# -----------------------------
st.markdown("""
<section class="section booking" id="booking">
<div style="display:grid;grid-template-columns:1fr 1.25fr;gap:45px;align-items:start;">
<div>
<p class="eyebrow">Book a Lesson</p>
<h2>Book Your Driving Lesson</h2>
<p>Tell us a little about what you need and we'll confirm your availability within one working day.</p>
<ul class="booking-points">
<li>DVSA-approved instructors</li>
<li>Manual and automatic cars</li>
<li>Pick-up from home, work or college</li>
</ul>
<p class="booking-call">Prefer to speak with us? Call <a href="tel:02012345678">020 1234 5678</a></p>
</div>
""", unsafe_allow_html=True)

with st.form("booking_form"):
    st.markdown("### Lesson Booking Enquiry")
    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("Full Name", placeholder="Jordan Smith")
        phone = st.text_input("Phone Number", placeholder="07xxx xxx xxx")
        transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
        pref_time = st.time_input("Preferred Time")
    with c2:
        email = st.text_input("Email Address", placeholder="jordan@email.com")
        lesson_type = st.selectbox("Lesson Type", [
            "First Driving Lesson",
            "Standard Driving Lessons",
            "Intensive Driving Course",
            "Test Preparation",
            "Refresher Lessons",
        ])
        pref_date = st.date_input("Preferred Date")
        pickup = st.text_input("Pickup Location", placeholder="Postcode or address")
    submitted = st.form_submit_button("Check Availability", use_container_width=True)

if submitted:
    if not full_name or not email or not phone:
        st.error("Please complete your name, email and phone number.")
    else:
        st.success(f"Thanks {full_name}! Your {lesson_type.lower()} enquiry has been received. We'll confirm availability within one working day.")

st.markdown("</div></section>", unsafe_allow_html=True)


# -----------------------------
# Learning journey
# -----------------------------
st.markdown("""
<section class="section journey">
<p class="eyebrow center">The Route to Passing</p>
<h2 class="center">Your Learning Journey</h2>
<p class="section-sub">Six clear stages from your very first lesson to driving independently.</p>
<ol class="timeline">
<li><span class="marker">01</span><h3>First Lesson</h3><p>Meet your instructor and get comfortable with the controls.</p></li>
<li><span class="marker">02</span><h3>Build Your Skills</h3><p>Junctions, manoeuvres and everyday road situations.</p></li>
<li><span class="marker">03</span><h3>Practice & Confidence</h3><p>Independent driving and varied road types.</p></li>
<li><span class="marker">04</span><h3>Mock Test</h3><p>A full test simulation to check you're ready.</p></li>
<li><span class="marker">05</span><h3>Driving Test</h3><p>Sit your practical test with full support.</p></li>
<li><span class="marker">06</span><h3>Pass & Drive Independently</h3><p>Collect your licence and hit the road.</p></li>
</ol>
</section>
""", unsafe_allow_html=True)


# Reviews
st.markdown("""
<section class="section section-alt" id="reviews">
<p class="eyebrow center">Testimonials</p>
<h2 class="center">What Our Students Say</h2>
<div class="review-grid">
<div class="review-card"><span class="stars">★★★★★</span><p>"I passed my driving test first time thanks to Sarah. Every lesson was structured, friendly and easy to understand."</p><p class="review-name">Emily R.</p></div>
<div class="review-card"><span class="stars">★★★★★</span><p>"Excellent instructors and a very professional service. I felt much more confident after every lesson."</p><p class="review-name">Daniel M.</p></div>
<div class="review-card"><span class="stars">★★★★★</span><p>"Highly recommended. The lessons were flexible and perfectly suited to my schedule."</p><p class="review-name">Sophie T.</p></div>
</div>
<div class="rating-summary"><span class="stars">★★★★★</span><strong>4.9/5</strong><span>Based on 500+ Student Reviews</span></div>
</section>
""", unsafe_allow_html=True)


# Before/after
st.markdown("""
<section class="section">
<p class="eyebrow center">The DrivePro Difference</p>
<h2 class="center">Turn Website Visitors Into Driving Students</h2>
<div class="value-grid">
<div class="value-card before"><h3>Typical Website</h3><ul>
<li>✕ Difficult to find pricing</li><li>✕ No clear booking CTA</li><li>✕ Poor mobile experience</li><li>✕ Limited information</li><li>✕ Hard to contact</li>
</ul></div>
<div class="value-card after"><h3>Modern DrivePro Experience</h3><ul>
<li>✓ Clear lesson packages</li><li>✓ Easy booking enquiry</li><li>✓ Mobile-first design</li><li>✓ Instructor profiles</li><li>✓ Strong calls-to-action</li>
</ul></div>
</div>
<div class="value-cta"><a href="#contact" class="btn btn-accent">Let's Build Your Driving School Website</a></div>
</section>
""", unsafe_allow_html=True)


# FAQ
st.markdown("""
<section class="section" id="faq">
<div class="faq">
<p class="eyebrow center">FAQ</p>
<h2 class="center">Frequently Asked Questions</h2>
<details open><summary>How old do I need to be to start lessons?</summary><p>You can start lessons at 17, or 16 if you receive the enhanced rate of the mobility component of PIP.</p></details>
<details><summary>Do you offer automatic driving lessons?</summary><p>Yes, all of our packages are available in manual or automatic vehicles.</p></details>
<details><summary>How long is each lesson?</summary><p>Standard lessons are 60 minutes, with longer intensive sessions available on request.</p></details>
<details><summary>Can I choose my instructor?</summary><p>Absolutely. You can request a specific instructor when booking, subject to availability.</p></details>
<details><summary>Do you offer intensive driving courses?</summary><p>Yes, our intensive course packs focused hours together to fast-track your test readiness.</p></details>
<details><summary>Can I book lessons online?</summary><p>Yes, use our booking form above and our team will confirm availability within one working day.</p></details>
<details><summary>What happens if I need to cancel?</summary><p>We ask for at least 48 hours' notice so we can offer the slot to another student.</p></details>
<details><summary>Do you offer test-day preparation?</summary><p>Yes, our test preparation package includes a mock test and route-specific practice.</p></details>
</div>
</section>
""", unsafe_allow_html=True)


# Service area
st.markdown("""
<section class="section section-alt">
<p class="eyebrow center">Coverage</p>
<h2 class="center">Driving Lessons Near You</h2>
<div class="area-grid">
<div class="map">
<div class="city c1"><span>London</span></div>
<div class="city c2"><span>Manchester</span></div>
<div class="city c3"><span>Birmingham</span></div>
<div class="city c4"><span>Leeds</span></div>
</div>
<div>
<ul class="area-list"><li>London</li><li>Manchester</li><li>Birmingham</li><li>Leeds</li></ul>
""", unsafe_allow_html=True)

with st.form("postcode_form"):
    postcode = st.text_input("Enter your postcode", placeholder="e.g. SW1A 1AA")
    postcode_submit = st.form_submit_button("Check My Area")
if postcode_submit:
    if postcode.strip():
        st.success(f"Thanks! We can check availability for {postcode.upper()}.")
    else:
        st.warning("Please enter your postcode.")

st.markdown("""
<p style="color:#667085">We provide professional driving lessons across multiple local areas.</p>
</div></div>
</section>
""", unsafe_allow_html=True)


# Contact
st.markdown("""
<section class="section" id="contact">
<p class="eyebrow center">Get In Touch</p>
<h2 class="center">Ready to Start Driving?</h2>
<div class="contact-grid">
""", unsafe_allow_html=True)

with st.form("contact_form"):
    st.markdown("### Send an Enquiry")
    c1, c2 = st.columns(2)
    with c1:
        c_name = st.text_input("Name", placeholder="Your name")
        c_phone = st.text_input("Phone", placeholder="07xxx xxx xxx")
    with c2:
        c_email = st.text_input("Email", placeholder="you@email.com")
    c_message = st.text_area("Message", placeholder="Tell us what you're looking for", height=120)
    contact_submit = st.form_submit_button("Send Enquiry", use_container_width=True)

if contact_submit:
    if not c_name or not c_email or not c_message:
        st.error("Please complete your name, email and message.")
    else:
        st.success(f"Thanks {c_name}! Your enquiry has been sent.")

st.markdown("""
<div class="contact-details">
<div class="contact-block"><h3>Phone</h3><p><a href="tel:02012345678">020 1234 5678</a></p></div>
<div class="contact-block"><h3>Email</h3><p><a href="mailto:hello@driveproacademy.co.uk">hello@driveproacademy.co.uk</a></p></div>
<div class="contact-block"><h3>Opening Hours</h3><p>Mon–Fri: 8:00–19:00<br>Sat: 9:00–16:00<br>Sun: Closed</p></div>
<div class="contact-block"><h3>Follow Us</h3><div class="social"><span>f</span><span>ig</span><span>x</span></div></div>
</div>
</div>
</section>
""", unsafe_allow_html=True)


# Final CTA
st.markdown("""
<section class="final">
<h2>Your Driving Journey Starts Here.</h2>
<p>Take the first step toward becoming a confident, independent driver.</p>
<a href="#booking" class="btn btn-accent">Book Your First Lesson</a>
<a href="tel:02012345678" class="btn btn-ghost">Call Us Today</a>
</section>
""", unsafe_allow_html=True)


# Footer
st.markdown("""
<footer class="footer">
<div class="footer-grid">
<div><h3>DrivePro <em>Academy</em></h3><p>Professional driving lessons designed around you.</p></div>
<div><h3>Quick Links</h3><ul>
<li><a href="#home">Home</a></li><li><a href="#lessons">Lessons</a></li><li><a href="#pricing">Pricing</a></li><li><a href="#instructors">Instructors</a></li><li><a href="#reviews">Reviews</a></li><li><a href="#faq">FAQ</a></li><li><a href="#contact">Contact</a></li>
</ul></div>
<div><h3>Services</h3><ul>
<li><a href="#lessons">Driving Lessons</a></li><li><a href="#lessons">Automatic Lessons</a></li><li><a href="#lessons">Intensive Courses</a></li><li><a href="#lessons">Test Preparation</a></li><li><a href="#lessons">Refresher Lessons</a></li>
</ul></div>
<div><h3>Contact</h3><ul><li><a href="tel:02012345678">020 1234 5678</a></li><li><a href="mailto:hello@driveproacademy.co.uk">hello@driveproacademy.co.uk</a></li></ul></div>
</div>
<div class="footer-bottom"><p>© 2026 DrivePro Academy. All rights reserved.</p><div><a href="#">Privacy Policy</a> &nbsp; <a href="#">Terms & Conditions</a></div></div>
</footer>
""", unsafe_allow_html=True)
