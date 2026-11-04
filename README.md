# gasntrio.com

האתר של די גאסן טריו, בעברית ובאנגלית. HTML, CSS ו-JavaScript, בלי שרת ובלי מנוי.

## כתובות
| עמוד | עברית | English |
|---|---|---|
| דף הבית | `/` | `/en/` |
| חתונות ואירועים | `/events/` | `/en/events/` |
| ערכת עיתונות | `/epk/` | `/en/epk/` |
| מדיניות פרטיות | `/privacy/` | `/en/privacy/` |

הכתובות הישנות מ-Wix (`/about`, `/concerts`, `/music`, `/lpwedding`, `/di-gasn-events`, `/privacypolicy`) מופנות לעמודים החדשים בקובץ `_redirects`.

## איפה עורכים
כל התוכן נמצא בתיקייה `content/`, ועורכים אותו דרך **Pages CMS** (app.pagescms.org, כניסה עם GitHub). לכל טקסט יש שדה בעברית ושדה באנגלית.

| בתפריט הניהול | קובץ |
|---|---|
| הופעות | `content/shows.json` |
| מוזיקה וסרטונים | `content/music.json` |
| דף הבית | `content/home.json` |
| חברי ההרכב | `content/members.json` |
| חתונות ואירועים | `content/events.json` |
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
