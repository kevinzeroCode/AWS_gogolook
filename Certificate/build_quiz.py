
#!/usr/bin/env python3
"""Parse AIF PDF and generate complete AWS quiz HTML"""

import pdfplumber, re, json, sys
sys.path.insert(0, "C:/Users/USER/Documents/AWS/Certificate")
from clf_data import CLF_QUESTIONS
from clf_new_batch import NEW_CLF
from clf_batch2 import CLF_BATCH2
from clf_batch3 import CLF_BATCH3
from clf_batch4 import CLF_BATCH4
from clf_batch5 import CLF_BATCH5
from aif_batch1 import AIF_BATCH1
from aif_batch2 import AIF_BATCH2
from aif_batch3 import AIF_BATCH3
from aif_batch4 import AIF_BATCH4
from aif_batch5 import AIF_BATCH5

try:
    import wordninja
    HAS_NINJA = True
except ImportError:
    HAS_NINJA = False

# ── Text fixer ────────────────────────────────────────────────────────────────
def fix_token(tok):
    if not HAS_NINJA:
        return tok
    alpha = re.sub(r'[^a-zA-Z]', '', tok)
    if len(alpha) <= 5 or re.search(r'\d', tok):
        return tok
    m = re.match(r'^([^a-zA-Z]*)(.*?)([^a-zA-Z]*)$', tok)
    if m:
        pre, core, suf = m.group(1), m.group(2), m.group(3)
        if len(core) > 7:
            segs = wordninja.split(core)
            if core and core[0].isupper() and segs:
                segs[0] = segs[0].capitalize()
            return pre + ' '.join(segs) + suf
    return tok

def smart_fix(text):
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    parts = re.split(r'(\s+)', text)
    text = ''.join(fix_token(p) if not re.match(r'\s+', p) else p for p in parts)
    for pat, rep in [
        (r'\bA I\b','AI'),(r'\bM L\b','ML'),(r'\bL L M\b','LLM'),
        (r'\bR A G\b','RAG'),(r'\bA W S\b','AWS'),(r'\bG A N\b','GAN'),
        (r'\bN L P\b','NLP'),(r'\bF M\b','FM'),(r'\bF Ms\b','FMs'),
        (r'\bS L M\b','SLM'),(r'\bB L E U\b','BLEU'),(r'\bR O U G E\b','ROUGE'),
        (r'\bR M S E\b','RMSE'),(r'\bR L H F\b','RLHF'),(r'\bI a C\b','IaC'),
        (r'\bP D P\b','PDP'),(r'\bP D Ps\b','PDPs'),(r'\bC S A T\b','CSAT'),
        (r'\bchat bot\b','chatbot'),(r'\bdata set\b','dataset'),
        (r'\bfine tune\b','fine-tune'),(r'\bfine tuning\b','fine-tuning'),
        (r'\bpre trained\b','pre-trained'),(r'\bon premises\b','on-premises'),
        (r'\bwork flow\b','workflow'),(r'\bbase line\b','baseline'),
    ]:
        text = re.sub(pat, rep, text)
    return re.sub(r'  +', ' ', text).strip()

# ── AIF Parser ────────────────────────────────────────────────────────────────
def parse_aif():
    full = ""
    with pdfplumber.open("C:/Users/USER/Documents/AWS/Certificate/AIF-C01-1-2.pdf") as pdf:
        for pg in pdf.pages:
            t = pg.extract_text()
            if t:
                full += "\n" + t
    for p in [
        r'Questions&AnswersPDF Page\d+', r'https?://\S+',
        r'Amazon\s*\nAIF-C01 Exam.*?Certified AI Practitioner\s*\n',
        r'Product Questions:.*?\n', r'Version:.*?\n',
        r"I'll continue.*?(?:tuned|shortly)[\.\!]\s*\n",
        r"Sure[\.,]?\s*[Cc]ontinuing.*?\n",
        r"Letmeknow.*?\n", r"Yousaid:.*?\n", r"ChatGPTsaid:.*?\n",
        r"Explanation:\s*\n", r"Thank You for Purchasing.*",
        r"Download Free.*", r"Test Your Preparation.*",
        r"Use Coupon.*", r"Practice Exam Software.*",
    ]:
        full = re.sub(p, '', full, flags=re.DOTALL|re.IGNORECASE)

    parts = re.split(r'\nQuestion:\s*(\d+)\s*\n', full)
    questions = []
    for i in range(1, len(parts), 2):
        qnum = int(parts[i])
        block = parts[i+1] if i+1 < len(parts) else ""
        am = re.search(r'\nAnswer:\s*([A-E,\s]+?)(?:\n|$)', block)
        if not am:
            continue
        corr = [a.strip() for a in re.split(r'[,\s]+', am.group(1).strip()) if a.strip() in list('ABCDE')]
        content = block[:am.start()]
        opts = {}
        op = re.compile(r'\n([A-E])\.([^\n]+(?:\n(?![A-E]\.|Answer:|Question:)[^\n]*)*)')
        fp = None
        for m in op.finditer(content):
            if fp is None: fp = m.start()
            opts[m.group(1)] = smart_fix(re.sub(r'\s+',' ',m.group(2)).strip())
        qt = smart_fix(re.sub(r'\s+',' ', content[:fp].strip() if fp else content.strip()))
        if not qt or not opts or not corr:
            continue
        questions.append({
            'id': qnum, 'exam': 'AIF',
            'question': qt, 'question_zh': '',
            'options': {k: {'en': v, 'zh': ''} for k,v in opts.items()},
            'correct': corr, 'multi': len(corr) > 1,
            'explanations': {k: ('✗ CORRECT — ' if k in corr else '✗ Incorrect — ') + v
                             for k,v in opts.items()}
        })
    return questions

# ── Convert CLF to unified format ─────────────────────────────────────────────
def convert_clf():
    out = []
    for q in CLF_QUESTIONS + NEW_CLF + CLF_BATCH2 + CLF_BATCH3 + CLF_BATCH4 + CLF_BATCH5:
        opts = {k: {'en': v['en'], 'zh': v['zh']} for k,v in q['options'].items()}
        out.append({
            'id': q['id'], 'exam': 'CLF',
            'question': q['question'], 'question_zh': q['question_zh'],
            'options': opts, 'correct': q['correct'], 'multi': q['multi'],
            'explanations': q['explanations']
        })
    return out

# ── Main ──────────────────────────────────────────────────────────────────────
print("Parsing AIF PDF...")
aif_qs = parse_aif()
# Merge manually added AIF questions (avoid duplicate IDs)
existing_aif_ids = {q['id'] for q in aif_qs}
for q in AIF_BATCH1 + AIF_BATCH2 + AIF_BATCH3 + AIF_BATCH4 + AIF_BATCH5:
    if q['id'] not in existing_aif_ids:
        aif_qs.append(q)
        existing_aif_ids.add(q['id'])
print(f"  → {len(aif_qs)} AIF questions extracted")

clf_qs = convert_clf()
print(f"  → {len(clf_qs)} CLF questions loaded")

all_data = {'aif': aif_qs, 'clf': clf_qs}
with open("C:/Users/USER/Documents/AWS/Certificate/quiz_data.json","w",encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)
print("  → quiz_data.json saved")

# ── HTML Generator ────────────────────────────────────────────────────────────
JSON_STR = json.dumps(all_data, ensure_ascii=False)

HTML = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AWS 認證考試練習 | AWS Certification Quiz</title>
<style>
:root{
  --bg:#0f1117;--card:#1a1d27;--card2:#22263a;--border:#2e3352;
  --accent:#ff9900;--accent2:#146eb4;--green:#2ecc71;--red:#e74c3c;
  --orange:#f39c12;--text:#e8eaf6;--muted:#8892b0;
  --radius:14px;--shadow:0 4px 24px #0006;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh;display:flex;flex-direction:column;align-items:center}
.screen{width:100%;max-width:860px;padding:24px 16px;display:none}
.screen.active{display:block}

/* HOME */
.home-hero{text-align:center;padding:50px 0 32px}
.home-hero h1{font-size:2.4rem;font-weight:800;background:linear-gradient(135deg,#ff9900,#146eb4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:8px}
.home-hero p{color:var(--muted);font-size:1.05rem;margin-bottom:36px}
.exam-cards{display:grid;grid-template-columns:1fr 1fr;gap:20px;max-width:640px;margin:0 auto}
.exam-card{background:var(--card);border:2px solid var(--border);border-radius:var(--radius);padding:28px 20px;cursor:pointer;transition:.2s;text-align:center;position:relative}
.exam-card:hover{border-color:var(--accent);transform:translateY(-3px);box-shadow:var(--shadow)}
.exam-card .badge{display:inline-block;background:var(--accent);color:#000;font-weight:800;font-size:.8rem;padding:3px 10px;border-radius:20px;margin-bottom:10px}
.exam-card.clf .badge{background:var(--accent2);color:#fff}
.exam-card h2{font-size:1.3rem;margin-bottom:6px}
.exam-card p{color:var(--muted);font-size:.9rem;line-height:1.6}
.review-chip{display:inline-block;background:#3a2200;color:var(--orange);border:1px solid var(--orange);border-radius:20px;font-size:.75rem;padding:2px 8px;margin-top:8px;font-weight:600}

/* MODE */
.mode-header{text-align:center;margin-bottom:28px}
.mode-header h2{font-size:1.8rem;font-weight:700;margin-bottom:6px}
.mode-header p{color:var(--muted)}
.mode-cards{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;max-width:700px;margin:0 auto 24px}
.mode-card{background:var(--card);border:2px solid var(--border);border-radius:var(--radius);padding:22px 16px;cursor:pointer;transition:.2s;text-align:center}
.mode-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.mode-card.review-mode{border-color:#3a2200}
.mode-card.review-mode:hover{border-color:var(--orange)}
.mode-card.disabled{opacity:.4;cursor:not-allowed;pointer-events:none}
.mode-card h3{font-size:1rem;margin-bottom:5px}
.mode-card p{color:var(--muted);font-size:.8rem;line-height:1.4}
.mode-card .icon{font-size:1.8rem;margin-bottom:8px}
.review-count{display:inline-block;background:var(--orange);color:#000;border-radius:20px;font-size:.75rem;padding:1px 8px;font-weight:700;margin-top:6px}
.practice-opts{background:var(--card);border-radius:var(--radius);padding:20px;max-width:400px;margin:0 auto;text-align:center}
.practice-opts label{color:var(--muted);font-size:.9rem;display:block;margin-bottom:8px}
.practice-opts input[type=range]{width:100%;accent-color:var(--accent);margin:8px 0}
.n-display{font-size:1.4rem;font-weight:700;color:var(--accent)}
.btn{background:var(--accent);color:#000;border:none;border-radius:8px;padding:12px 28px;font-size:1rem;font-weight:700;cursor:pointer;transition:.2s;display:inline-block}
.btn:hover{opacity:.85;transform:translateY(-1px)}
.btn.secondary{background:transparent;color:var(--muted);border:1px solid var(--border)}
.btn.secondary:hover{border-color:var(--text);color:var(--text)}
.btn.danger{background:#c0392b;color:#fff}
.back-btn{background:none;border:none;color:var(--muted);cursor:pointer;font-size:.9rem;padding:4px 0;margin-bottom:20px;display:flex;align-items:center;gap:6px}
.back-btn:hover{color:var(--text)}

/* QUIZ */
.quiz-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;gap:10px}
.progress-wrap{flex:1;background:var(--card2);border-radius:99px;height:6px;overflow:hidden}
.progress-bar{height:100%;background:linear-gradient(90deg,#ff9900,#146eb4);transition:.4s}
.quiz-counter{font-size:.82rem;color:var(--muted);white-space:nowrap}
.lang-toggle{background:var(--card2);border:1px solid var(--border);color:var(--text);border-radius:6px;padding:4px 10px;font-size:.78rem;cursor:pointer;white-space:nowrap}
.question-card{background:var(--card);border-radius:var(--radius);padding:24px;margin-bottom:16px;border:1px solid var(--border);position:relative}
.q-top-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;gap:8px}
.question-card .q-label{font-size:.72rem;color:var(--accent);font-weight:700;letter-spacing:.08em}
.review-tag{background:#3a2200;color:var(--orange);border:1px solid var(--orange);border-radius:6px;font-size:.7rem;padding:2px 8px;font-weight:600;white-space:nowrap}
.question-card .q-text{font-size:1.08rem;line-height:1.7;margin-bottom:6px}
.question-card .q-text-zh{font-size:.92rem;color:var(--muted);line-height:1.6}
.multi-hint{font-size:.78rem;color:var(--accent);margin-top:8px;font-style:italic}
.options-grid{display:flex;flex-direction:column;gap:9px}
.opt-btn{background:var(--card2);border:2px solid var(--border);border-radius:10px;padding:13px 16px;cursor:pointer;transition:.15s;text-align:left;width:100%;color:var(--text);display:flex;align-items:flex-start;gap:13px}
.opt-btn:hover:not(:disabled){border-color:var(--accent)}
.opt-btn .opt-letter{background:var(--border);border-radius:5px;padding:2px 8px;font-weight:700;font-size:.82rem;min-width:26px;text-align:center;flex-shrink:0;margin-top:2px}
.opt-btn .opt-body{flex:1}
.opt-btn .opt-en{font-size:.93rem;line-height:1.5}
.opt-btn .opt-zh{font-size:.8rem;color:var(--muted);margin-top:2px}
.opt-btn.selected{border-color:var(--accent2)}
.opt-btn.selected .opt-letter{background:var(--accent2)}
.opt-btn.correct{border-color:var(--green)!important;background:#152a1e}
.opt-btn.correct .opt-letter{background:var(--green);color:#000}
.opt-btn.wrong{border-color:var(--red)!important;background:#2a1515}
.opt-btn.wrong .opt-letter{background:var(--red)}
.opt-btn:disabled{cursor:default}
.submit-row{display:flex;justify-content:center;margin:14px 0}

/* EXPLANATION */
.explanation-panel{background:var(--card);border-radius:var(--radius);padding:18px;border:1px solid var(--border);margin-bottom:14px}
.explanation-panel h4{font-size:.78rem;color:var(--accent);font-weight:700;letter-spacing:.1em;margin-bottom:12px}
.exp-item{display:flex;gap:10px;margin-bottom:11px;align-items:flex-start}
.exp-letter{font-weight:700;font-size:.78rem;background:var(--border);border-radius:4px;padding:2px 7px;min-width:24px;text-align:center;flex-shrink:0;margin-top:1px}
.exp-letter.correct{background:var(--green);color:#000}
.exp-letter.wrong{background:var(--red)}
.exp-text{font-size:.86rem;line-height:1.58;color:#c8d0e8}
.result-badge{text-align:center;padding:13px;border-radius:10px;margin-bottom:14px;font-size:1.05rem;font-weight:700}
.result-badge.pass{background:#152a1e;color:var(--green);border:1px solid var(--green)}
.result-badge.fail{background:#2a1515;color:var(--red);border:1px solid var(--red)}
.next-row{display:flex;justify-content:center;gap:12px;margin-top:8px}

/* RESULTS */
.results-card{background:var(--card);border-radius:var(--radius);padding:30px;text-align:center;border:1px solid var(--border);margin-bottom:20px}
.score-circle{width:130px;height:130px;border-radius:50%;border:5px solid var(--accent);display:flex;flex-direction:column;align-items:center;justify-content:center;margin:0 auto 18px}
.score-circle .score-num{font-size:2.2rem;font-weight:800;color:var(--accent);line-height:1}
.score-circle .score-pct{font-size:.85rem;color:var(--muted);margin-top:2px}
.results-card h2{font-size:1.4rem;margin-bottom:6px}
.results-card p{color:var(--muted);font-size:.9rem}
.results-actions{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:18px}
.wrong-list{background:var(--card);border-radius:var(--radius);padding:18px;border:1px solid var(--border)}
.wrong-list h3{font-size:.95rem;margin-bottom:12px;color:var(--orange);display:flex;align-items:center;gap:8px}
.wrong-item{padding:10px 0;border-bottom:1px solid var(--border);font-size:.86rem}
.wrong-item:last-child{border-bottom:none}
.wrong-item .wi-q{color:var(--text);margin-bottom:3px;line-height:1.4}
.wrong-item .wi-ans{color:var(--muted);font-size:.8rem}

/* HISTORY CHIP */
.history-bar{background:var(--card2);border-radius:10px;padding:10px 14px;margin-bottom:18px;display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:.82rem;color:var(--muted)}
.history-bar span{color:var(--text)}
.history-bar button{background:none;border:1px solid var(--border);color:var(--muted);border-radius:6px;padding:3px 10px;cursor:pointer;font-size:.78rem}
.history-bar button:hover{border-color:var(--red);color:var(--red)}

@media(max-width:600px){
  .exam-cards{grid-template-columns:1fr}
  .mode-cards{grid-template-columns:1fr 1fr}
  .home-hero h1{font-size:1.8rem}
  .mode-cards .mode-card:last-child{grid-column:1/-1}
}
@media(max-width:400px){
  .mode-cards{grid-template-columns:1fr}
}
</style>
</head>
<body>

<!-- ═══ HOME ═══ -->
<div id="screen-home" class="screen active">
  <div class="home-hero">
    <h1>AWS 認證考試練習</h1>
    <p>AWS Certification Practice Quiz · 中英文雙語</p>
  </div>
  <div class="exam-cards">
    <div class="exam-card" onclick="selectExam('AIF')">
      <div class="badge">AIF-C01</div>
      <h2>AI Practitioner</h2>
      <p>AWS 認證 AI 從業者<br><span id="aif-count"></span> 題</p>
      <div id="aif-review-chip"></div>
    </div>
    <div class="exam-card clf" onclick="selectExam('CLF')">
      <div class="badge">CLF-C02</div>
      <h2>Cloud Practitioner</h2>
      <p>AWS 認證雲端從業者<br><span id="clf-count"></span> 題</p>
      <div id="clf-review-chip"></div>
    </div>
  </div>
</div>

<!-- ═══ MODE ═══ -->
<div id="screen-mode" class="screen">
  <button class="back-btn" onclick="showScreen('home')">← 返回 Back</button>
  <div class="mode-header">
    <h2 id="mode-title"></h2>
    <p id="mode-subtitle"></p>
  </div>
  <div id="mode-history-bar" class="history-bar" style="display:none">
    <div>📚 累積錯題 Wrong history: <span id="history-count">0</span> 題 | 上次練習正確率: <span id="last-acc">-</span></div>
    <button onclick="clearHistory()">清除記錄 Clear</button>
  </div>
  <div class="mode-cards">
    <div class="mode-card" onclick="startMode('full')">
      <div class="icon">📋</div>
      <h3>完整考試</h3>
      <p>Full Exam<br>全部題目隨機排序</p>
    </div>
    <div class="mode-card" onclick="openPractice()">
      <div class="icon">🎯</div>
      <h3>隨機練習</h3>
      <p>Practice<br>自選題數隨機抽題</p>
    </div>
    <div class="mode-card review-mode" id="review-mode-card" onclick="startMode('review')">
      <div class="icon">🔁</div>
      <h3>複習錯題</h3>
      <p>Review Wrong<br>優先出現答錯的題</p>
      <div class="review-count" id="review-count-badge">0 題</div>
    </div>
  </div>
  <div class="practice-opts" id="practice-opts" style="display:none">
    <label>題數 Number of questions</label>
    <div class="n-display" id="n-display">20</div>
    <input type="range" id="n-slider" min="5" max="87" value="20" oninput="updateN(this.value)">
    <br><br>
    <button class="btn" onclick="startMode('practice')">開始練習 Start</button>
  </div>
</div>

<!-- ═══ QUIZ ═══ -->
<div id="screen-quiz" class="screen">
  <div class="quiz-top">
    <button class="back-btn" style="margin:0;padding:0" onclick="confirmExit()">✕</button>
    <div class="progress-wrap"><div class="progress-bar" id="prog-bar"></div></div>
    <span class="quiz-counter" id="quiz-counter">1 / 20</span>
    <button class="lang-toggle" id="lang-btn" onclick="toggleLang()">中文</button>
  </div>
  <div class="question-card">
    <div class="q-top-row">
      <div class="q-label" id="q-label">QUESTION 1</div>
      <div class="review-tag" id="review-tag" style="display:none">⚠ 錯過 Need Review</div>
    </div>
    <div class="q-text" id="q-text"></div>
    <div class="q-text-zh" id="q-text-zh" style="display:none"></div>
    <div class="multi-hint" id="multi-hint" style="display:none">⚡ 多選題 — 請選所有正確答案 Select ALL correct answers</div>
  </div>
  <div class="options-grid" id="options-grid"></div>
  <div class="submit-row" id="submit-row" style="display:none">
    <button class="btn" onclick="submitAnswer()">確認 Submit</button>
  </div>
  <div id="explanation-area"></div>
  <div class="next-row" id="next-row" style="display:none">
    <button class="btn" id="next-btn" onclick="nextQuestion()">下一題 Next →</button>
  </div>
</div>

<!-- ═══ RESULTS ═══ -->
<div id="screen-results" class="screen">
  <div class="results-card">
    <div class="score-circle">
      <span class="score-num" id="res-score">0/0</span>
      <span class="score-pct" id="res-pct">0%</span>
    </div>
    <h2 id="res-title"></h2>
    <p id="res-sub"></p>
    <div class="results-actions">
      <button class="btn" onclick="retryQuiz()">重新練習 Retry</button>
      <button class="btn secondary" id="res-review-btn" onclick="selectExam(currentExam);showScreen('mode')">回選單 Menu</button>
      <button class="btn secondary" onclick="showScreen('home')">首頁 Home</button>
    </div>
  </div>
  <div class="wrong-list" id="wrong-list" style="display:none">
    <h3>⚠ 答錯的題目 Wrong Answers <span id="wrong-count-badge"></span></h3>
    <div id="wrong-items"></div>
  </div>
</div>

<script>
const RAW = """ + JSON_STR + """;

const QUESTIONS = {
  AIF: RAW.aif.map(q => ({...q,
    options: Object.fromEntries(Object.entries(q.options).map(([k,v])=>[k,typeof v==='string'?{en:v,zh:''}:v]))
  })),
  CLF: RAW.clf
};

// ── localStorage helpers ──────────────────────────────────────────────────────
function wrongKey(exam){ return 'aws_wrong_' + exam; }
function lastAccKey(exam){ return 'aws_lastacc_' + exam; }

function loadWrongIds(exam){
  try{ return new Set(JSON.parse(localStorage.getItem(wrongKey(exam))) || []); }
  catch{ return new Set(); }
}
function saveWrongIds(exam, set){
  localStorage.setItem(wrongKey(exam), JSON.stringify([...set]));
}
function loadLastAcc(exam){
  return localStorage.getItem(lastAccKey(exam));
}
function saveLastAcc(exam, pct){
  localStorage.setItem(lastAccKey(exam), pct + '%');
}

// ── State ─────────────────────────────────────────────────────────────────────
let currentExam = 'AIF';
let quizQuestions = [];
let qIndex = 0, score = 0;
let wrongAnswers = [];   // this session
let showChinese = false;
let selectedOpts = new Set();
let answered = false;
let lastMode = 'full';
let lastN = 20;
let sessionWrongIds = new Set();  // ids wrong this session (to update storage at end)
let sessionRightIds = new Set();

// ── Init ──────────────────────────────────────────────────────────────────────
function initHome(){
  document.getElementById('aif-count').textContent = QUESTIONS.AIF.length;
  document.getElementById('clf-count').textContent = QUESTIONS.CLF.length;
  ['AIF','CLF'].forEach(exam => {
    const wc = loadWrongIds(exam).size;
    const chip = document.getElementById(exam.toLowerCase()+'-review-chip');
    chip.innerHTML = wc > 0 ? `<span class="review-chip">⚠ ${wc} 題需複習</span>` : '';
  });
}
initHome();

// ── Navigation ────────────────────────────────────────────────────────────────
function showScreen(name){
  document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
  document.getElementById('screen-'+name).classList.add('active');
  window.scrollTo(0,0);
}

function selectExam(exam){
  currentExam = exam;
  document.getElementById('mode-title').textContent =
    exam==='AIF' ? 'AIF-C01 · AI Practitioner' : 'CLF-C02 · Cloud Practitioner';
  document.getElementById('mode-subtitle').textContent =
    exam==='AIF' ? 'AWS 認證 AI 從業者' : 'AWS 認證雲端從業者';

  const mx = QUESTIONS[exam].length;
  const sl = document.getElementById('n-slider');
  sl.max = mx; sl.value = Math.min(parseInt(sl.value)||20, mx);
  updateN(sl.value);
  document.getElementById('practice-opts').style.display = 'none';

  // Wrong history bar
  const wids = loadWrongIds(exam);
  const hbar = document.getElementById('mode-history-bar');
  const lacc = loadLastAcc(exam);
  if(wids.size > 0 || lacc){
    hbar.style.display = 'flex';
    document.getElementById('history-count').textContent = wids.size;
    document.getElementById('last-acc').textContent = lacc || '-';
  } else {
    hbar.style.display = 'none';
  }

  // Review mode card
  const rc = document.getElementById('review-count-badge');
  const rcard = document.getElementById('review-mode-card');
  rc.textContent = wids.size + ' 題';
  rcard.classList.toggle('disabled', wids.size === 0);

  showScreen('mode');
}

function openPractice(){
  const po = document.getElementById('practice-opts');
  po.style.display = po.style.display==='none' ? 'block' : 'none';
}
function updateN(val){ lastN=parseInt(val); document.getElementById('n-display').textContent=val; }

function shuffle(arr){
  const a=[...arr];
  for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}
  return a;
}

// ── Start Quiz ────────────────────────────────────────────────────────────────
function startMode(mode){
  lastMode = mode;
  const pool = QUESTIONS[currentExam];
  const wids = loadWrongIds(currentExam);

  if(mode==='full'){
    quizQuestions = shuffle([...pool]);
  } else if(mode==='practice'){
    // Prioritize wrong questions, fill rest randomly
    const wrong = shuffle(pool.filter(q => wids.has(q.id)));
    const rest  = shuffle(pool.filter(q => !wids.has(q.id)));
    quizQuestions = [...wrong, ...rest].slice(0, lastN);
  } else if(mode==='review'){
    // Only wrong questions
    const wrong = pool.filter(q => wids.has(q.id));
    if(wrong.length===0){ alert('目前沒有錯題記錄！\\nNo wrong answers recorded yet.'); return; }
    quizQuestions = shuffle(wrong);
  }

  qIndex=0; score=0; wrongAnswers=[];
  sessionWrongIds=new Set(); sessionRightIds=new Set();
  startQuestion();
  showScreen('quiz');
}

function retryQuiz(){ startMode(lastMode); }

// ── Question ──────────────────────────────────────────────────────────────────
function startQuestion(){
  const q = quizQuestions[qIndex];
  answered=false; selectedOpts=new Set();
  const wids = loadWrongIds(currentExam);

  // Progress
  document.getElementById('prog-bar').style.width = (qIndex/quizQuestions.length*100)+'%';
  document.getElementById('quiz-counter').textContent = `${qIndex+1} / ${quizQuestions.length}`;
  document.getElementById('q-label').textContent = `${q.exam} · Q${q.id}`;

  // Review tag
  const rt = document.getElementById('review-tag');
  rt.style.display = wids.has(q.id) ? 'inline-block' : 'none';

  // Question text
  document.getElementById('q-text').textContent = q.question;
  const zhEl = document.getElementById('q-text-zh');
  if(q.question_zh){ zhEl.textContent=q.question_zh; zhEl.style.display=showChinese?'block':'none'; }
  else { zhEl.style.display='none'; }

  document.getElementById('multi-hint').style.display = q.multi?'block':'none';

  // Options
  const grid = document.getElementById('options-grid');
  grid.innerHTML='';
  Object.entries(q.options).forEach(([letter,opt])=>{
    const btn=document.createElement('button');
    btn.className='opt-btn'; btn.dataset.letter=letter;
    btn.onclick=()=>handleOptClick(btn,q);
    const zhHtml = opt.zh ? `<div class="opt-zh" style="display:${showChinese?'block':'none'}">${opt.zh}</div>` : '';
    btn.innerHTML=`<span class="opt-letter">${letter}</span><span class="opt-body"><div class="opt-en">${opt.en}</div>${zhHtml}</span>`;
    grid.appendChild(btn);
  });

  document.getElementById('submit-row').style.display = q.multi?'flex':'none';
  document.getElementById('explanation-area').innerHTML='';
  document.getElementById('next-row').style.display='none';
}

function handleOptClick(btn,q){
  if(answered) return;
  const l=btn.dataset.letter;
  if(q.multi){
    selectedOpts.has(l) ? (selectedOpts.delete(l), btn.classList.remove('selected'))
                        : (selectedOpts.add(l),    btn.classList.add('selected'));
  } else {
    selectedOpts=new Set([l]);
    document.querySelectorAll('.opt-btn').forEach(b=>b.classList.remove('selected'));
    btn.classList.add('selected');
    revealAnswer(q);
  }
}

function submitAnswer(){
  if(selectedOpts.size===0) return;
  revealAnswer(quizQuestions[qIndex]);
}

function revealAnswer(q){
  answered=true;
  document.getElementById('submit-row').style.display='none';
  const correct=new Set(q.correct);
  const userCorr=[...selectedOpts].every(s=>correct.has(s)) && selectedOpts.size===correct.size;

  // Update persistent wrong list
  const wids = loadWrongIds(currentExam);
  if(userCorr){ wids.delete(q.id); sessionRightIds.add(q.id); }
  else { wids.add(q.id); sessionWrongIds.add(q.id); }
  saveWrongIds(currentExam, wids);

  if(userCorr) score++;
  else wrongAnswers.push({q, selected:[...selectedOpts]});

  // Color options
  document.querySelectorAll('.opt-btn').forEach(btn=>{
    btn.disabled=true;
    const l=btn.dataset.letter;
    if(correct.has(l)) btn.classList.add('correct');
    else if(selectedOpts.has(l)) btn.classList.add('wrong');
  });

  // Result badge
  const expArea=document.getElementById('explanation-area');
  const badge=document.createElement('div');
  badge.className='result-badge '+(userCorr?'pass':'fail');
  badge.textContent=userCorr?'✓ 正確！Correct!':'✗ 答錯了 Incorrect';
  expArea.appendChild(badge);

  // Explanations panel
  if(q.explanations){
    const panel=document.createElement('div');
    panel.className='explanation-panel';
    panel.innerHTML='<h4>EXPLANATION · 解析</h4>';
    Object.entries(q.options).forEach(([letter])=>{
      const isCorr=correct.has(letter);
      const item=document.createElement('div');
      item.className='exp-item';
      item.innerHTML=`<span class="exp-letter ${isCorr?'correct':'wrong'}">${letter}</span><span class="exp-text">${q.explanations[letter]||''}</span>`;
      panel.appendChild(item);
    });
    expArea.appendChild(panel);
  }

  // Next button
  document.getElementById('next-row').style.display='flex';
  document.getElementById('next-btn').textContent =
    qIndex>=quizQuestions.length-1 ? '查看結果 Results →' : '下一題 Next →';
  expArea.scrollIntoView({behavior:'smooth',block:'start'});
}

function nextQuestion(){
  qIndex++;
  if(qIndex>=quizQuestions.length){ showResults(); }
  else { startQuestion(); window.scrollTo(0,0); }
}

// ── Results ───────────────────────────────────────────────────────────────────
function showResults(){
  const total=quizQuestions.length;
  const pct=Math.round(score/total*100);
  saveLastAcc(currentExam, pct);

  document.getElementById('res-score').textContent=`${score}/${total}`;
  document.getElementById('res-pct').textContent=pct+'%';
  document.getElementById('res-title').textContent=pct>=70?'🎉 恭喜通過！Passed!':'📚 繼續加油 Keep studying!';

  const wids=loadWrongIds(currentExam);
  document.getElementById('res-sub').textContent=
    `正確率 ${pct}% · 答對 ${score}，答錯 ${total-score}  |  累積錯題 ${wids.size} 題`;

  const wi=document.getElementById('wrong-items');
  wi.innerHTML='';
  if(wrongAnswers.length>0){
    document.getElementById('wrong-count-badge').textContent='('+wrongAnswers.length+')';
    wrongAnswers.forEach(({q,selected})=>{
      const div=document.createElement('div');
      div.className='wrong-item';
      div.innerHTML=`<div class="wi-q">Q${q.id}. ${q.question.substring(0,90)}${q.question.length>90?'…':''}</div>
        <div class="wi-ans">您答 You: <b>${selected.join(',')}</b> · 正確 Correct: <b>${q.correct.join(',')}</b></div>`;
      wi.appendChild(div);
    });
    document.getElementById('wrong-list').style.display='block';
  } else {
    document.getElementById('wrong-list').style.display='none';
  }

  initHome(); // refresh review chips on home
  showScreen('results');
}

// ── Language Toggle ───────────────────────────────────────────────────────────
function toggleLang(){
  showChinese=!showChinese;
  document.getElementById('lang-btn').textContent=showChinese?'EN':'中文';
  const q=quizQuestions[qIndex];
  if(!q) return;
  const zhEl=document.getElementById('q-text-zh');
  zhEl.style.display=(showChinese&&q.question_zh)?'block':'none';
  document.querySelectorAll('.opt-btn').forEach(btn=>{
    const zhDiv=btn.querySelector('.opt-zh');
    if(zhDiv) zhDiv.style.display=showChinese?'block':'none';
  });
}

function confirmExit(){
  if(confirm('確定要離開考試嗎？進度不會儲存。\\nExit the quiz? Progress will be lost.')) showScreen('home');
}

function clearHistory(){
  if(confirm('確定要清除所有錯題記錄嗎？\\nClear all wrong answer history?')){
    localStorage.removeItem(wrongKey(currentExam));
    localStorage.removeItem(lastAccKey(currentExam));
    selectExam(currentExam);
    initHome();
  }
}
</script>
</body>
</html>"""

out_path = "C:/Users/USER/Documents/AWS/Certificate/aws_quiz.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"\n✅ Generated: {out_path}")
print(f"   AIF: {len(aif_qs)} questions  |  CLF: {len(clf_qs)} questions")
