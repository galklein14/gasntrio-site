# gasntrio.com

האתר של די גאסן טריו, בעברית ובאנגלית. HTML, CSS ו-JavaScript, בלי שרת ובלי מנוי.

## כתובות
האנגלית היא שפת ברירת המחדל; העברית תחת `/he/`.

| עמוד | English | עברית |
|---|---|---|
| דף הבית | `/` | `/he/` |
| About | `/about/` | `/he/about/` |
| Concerts | `/concerts/` | `/he/concerts/` |
| Music | `/music/` | `/he/music/` |
| מופעים ואירועים | `/events/` | `/he/di-gasn-events/` |
| חתונות (עמוד נחיתה) | `/wedding/` | `/he/lpwedding/` |
| EPK | `/epk/` | `/he/epk/` |
| מדיניות פרטיות | `/privacypolicy/` | `/he/privacypolicy/` |

הכתובות הישנות מ-Wix שהיו בעברית (`/lpwedding`, `/di-gasn-events`) מופנות לגרסה העברית בקובץ `_redirects`.

## איפה עורכים
כל התוכן נמצא בתיקייה `content/`, ועורכים אותו דרך **Pages CMS** (app.pagescms.org, כניסה עם GitHub). לכל טקסט יש שדה בעברית ושדה באנגלית.

| בתפריט הניהול | קובץ |
|---|---|
| הופעות | `content/shows.json` |
| מוזיקה וסרטונים | `content/music.json` |
| דף הבית | `content/home.json` |
| חברי ההרכב | `content/members.json` |
| מופעים ואירועים | `content/stage.json` |
| חתונות (עמוד נחיתה) | `content/events.json` |
| ערכת עיתונות | `content/press.json` |
| הגדרות כלליות | `content/general.json` |

כל שמירה נשמרת ב-GitHub, ו-Cloudflare Pages מעדכן את האתר תוך כדקה.

## הופעות
- הופעות מ-Bandsintown מופיעות אוטומטית בווידג'ט.
- הופעה שמוסיפים ידנית (הופעות ← הוספה) מוצגת מעליו, והיא נעלמת לבד אחרי שהתאריך עבר.

## טופס יצירת קשר
הטופס מופיע רק אחרי שמכניסים מפתח Web3Forms בהגדרות כלליות. מפתח חינמי מקבלים ב-web3forms.com עם המייל gasntrio@gmail.com. עד אז מוצגים וואטסאפ, טלפונים ומייל.

## מבנה העמודים
את המבנה והתוויות הקבועות (תפריט, כותרות) בונים מ-`tools/build.py`. אחרי שינוי שם מריצים `python3 tools/build.py`. הצבעים והגופנים מוגדרים בראש `style.css`.
