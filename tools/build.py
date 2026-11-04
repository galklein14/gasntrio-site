#!/usr/bin/env python3
"""Builds the Hebrew and English HTML pages from the templates below.

Run after changing page structure or interface labels:  python3 tools/build.py
Day-to-day content (texts, shows, videos, members) lives in content/*.json and
is edited through Pages CMS, with no build step.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://gasntrio.com"

PAGES = {
    "home":    {"he": "",          "en": "en/"},
    "events":  {"he": "events/",   "en": "en/events/"},
    "epk":     {"he": "epk/",      "en": "en/epk/"},
    "privacy": {"he": "privacy/",  "en": "en/privacy/"},
}

UI = {
    "skip": ("Skip to content", "דילוג לתוכן"),
    "menu": ("Menu", "תפריט"),
    "nav_about": ("About", "עלינו"),
    "nav_shows": ("Shows", "הופעות"),
    "nav_music": ("Music", "מוזיקה"),
    "nav_events": ("Weddings & events", "חתונות ואירועים"),
    "nav_epk": ("Press kit", "ערכת עיתונות"),
    "nav_book": ("Book us", "הזמינו אותנו"),
    "lang_other": ("עברית", "English"),
    "cta_book": ("Book the band", "הזמינו את הלהקה"),
    "cta_listen": ("Listen", "להאזנה"),
    "cta_events": ("Weddings & events", "לחתונות ואירועים"),
    "shows_title": ("Upcoming shows", "הופעות קרובות"),
    "bit_title": ("More dates from Bandsintown", "עוד תאריכים מ-Bandsintown"),
    "band_title": ("The band", "ההרכב"),
    "music_title": ("Listen & watch", "להאזין ולצפות"),
    "albums_title": ("Albums", "אלבומים"),
    "contact_title": ("Let's talk", "בואו נדבר"),
    "contact_text": ("Concerts, festivals, weddings and private events, in Israel and abroad. Tell us the date, the place and what you're celebrating.",
                     "הופעות, פסטיבלים, חתונות ואירועים פרטיים, בארץ ובחו״ל. ספרו לנו מה התאריך, איפה ומה חוגגים."),
    "f_name": ("Name", "שם"),
    "f_email": ("Email", "אימייל"),
    "f_phone": ("Phone", "טלפון"),
    "f_date": ("Event date", "תאריך האירוע"),
    "f_type": ("Type of event", "סוג האירוע"),
    "f_types": ("Concert / festival|Wedding|Bar / bat mitzvah|Private or corporate event|Other",
                "הופעה / פסטיבל|חתונה|בר / בת מצווה|אירוע פרטי או של חברה|אחר"),
    "f_msg": ("Message", "הודעה"),
    "f_send": ("Send", "שליחה"),
    "events_kicker": ("Weddings & events", "חתונות ואירועים"),
    "services_title": ("Upgrade your event", "שדרגו את האירוע שלכם"),
    "testimonials_title": ("What couples say", "מה אומרים עלינו"),
    "watch_title": ("See us at a wedding", "ככה זה נראה בחתונה"),
    "epk_kicker": ("Electronic press kit", "ערכת עיתונות"),
    "epk_title": ("Press kit", "ערכת עיתונות"),
    "live_title": ("Live experience", "החוויה החיה"),
    "festivals_title": ("Selected festivals & venues", "פסטיבלים ובמות נבחרים"),
    "bio_title": ("Biography", "ביוגרפיה"),
    "photos_title": ("Photos", "תמונות"),
    "privacy": ("Privacy policy", "מדיניות פרטיות"),
    "rights": ("All rights reserved", "כל הזכויות שמורות"),
}

TITLES = {
    "home": ("Di Gasn Trio | Israeli Balkan-Klezmer Band", "די גאסן טריו | להקת בלקן-כליזמר ישראלית"),
    "events": ("Klezmer band for weddings and events | Di Gasn Trio", "להקת כליזמר לחתונות ואירועים | די גאסן טריו"),
    "epk": ("Press kit | Di Gasn Trio", "ערכת עיתונות | די גאסן טריו"),
    "privacy": ("Privacy policy | Di Gasn Trio", "מדיניות פרטיות | די גאסן טריו"),
}
DESCS = {
    "home": ("Di Gasn Trio: klezmer and Balkan music from Jerusalem. Concerts, festivals, weddings and events in Israel and abroad.",
             "די גאסן טריו: מוזיקת כליזמר ובלקן מירושלים. הופעות, פסטיבלים, חתונות ואירועים בארץ ובחו״ל."),
    "events": ("A live klezmer and Balkan band for your wedding: reception, chuppah, procession and dancing.",
               "להקת כליזמר ובלקן חיה לחתונה שלכם: קבלת פנים, חופה, תהלוכה וריקודים."),
    "epk": ("Biography, press photos, technical rider and videos of Di Gasn Trio.",
            "ביוגרפיה, תמונות לעיתונות, מפרט טכני וסרטונים של די גאסן טריו."),
    "privacy": ("How gasntrio.com handles your information.", "איך האתר gasntrio.com מטפל במידע שלכם."),
}

PRIVACY = {
    "en": """<p>This site does not use advertising or tracking cookies. If you send us a message through the contact form, your details (name, email, phone and message) are delivered to our email through the Web3Forms service and are used only to reply to you.</p>
<p>Embedded YouTube videos load only when you press play, using YouTube's privacy-enhanced mode. The Bandsintown and Spotify players are provided by those services and are subject to their own privacy policies.</p>
<p>To ask about or delete information you sent us, write to <a href="mailto:gasntrio@gmail.com">gasntrio@gmail.com</a>.</p>""",
    "he": """<p>האתר אינו משתמש בעוגיות פרסום או מעקב. אם תשלחו לנו הודעה דרך טופס יצירת הקשר, הפרטים שלכם (שם, אימייל, טלפון וההודעה) יישלחו לתיבת המייל שלנו דרך השירות Web3Forms וישמשו רק כדי לחזור אליכם.</p>
<p>סרטוני יוטיוב נטענים רק כשלוחצים על ניגון, במצב הפרטיות המוגברת של יוטיוב. נגני Bandsintown וספוטיפיי מסופקים על ידי השירותים האלה וכפופים למדיניות הפרטיות שלהם.</p>
<p>לשאלות על מידע ששלחתם לנו או לבקשה למחוק אותו, כתבו ל-<a href="mailto:gasntrio@gmail.com">gasntrio@gmail.com</a>.</p>""",
}


def build(page, lang):
    i = 0 if lang == "en" else 1
    t = lambda k: UI[k][i]
    pre = "/en/" if lang == "en" else "/"
    home = pre
    other = "he" if lang == "en" else "en"
    other_url = "/" + PAGES[page][other]
    self_url = "/" + PAGES[page][lang]
    sec = lambda s: (home + "#" + s) if page != "home" else "#" + s
    cur = lambda p: ' aria-current="page"' if p == page else ""
    dir_ = "ltr" if lang == "en" else "rtl"

    head = f"""<!doctype html>
<html lang="{lang}" dir="{dir_}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLES[page][i]}</title>
<meta name="description" content="{DESCS[page][i]}">
<link rel="canonical" href="{SITE}{self_url}">
<link rel="alternate" hreflang="he" href="{SITE}/{PAGES[page]['he']}">
<link rel="alternate" hreflang="en" href="{SITE}/{PAGES[page]['en']}">
<link rel="alternate" hreflang="x-default" href="{SITE}/{PAGES[page]['he']}">
<meta property="og:title" content="{TITLES[page][i]}">
<meta property="og:description" content="{DESCS[page][i]}">
<meta property="og:image" content="{SITE}/images/hero.jpg">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Suez+One&family=Assistant:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body data-page="{page}">
<a class="skip" href="#main">{t('skip')}</a>
<header class="bar">
  <div class="wrap bar-inner">
    <a class="logo" href="{home}"><img src="/images/logo-cream.png" alt="Di Gasn Trio · די גאסן טריו" width="160" height="50"></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{t('menu')}</button>
    <nav id="nav" aria-label="Main">
      <a href="{sec('about')}">{t('nav_about')}</a>
      <a href="{sec('shows')}">{t('nav_shows')}</a>
      <a href="{sec('music')}">{t('nav_music')}</a>
      <a href="{pre}events/"{cur('events')}>{t('nav_events')}</a>
      <a href="{pre}epk/"{cur('epk')}>{t('nav_epk')}</a>
      <a class="lang" href="{other_url}" hreflang="{other}" lang="{other}">{t('lang_other')}</a>
      <a class="btn small" href="#contact">{t('nav_book')}</a>
    </nav>
  </div>
</header>
<main id="main">
"""
    types = "".join(f"<option>{o}</option>" for o in t("f_types").split("|"))
    contact = f"""
<section class="contact" id="contact">
  <div class="wrap contact-grid">
    <div>
      <h2>{t('contact_title')}</h2>
      <p class="lead">{t('contact_text')}</p>
      <div class="direct" id="direct"></div>
    </div>
    <form id="form" action="https://api.web3forms.com/submit" method="POST" hidden>
      <input type="hidden" name="access_key" id="form-key">
      <input type="hidden" name="subject" value="gasntrio.com">
      <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
      <label>{t('f_name')}<input name="name" required autocomplete="name"></label>
      <label>{t('f_email')}<input name="email" type="email" required autocomplete="email"></label>
      <label>{t('f_phone')}<input name="phone" type="tel" autocomplete="tel"></label>
      <label>{t('f_date')}<input name="event_date" type="date"></label>
      <label class="full">{t('f_type')}<select name="event_type">{types}</select></label>
      <label class="full">{t('f_msg')}<textarea name="message" required></textarea></label>
      <div class="full"><button class="btn" type="submit">{t('f_send')}</button></div>
      <p class="form-status full" id="form-status" role="status"></p>
    </form>
  </div>
</section>
"""
    foot = f"""</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div><img src="/images/logo-cream.png" alt="Di Gasn Trio" width="172" height="54"><ul id="social"></ul></div>
      <div id="foot-contact"></div>
    </div>
    <p class="fine">© <span id="year"></span> Di Gasn Trio · {t('rights')}<a href="{pre}privacy/">{t('privacy')}</a></p>
  </div>
</footer>
<script src="/app.js" defer></script>
</body>
</html>
"""

    if page == "home":
        body = f"""
<section class="hero">
  <img id="hero-img" src="/images/hero.jpg" alt="" fetchpriority="high">
  <div class="wrap">
    <p class="kicker" data-c="home.kicker"></p>
    <h1>{'Di Gasn Trio' if lang == 'en' else 'די גאסן טריו'}<span class="sub" lang="{other}">{'די גאסן טריו' if lang == 'en' else 'Di Gasn Trio'}</span></h1>
    <p class="tag" data-c="home.tagline"></p>
    <div class="ctas"><a class="btn" href="#contact">{t('cta_book')}</a><a class="btn ghost" href="#music">{t('cta_listen')}</a><a class="btn ghost" href="{pre}events/">{t('cta_events')}</a></div>
  </div>
</section>

<section id="shows">
  <div class="wrap">
    <div class="shows-head"><h2>{t('shows_title')}</h2><img src="/images/collage-birds.webp" alt="" width="170" height="147" loading="lazy"></div>
    <div id="shows-list"></div>
    <div class="bit-box" id="bit-box"><h3>{t('bit_title')}</h3><div id="bit"></div></div>
  </div>
</section>

<section class="about" id="about">
  <div class="wrap">
    <div class="about-grid">
      <div><h2 data-c="home.about_title"></h2><div id="about-text"></div></div>
      <div class="blob"><img src="/images/collage-hero.webp" alt="" width="452" height="502" loading="lazy"></div>
    </div>
    <ul class="highlights" id="highlights"></ul>
    <blockquote class="quote"><span data-c="home.quote"></span><cite data-c="home.quote_by"></cite></blockquote>
    <h2 style="margin-top:64px">{t('band_title')}</h2>
    <div id="members"></div>
  </div>
</section>

<section id="music">
  <div class="wrap">
    <h2>{t('music_title')}</h2>
    <div class="featured" id="featured"></div>
    <div id="videos"></div>
    <h2 style="margin-top:64px">{t('albums_title')}</h2>
    <div class="albums" id="albums"></div>
  </div>
</section>
"""
    elif page == "events":
        body = f"""
<section class="hero short">
  <img id="events-hero" src="/images/events.jpg" alt="" fetchpriority="high">
  <div class="wrap">
    <p class="kicker">{t('events_kicker')}</p>
    <h1 data-c="events.title" style="font-size:clamp(2.6rem,7vw,5.4rem)"></h1>
    <p class="tag" data-c="events.intro"></p>
    <div class="ctas"><a class="btn" href="#contact">{t('cta_book')}</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <h2>{t('services_title')}</h2>
    <p class="lead" data-c="events.question"></p>
    <div class="services" id="services"></div>
  </div>
</section>
<section class="band-text">
  <div class="wrap two">
    <div id="events-text"></div>
    <div class="stack"><h3 style="font-size:1.6rem;color:var(--indigo);margin:0">{t('watch_title')}</h3><div class="stack" id="events-videos"></div></div>
  </div>
</section>
<section class="testimonials">
  <div class="wrap">
    <h2>{t('testimonials_title')}</h2>
    <div id="testimonials"></div>
  </div>
</section>
<section style="padding-bottom:0">
  <div class="wrap gallery">
    <img src="/images/alley.jpg" alt="" loading="lazy"><img src="/images/procession.jpg" alt="" loading="lazy"><img src="/images/dance.jpg" alt="" loading="lazy">
  </div>
</section>
"""
    elif page == "epk":
        body = f"""
<section class="hero short">
  <img src="/images/live-3.jpg" alt="" fetchpriority="high">
  <div class="wrap">
    <p class="kicker">{t('epk_kicker')}</p>
    <h1 style="font-size:clamp(2.8rem,8vw,6rem)">{t('epk_title')}</h1>
    <p class="tag" data-c="press.intro"></p>
    <div class="downloads" id="downloads"></div>
  </div>
</section>
<section>
  <div class="wrap two">
    <div><h2>{t('bio_title')}</h2><div id="about-text"></div><blockquote class="quote" style="color:var(--indigo)"><span data-c="home.quote"></span><cite style="color:var(--coral)" data-c="home.quote_by"></cite></blockquote></div>
    <div><h2>{t('live_title')}</h2><p class="lead" data-c="press.live"></p><ul class="pill-list" id="experience"></ul>
      <h3 style="font-size:1.6rem;color:var(--indigo);margin:40px 0 10px">{t('festivals_title')}</h3><ul class="festivals" id="festivals"></ul></div>
  </div>
</section>
<section class="about">
  <div class="wrap"><h2>{t('band_title')}</h2><div id="members" style="margin-top:20px"></div></div>
</section>
<section>
  <div class="wrap"><h2>{t('music_title')}</h2><div id="videos"></div></div>
</section>
<section style="padding-top:0">
  <div class="wrap"><h2>{t('photos_title')}</h2><div class="gallery" id="photos"></div></div>
</section>
"""
    else:
        body = f"""
<section style="padding-top:60px">
  <div class="wrap" style="max-width:780px">
    <h1 style="font-size:2.6rem;color:var(--indigo)">{t('privacy')}</h1>
    {PRIVACY[lang]}
  </div>
</section>
"""
        contact = ""

    html = head + body + contact + foot
    out = ROOT / PAGES[page][lang] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


for p in PAGES:
    for l in ("he", "en"):
        build(p, l)
