// Di Gasn Trio — renders page content from the JSON files in content/.
// Edit content through the admin panel (Pages CMS), not here.

(async function () {
  const $ = (s, el = document) => el.querySelector(s);
  const lang = document.documentElement.lang === "en" ? "en" : "he";
  const L = (o, k) => (o ? o[`${k}_${lang}`] ?? o[`${k}_he`] ?? o[`${k}_en`] ?? "" : "");
  const h = (tag, attrs = {}, ...kids) => {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (v == null || v === false) continue;
      if (k === "text") el.textContent = v;
      else if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
      else el.setAttribute(k, v === true ? "" : v);
    }
    for (const kid of kids.flat()) if (kid != null && kid !== "") el.append(kid);
    return el;
  };
  const UI = {
    tickets: ["Tickets", "כרטיסים"], noShows: ["No public shows on the calendar right now. Book us for your event!", "כרגע אין הופעות פתוחות לקהל ביומן. אפשר להזמין אותנו לאירוע שלכם!"],
    follow: ["Get show alerts on Bandsintown", "קבלו התראות על הופעות ב-Bandsintown"],
    play: ["Play", "ניגון"], bio: ["Bio", "ביוגרפיה"], site: ["Website", "לאתר"],
    sending: ["Sending…", "שולח…"], sent: ["Thank you! We'll get back to you soon.", "תודה! נחזור אליכם בקרוב."],
    failed: ["The message wasn't sent. Please try again, or write to us directly.", "ההודעה לא נשלחה. נסו שוב, או כתבו לנו ישירות."],
    listen: ["Listen", "להאזנה"], whatsapp: ["WhatsApp", "וואטסאפ"],
  };
  const u = (k) => UI[k][lang === "en" ? 0 : 1];

  const load = (n) => fetch(`/content/${n}.json`, { cache: "no-cache" }).then((r) => { if (!r.ok) throw new Error(n); return r.json(); });
  let g, home, members, shows, music, events, press, stage;
  try {
    [g, home, members, shows, music, events, press, stage] = await Promise.all(["general", "home", "members", "shows", "music", "events", "press", "stage"].map(load));
  } catch (e) {
    document.body.prepend(h("p", { style: "background:#E4573D;color:#fff;padding:12px;margin:0;text-align:center", text: lang === "en" ? "The site content could not be loaded. Refresh the page to try again." : "לא הצלחנו לטעון את תוכן האתר. רעננו את הדף כדי לנסות שוב." }));
    return;
  }
  const data = { home, events, press, music, stage };

  // Bilingual text bindings: data-c="home.tagline" reads home.tagline_he / tagline_en
  document.querySelectorAll("[data-c]").forEach((el) => {
    const [src, key] = el.dataset.c.split(".");
    const v = L(data[src], key);
    if (v) el.textContent = v;
  });
  const paras = (box, list) => { if (box) box.replaceChildren(...(list || []).map((t) => h("p", { text: t }))); };

  // Click-to-play YouTube
  const ytId = (v) => { const m = String(v || "").match(/(?:v=|youtu\.be\/|embed\/|shorts\/|live\/)([\w-]{11})/); return m ? m[1] : String(v || "").trim(); };
  function player(link, title) {
    const id = ytId(link);
    const box = h("div", { class: "player" });
    const btn = h("button", { type: "button", "aria-label": `${u("play")}: ${title || ""}`, onclick: () => {
      box.replaceChildren(h("iframe", { src: `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`, title: title || "YouTube", allow: "autoplay; encrypted-media; picture-in-picture; fullscreen", allowfullscreen: true }));
    } },
      h("img", { src: `https://i.ytimg.com/vi/${id}/hqdefault.jpg`, alt: "", loading: "lazy" }),
      h("span", { class: "play", "aria-hidden": "true" }));
    btn.querySelector(".play").innerHTML = '<svg viewBox="0 0 24 24" width="28" height="28"><path d="M8 5l11 7-11 7z" fill="#fff"/></svg>';
    box.append(btn);
    return box;
  }
  const videoCard = (v) => h("article", { class: "video" }, player(v.youtube, L(v, "title")), h("h3", { text: L(v, "title") }), L(v, "caption") ? h("p", { text: L(v, "caption") }) : null);

  // Home hero image
  if ($("#hero-img") && home.hero_image) $("#hero-img").src = home.hero_image;
  if ($("#events-hero") && events.hero_image) $("#events-hero").src = events.hero_image;
  if ($("#stage-hero") && stage.hero_image) $("#stage-hero").src = stage.hero_image;

  // About text (home + press kit)
  paras($("#about-text"), home[`about_${lang}`]);
  const hl = $("#highlights");
  if (hl) hl.replaceChildren(...(home.highlights || []).map((x) => h("li", {}, h("b", { text: x.big }), x[lang])));

  // Members
  const mb = $("#members");
  const fullBio = mb?.dataset.full;
  if (mb) mb.replaceChildren(...members.map((m) => h("article", { class: "member" },
    h("img", { src: m.image, alt: L(m, "name"), loading: "lazy", width: 320, height: 320 }),
    h("div", { class: "member-body" },
      h("h3", { text: L(m, "name") }),
      h("p", { class: "role", text: L(m, "role") }),
      fullBio ? h("p", { class: "bio", text: L(m, "bio") }) : null,
      fullBio && m.website ? h("p", { style: "margin:6px 0 0" }, h("a", { href: m.website, target: "_blank", rel: "noopener", text: u("site") })) : null,
      !fullBio && L(m, "bio") ? h("details", {}, h("summary", { text: u("bio") }), h("p", { text: L(m, "bio") }), m.website ? h("p", {}, h("a", { href: m.website, target: "_blank", rel: "noopener", text: u("site") })) : null) : null,
    ))));

  // Shows: hand-added list + Bandsintown widget
  const today = new Date().toISOString().slice(0, 10);
  const list = $("#shows-list");
  if (list) {
    const up = (shows || []).filter((s) => s.date && s.date >= today).sort((a, b) => (a.date + (a.time || "")).localeCompare(b.date + (b.time || ""))).slice(0, Number(list.dataset.limit) || undefined);
    const loc = lang === "en" ? "en-GB" : "he-IL";
    list.replaceChildren(...(up.length ? up.map((s) => {
      const d = new Date(s.date + "T12:00:00");
      return h("article", { class: "show" },
        h("div", { class: "show-date" }, h("b", { text: String(d.getDate()).padStart(2, "0") }), h("span", { text: d.toLocaleDateString(loc, { month: "short" }) })),
        h("div", {}, h("h3", { text: L(s, "title") }), h("p", { text: [d.toLocaleDateString(loc, { weekday: "long", day: "numeric", month: "long", year: "numeric" }), s.time, L(s, "place")].filter(Boolean).join(" · ") })),
        s.tickets ? h("a", { class: "btn small", href: s.tickets, target: "_blank", rel: "noopener", text: u("tickets") }) : null);
    }) : [h("p", { class: "empty", text: u("noShows") })]));
  }
  const bit = $("#bit");
  if (bit && g.bandsintown?.artist_id) {
    bit.replaceChildren(h("a", {
      class: "bit-widget-initializer",
      "data-artist-name": `id_${g.bandsintown.artist_id}`,
      "data-language": "en",
      "data-display-past-dates": "false",
      "data-display-limit": "all",
      "data-auto-style": "false",
      "data-background-color": "#FFF8E6",
      "data-text-color": "#1B1B2A",
      "data-link-color": "#E4573D",
      "data-separator-color": "rgba(72,73,120,0.25)",
      "data-font": "Assistant",
      "data-display-start-time": "true",
      "data-event-ticket-cta-bg-color": "#E4573D",
      "data-event-ticket-cta-text-color": "#FFFFFF",
      "data-event-ticket-cta-border-radius": "99px",
      "data-follow-section-cta-bg-color": "#484978",
      "data-display-play-my-city": "false",
    }), h("p", { class: "follow" }, h("a", { href: g.bandsintown.url, target: "_blank", rel: "noopener", text: u("follow") })));
    const sc = document.createElement("script");
    sc.src = "https://widgetv3.bandsintown.com/main.min.js"; sc.charset = "utf-8"; sc.async = true;
    document.body.append(sc);
  } else if ($("#bit-box")) $("#bit-box").hidden = true;

  // Music
  const f = music.featured, fb = $("#featured");
  if (fb) {
    if (f && L(f, "title")) fb.replaceChildren(
      f.image ? h("img", { src: f.image, alt: L(f, "title"), loading: "lazy", width: 300, height: 300 }) : null,
      h("div", {}, h("p", { class: "kicker", text: L(f, "kicker") }), h("h3", { text: L(f, "title") }), h("p", { text: L(f, "text") }),
        f.link ? h("a", { class: "btn", href: f.link, target: "_blank", rel: "noopener", text: u("listen") }) : null));
    else fb.hidden = true;
  }
  const vids = $("#videos");
  if (vids) vids.replaceChildren(...(music.videos || []).slice(0, Number(vids.dataset.limit) || undefined).map(videoCard));
  const al = $("#albums");
  if (al) al.replaceChildren(...(music.spotify_albums || []).map((id) =>
    h("iframe", { src: `https://open.spotify.com/embed/album/${String(id).split("album/").pop().split("?")[0]}?theme=0`, loading: "lazy", allow: "encrypted-media", title: "Spotify" })));

  // Events page
  const sv = $("#services");
  if (sv) sv.replaceChildren(...(events.services || []).map((s) => h("article", { class: "service" },
    s.image ? h("img", { src: s.image, alt: "", loading: "lazy" }) : null,
    h("div", {}, h("h3", { text: s[lang] }), h("p", { text: L(s, "text") })))));
  paras($("#events-text"), events[`paragraphs_${lang}`]);
  const ev = $("#events-videos");
  if (ev) ev.replaceChildren(...(events.videos || []).map((v) => player(v, "Di Gasn Trio")));
  const ts = $("#testimonials");
  if (ts) ts.replaceChildren(...(events.testimonials || []).map((x) =>
    h("blockquote", { class: "testimonial", lang: x.lang || null, dir: x.lang === "he" ? "rtl" : x.lang === "en" ? "ltr" : null }, h("p", { text: `“${x.text}”` }), h("cite", { text: x.by }))));

  // Shows & events page
  const of = $("#offerings");
  if (of) of.replaceChildren(...(stage.offerings || []).map((o) => {
    const card = h("article", { class: "service" },
      o.image ? h("img", { src: o.image, alt: "", loading: "lazy" }) : null,
      h("div", {}, h("h3", { text: o[lang] }), h("p", { text: L(o, "text") })));
    const href = L(o, "link") || o.link;
    return href ? h("a", { href, class: "card-link" }, card) : card;
  }));

  // Press & radio (shown only when there are items)
  const md = $("#media");
  if (md) {
    const items = (press.media || []).filter((m) => m.url).sort((a, b) => String(b.date || "").localeCompare(String(a.date || "")));
    const icon = { radio: "📻", article: "📰", tv: "📺", podcast: "🎙" };
    if (!items.length) $("#press-sec").hidden = true;
    else md.replaceChildren(...items.map((m) => h("a", { class: "media-item", href: m.url, target: "_blank", rel: "noopener" },
      h("span", { class: "media-icon", "aria-hidden": "true", text: icon[m.type] || "🔗" }),
      h("span", {}, h("b", { text: L(m, "title") }), h("small", { text: [L(m, "outlet"), m.date ? new Date(m.date + "T12:00:00").toLocaleDateString(lang === "en" ? "en-GB" : "he-IL", { month: "long", year: "numeric" }) : ""].filter(Boolean).join(" · ") })))));
  }

  // Instagram: a live-feed widget (if one is set in the admin panel), otherwise
  // individual posts pasted as links. Instagram's own profile embed no longer
  // shows posts, so it isn't used.
  const ig = g.instagram || {};
  if ($("#insta-link") && ig.url) $("#insta-link").href = ig.url;
  const ie = $("#insta-embed");
  if (ie && ig.widget) {
    ie.replaceChildren(h("iframe", { src: ig.widget, title: "Instagram", loading: "lazy", scrolling: "no", class: "insta-widget" }));
  } else if (ie && (ig.posts || []).length) {
    ie.classList.add("insta-grid");
    ie.replaceChildren(...ig.posts.slice(0, 6).map((url) => h("blockquote", { class: "instagram-media", "data-instgrm-permalink": url, "data-instgrm-version": "14" }, h("a", { href: url, target: "_blank", rel: "noopener", text: "Instagram" }))));
    const sc = document.createElement("script"); sc.src = "https://www.instagram.com/embed.js"; sc.async = true; document.body.append(sc);
  }

  // Wedding block on the Shows & events page: rotating photos + clip
  const ws = $("#wedding-slides");
  if (ws && (stage.wedding_photos || []).length) {
    const imgs = stage.wedding_photos.map((src, i) => h("img", { src, alt: "", loading: i ? "lazy" : null, class: i ? "" : "on" }));
    ws.replaceChildren(...imgs);
    let k = 0;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (imgs.length > 1 && !reduce) setInterval(() => { imgs[k].classList.remove("on"); k = (k + 1) % imgs.length; imgs[k].classList.add("on"); }, 4000);
  }
  if ($("#wedding-clip") && stage.wedding_video) $("#wedding-clip").replaceChildren(player(stage.wedding_video, L(stage, "wedding_title")));

  // Press kit page
  const dl = $("#downloads");
  if (dl) dl.replaceChildren(...(press.downloads || []).map((d, i) => h("a", { class: i ? "btn ghost" : "btn", href: d.url, target: "_blank", rel: "noopener", text: L(d, "label") })));
  const exp = $("#experience");
  if (exp) exp.replaceChildren(...(press.experience || []).map((x) => h("li", { text: x[lang] })));
  const fs = $("#festivals");
  if (fs) fs.replaceChildren(...(press.festivals || []).map((x) => h("li", { text: x[lang] })));
  const ph = $("#photos");
  if (ph) ph.replaceChildren(...(press.photos || []).map((src) => h("a", { href: src, target: "_blank", rel: "noopener" }, h("img", { src, alt: "Di Gasn Trio", loading: "lazy" }))));

  // Contact: direct links + form (the form shows only once a Web3Forms key is set)
  const tel = (n) => `tel:${n.replace(/[^+\d]/g, "")}`;
  const direct = [
    g.whatsapp ? h("a", { href: `https://wa.me/${g.whatsapp}`, target: "_blank", rel: "noopener" }, h("span", { text: "✆" }), u("whatsapp")) : null,
    ...(g.phones || []).map((p) => h("a", { href: tel(p.number) }, h("span", { text: "☎" }), h("bdi", { dir: "ltr", text: p.number }), ` · ${L(p, "name")}`)),
    g.email ? h("a", { href: `mailto:${g.email}` }, h("span", { text: "✉" }), g.email) : null,
  ];
  if ($("#direct")) $("#direct").replaceChildren(...direct);
  if ($("#foot-contact")) $("#foot-contact").replaceChildren(
    ...(g.phones || []).map((p) => h("p", { style: "margin:0" }, h("a", { href: tel(p.number), style: "text-decoration:none" }, h("bdi", { dir: "ltr", text: p.number })))),
    h("p", { style: "margin:0" }, h("a", { href: `mailto:${g.email}`, style: "text-decoration:none", text: g.email })));
  const form = $("#form");
  if (form && g.web3forms_key) {
    form.hidden = false;
    $("#form-key").value = g.web3forms_key;
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const status = $("#form-status"), btn = form.querySelector("button");
      status.textContent = u("sending"); btn.disabled = true;
      try {
        const r = await fetch(form.action, { method: "POST", headers: { Accept: "application/json" }, body: new FormData(form) });
        if (!r.ok) throw 0;
        form.reset(); $("#form-key").value = g.web3forms_key;
        status.textContent = u("sent");
      } catch { status.textContent = u("failed"); }
      finally { btn.disabled = false; }
    });
  }

  // Footer
  if ($("#social")) $("#social").replaceChildren(...(g.social || []).map((s) => h("li", {}, h("a", { href: s.url, target: "_blank", rel: "noopener", text: s.label }))));
  if ($("#year")) $("#year").textContent = new Date().getFullYear();

  // Mobile menu + sticky bar shadow
  const menuBtn = $(".menu-btn"), nav = $("#nav");
  menuBtn?.addEventListener("click", () => { const o = nav.classList.toggle("open"); menuBtn.setAttribute("aria-expanded", o); });
  nav?.addEventListener("click", (e) => { if (e.target.closest("a")) { nav.classList.remove("open"); menuBtn?.setAttribute("aria-expanded", "false"); } });
  const bar = $(".bar");
  const onScroll = () => bar.classList.toggle("scrolled", window.scrollY > 8);
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
})();
