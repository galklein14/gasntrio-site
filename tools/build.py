#!/usr/bin/env python3
"""Builds the Hebrew and English HTML pages from the templates below.

Run after changing page structure or interface labels:  python3 tools/build.py
Day-to-day content (texts, shows, videos, members) lives in content/*.json and
is edited through Pages CMS, with no build step.
"""
import hashlib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://gasntrio.com"
# Version tags so browsers fetch the new CSS/JS after every change
VER = {f: hashlib.md5((ROOT / f).read_bytes()).hexdigest()[:8] for f in ("style.css", "app.js")}

# Same addresses as the original Wix site, so old links keep working.
# English is the default language (site root); Hebrew lives under /he/.
# The old Wix addresses /di-gasn-events and /lpwedding were Hebrew pages,
# so _redirects sends them to the Hebrew versions.
PAGES = {
    "home":     {"en": "",               "he": "he/"},
    "about":    {"en": "about/",         "he": "he/about/"},
    "concerts": {"en": "concerts/",      "he": "he/concerts/"},
    "music":    {"en": "music/",         "he": "he/music/"},
    "events":   {"en": "events/",        "he": "he/di-gasn-events/"},
    "wedding":  {"en": "wedding/",       "he": "he/lpwedding/"},
    "epk":      {"en": "epk/",           "he": "he/epk/"},
    "privacy":  {"en": "privacypolicy/", "he": "he/privacypolicy/"},
}

UI = {
    "skip": ("Skip to content", "דילוג לתוכן"),
    "menu": ("Menu", "תפריט"),
    "nav_about": ("About", "עלינו"),
    "nav_shows": ("Concerts", "הופעות"),
    "nav_music": ("Music", "מוזיקה"),
    "nav_events": ("Shows & Events", "מופעים ואירועים"),
    "nav_wedding": ("Weddings", "חתונות"),
    "nav_epk": ("EPK", "ערכת עיתונות"),
    "nav_home": ("Home", "בית"),
    "more_shows": ("All concerts", "לכל ההופעות"),
    "more_music": ("More music", "עוד מוזיקה"),
    "nav_book": ("Book us", "הזמינו אותנו"),
    "lang_other": ("עברית", "English"),
    "cta_book": ("Book the band", "הזמינו את הלהקה"),
    "cta_listen": ("Listen", "להאזנה"),
    "cta_events": ("Weddings & events", "לחתונות ואירועים"),
    "shows_title": ("Upcoming shows", "הופעות קרובות"),
    "bit_title": ("More dates from Bandsintown", "עוד תאריכים מ-Bandsintown"),
    "band_title": ("The band", "ההרכב"),
    "music_title": ("Listen & watch", "להאזין ולצפות"),
    "videos_title": ("Videos", "סרטונים"),
    "offer_title": ("What we offer", "מה אנחנו מציעים"),
    "wedding_more": ("Weddings: all the details", "לכל הפרטים על חתונות"),
    "watch_live": ("Watch us live", "ככה זה נראה על הבמה"),
    "press_title": ("Press & radio", "בתקשורת וברדיו"),
    "downloads_title": ("Downloads: press kit, photos, tech rider", "להורדה: ערכת עיתונות, תמונות, מפרט טכני"),
    "epk_hint": ("Open the sections you need.", "פתחו את החלקים שאתם צריכים."),
    "insta_title": ("On Instagram", "באינסטגרם"),
    "insta_follow": ("Follow us", "עקבו אחרינו"),
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
    "about": ("About | Di Gasn Trio", "עלינו | די גאסן טריו"),
    "concerts": ("Concerts | Original Klezmer-Balkan band | Di Gasn Trio", "הופעות | להקת כליזמר-בלקן | די גאסן טריו"),
    "music": ("Music | Original Klezmer-Balkan band | Di Gasn Trio", "מוזיקה | להקת כליזמר-בלקן | די גאסן טריו"),
    "wedding": ("Klezmer band for your wedding | Di Gasn Trio", "להקת כליזמר לחתונה | די גאסן טריו"),
    "events": ("Shows & events | Di Gasn Trio", "מופעים ואירועים | די גאסן טריו"),
    "epk": ("Press kit | Di Gasn Trio", "ערכת עיתונות | די גאסן טריו"),
    "privacy": ("Privacy policy | Di Gasn Trio", "מדיניות פרטיות | די גאסן טריו"),
}
DESCS = {
    "about": ("Di Gasn Trio: the story of the band and its musicians.", "די גאסן טריו: הסיפור של הלהקה והנגנים."),
    "concerts": ("Upcoming concerts of Di Gasn Trio in Israel and abroad.", "ההופעות הקרובות של די גאסן טריו בארץ ובחו״ל."),
    "music": ("Albums, singles and videos of Di Gasn Trio.", "אלבומים, סינגלים וסרטונים של די גאסן טריו."),
    "wedding": ("A live klezmer and Balkan band for your wedding: reception, chuppah, procession and dancing.", "להקת כליזמר ובלקן חיה לחתונה שלכם: קבלת פנים, חופה, תהלוכה וריקודים."),
    "home": ("Di Gasn Trio: klezmer and Balkan music from Jerusalem. Concerts, festivals, weddings and events in Israel and abroad.",
             "די גאסן טריו: מוזיקת כליזמר ובלקן מירושלים. הופעות, פסטיבלים, חתונות ואירועים בארץ ובחו״ל."),
    "events": ("Themed concerts, masterclasses, private concerts, life-cycle events and lectures with Di Gasn Trio.",
               "מופעי תוכן, כיתות אמן, הופעות לקבוצות, טקסי חיים ואירועים פרטיים והרצאות עם די גאסן טריו."),
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
    link = lambda p: "/" + PAGES[p][lang]
    home = link("home")
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
<link rel="alternate" hreflang="x-default" href="{SITE}/{PAGES[page]['en']}">
<meta property="og:title" content="{TITLES[page][i]}">
<meta property="og:description" content="{DESCS[page][i]}">
<meta property="og:image" content="{SITE}/images/hero.jpg">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Suez+One&family=Assistant:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v={VER['style.css']}">
</head>
<body data-page="{page}">
<a class="skip" href="#main">{t('skip')}</a>
<header class="bar">
  <div class="wrap bar-inner">
    <a class="logo" href="{home}"><img src="/images/logo-cream.png" alt="Di Gasn Trio · די גאסן טריו" width="160" height="50"></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{t('menu')}</button>
    <nav id="nav" aria-label="Main">
      <a href="{link("about")}"{cur('about')}>{t('nav_about')}</a>
      <a href="{link("concerts")}"{cur('concerts')}>{t('nav_shows')}</a>
      <a href="{link("music")}"{cur('music')}>{t('nav_music')}</a>
      <a href="{link("events")}"{cur('events')}>{t('nav_events')}</a>
      <a href="{link("epk")}"{cur('epk')}>{t('nav_epk')}</a>
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
    <p class="fine">© <span id="year"></span> Di Gasn Trio · {t('rights')}<a href="{link("privacy")}">{t('privacy')}</a></p>
  </div>
</footer>
<script src="/app.js?v={VER['app.js']}" defer></script>
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
    <div class="ctas"><a class="btn" href="#contact">{t('cta_book')}</a><a class="btn ghost" href="{link("music")}">{t('cta_listen')}</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="featured" id="featured"></div>
    <div id="videos" data-limit="2" class="pair"></div>
    <p style="margin-top:28px"><a class="btn ink" href="{link("music")}">{t('more_music')}</a></p>
  </div>
</section>
<section class="about">
  <div class="wrap">
    <div class="shows-head"><h2>{t('shows_title')}</h2><img src="/images/collage-birds.webp" alt="" width="170" height="147" loading="lazy"></div>
    <div id="shows-list" data-limit="3" class="on-dark"></div>
    <p style="margin-top:20px"><a class="btn" href="{link("concerts")}">{t('more_shows')}</a></p>
  </div>
</section>
<section class="insta" id="insta">
  <div class="wrap">
    <div class="insta-head"><h2>{t('insta_title')}</h2><a class="btn ink" id="insta-link" href="https://www.instagram.com/balkan.klezmer.band/" target="_blank" rel="noopener">{t('insta_follow')} · @balkan.klezmer.band</a></div>
    <div class="insta-embed" id="insta-embed"></div>
  </div>
</section>
"""
    elif page == "about":
        body = f"""
<section class="about" style="padding-top:clamp(48px,7vw,80px)">
  <div class="wrap">
    <div class="about-grid">
      <div><p class="kicker" style="color:var(--khaki)">{t('nav_about')}</p><h1 class="page-title light" data-c="home.about_title"></h1><div id="about-text"></div></div>
      <div class="blob"><img src="/images/collage-hero.webp" alt="" width="452" height="502"></div>
    </div>
    <ul class="highlights" id="highlights"></ul>
    <blockquote class="quote"><span data-c="home.quote"></span><cite data-c="home.quote_by"></cite></blockquote>
  </div>
</section>
<section>
  <div class="wrap">
    <h2>{t('band_title')}</h2>
    <div id="members" data-full="1" class="full-bios"></div>
  </div>
</section>
<section class="press-sec" id="press-sec" style="padding-top:0">
  <div class="wrap"><h2>{t('press_title')}</h2><div class="media-list" id="media"></div></div>
</section>
"""
    elif page == "concerts":
        body = f"""
<section>
  <div class="wrap">
    <div class="shows-head"><h1 class="page-title">{t('shows_title')}</h1><img src="/images/collage-birds.webp" alt="" width="170" height="147"></div>
    <div id="shows-list"></div>
    <div class="bit-box" id="bit-box"><h3>{t('bit_title')}</h3><div id="bit"></div></div>
  </div>
</section>
"""
    elif page == "music":
        body = f"""
<section>
  <div class="wrap">
    <h1 class="page-title">{t('music_title')}</h1>
    <div class="featured" id="featured"></div>
    <h2>{t('albums_title')}</h2>
    <div class="albums" id="albums"></div>
    <h2 style="margin-top:64px">{t('videos_title')}</h2>
    <div id="videos"></div>
  </div>
</section>
"""
    elif page == "events":
        body = f"""
<section class="hero short">
  <img id="stage-hero" src="/images/live-2.jpg" alt="" fetchpriority="high">
  <div class="wrap">
    <p class="kicker">{t('nav_events')}</p>
    <h1 data-c="stage.title" style="font-size:clamp(2.6rem,7vw,5.4rem)"></h1>
    <p class="tag" data-c="stage.intro"></p>
    <div class="ctas"><a class="btn" href="#contact">{t('cta_book')}</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <h2>{t('offer_title')}</h2>
    <div class="services offerings" id="offerings"></div>
  </div>
</section>
<section class="wedding-band">
  <div class="wrap wedding-banner">
    <div class="slideshow" id="wedding-slides" aria-label="{t('nav_wedding')}"></div>
    <div><p class="kicker">{t('nav_wedding')}</p><h2 data-c="stage.wedding_title"></h2><p class="lead" data-c="stage.wedding_text"></p>
    <div id="wedding-clip" class="wedding-clip"></div>
    <a class="btn" href="{link('wedding')}">{t('wedding_more')}</a></div>
  </div>
</section>
<section class="about">
  <div class="wrap two">
    <div><h2>{t('live_title')}</h2><p class="lead" data-c="press.live"></p><ul class="pill-list" id="experience"></ul>
      <blockquote class="quote"><span data-c="home.quote"></span><cite data-c="home.quote_by"></cite></blockquote></div>
    <div><h3 style="font-size:1.6rem;margin:0 0 10px;color:var(--khaki)">{t('festivals_title')}</h3><ul class="festivals on-dark" id="festivals"></ul></div>
  </div>
</section>
"""
    elif page == "wedding":
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
  </div>
</section>
<section class="epk">
  <div class="wrap">
    <p class="lead epk-hint">{t('epk_hint')}</p>
    <details class="acc"><summary>{t('downloads_title')}</summary><div class="acc-body"><div class="downloads" id="downloads"></div></div></details>
    <details class="acc"><summary>{t('bio_title')}</summary><div class="acc-body"><div id="about-text"></div><blockquote class="quote" style="color:var(--indigo)"><span data-c="home.quote"></span><cite style="color:var(--coral)" data-c="home.quote_by"></cite></blockquote></div></details>
    <details class="acc"><summary>{t('live_title')}</summary><div class="acc-body"><p class="lead" data-c="press.live"></p><ul class="pill-list" id="experience"></ul></div></details>
    <details class="acc"><summary>{t('festivals_title')}</summary><div class="acc-body"><ul class="festivals" id="festivals"></ul></div></details>
    <details class="acc"><summary>{t('band_title')}</summary><div class="acc-body"><div id="members"></div></div></details>
    <details class="acc"><summary>{t('music_title')}</summary><div class="acc-body"><div id="videos"></div></div></details>
    <details class="acc" id="press-sec"><summary>{t('press_title')}</summary><div class="acc-body"><div class="media-list" id="media"></div></div></details>
    <details class="acc"><summary>{t('photos_title')}</summary><div class="acc-body"><div class="gallery" id="photos"></div></div></details>
  </div>
</section>
"""
    else:
        body = f"""
<section style="padding-top:60px">
  <div class="wrap" style="max-width:780px">
    <h1 class="page-title">{t('privacy')}</h1>
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
