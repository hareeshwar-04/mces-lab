// MCES Lab Experiments Application Logic
(function () {
  'use strict';

  let currentExp = null;
  let currentFileIndex = 0;
  let activeCategory = 'All';
  let searchTerm = '';

  // DOM Elements
  const searchInput = document.getElementById('searchInput');
  const countBadge = document.getElementById('countBadge');
  const filterBar = document.getElementById('filterBar');
  const homeView = document.getElementById('homeView');
  const detailView = document.getElementById('detailView');
  const grid = document.getElementById('grid');
  const emptyState = document.getElementById('emptyState');
  const backBtn = document.getElementById('backBtn');
  const prevExpBtn = document.getElementById('prevExpBtn');
  const nextExpBtn = document.getElementById('nextExpBtn');
  const expNum = document.getElementById('expNum');
  const expCategory = document.getElementById('expCategory');
  const expTitle = document.getElementById('expTitle');
  const expDesc = document.getElementById('expDesc');
  const expHardware = document.getElementById('expHardware');
  const tabsList = document.getElementById('tabsList');
  const fileName = document.getElementById('fileName');
  const fileLang = document.getElementById('fileLang');
  const copyBtn = document.getElementById('copyBtn');
  const downloadBtn = document.getElementById('downloadBtn');
  const codeViewer = document.getElementById('codeViewer');
  const toast = document.getElementById('toast');

  // Syntax Highlighting
  function highlightAsm(code) {
    const lines = code.split('\n');
    return lines.map(line => {
      // Comment
      const commentIdx = line.indexOf(';');
      let mainPart = commentIdx !== -1 ? line.substring(0, commentIdx) : line;
      let commentPart = commentIdx !== -1 ? line.substring(commentIdx) : '';

      // Escape HTML in mainPart
      mainPart = escapeHtml(mainPart);

      // Labels (e.g. EVL:, HERE:)
      mainPart = mainPart.replace(/\b([A-Za-z_][A-Za-z0-9_]*):/g, '<span class="hl-label">$1</span>:');

      // Directives
      mainPart = mainPart.replace(/\b(ORG|END|DB|DW|EQU|BIT|DATA|IDATA|XDATA)\b/gi, '<span class="hl-directive">$1</span>');

      // Opcodes
      mainPart = mainPart.replace(/\b(MOV|MOVC|MOVX|PUSH|POP|XCH|XCHD|ADD|ADDC|SUBB|INC|DEC|MUL|DIV|DA|ANL|ORL|XRL|CLR|CPL|RL|RLC|RR|RRC|SWAP|SETB|JC|JNC|JB|JNB|JBC|JZ|JNZ|CJNE|DJNZ|NOP|ACALL|LCALL|RET|RETI|AJMP|LJMP|SJMP|JMP)\b/gi, '<span class="hl-keyword">$1</span>');

      // Registers & SFRs
      mainPart = mainPart.replace(/\b([AB]|R[0-7]|DPTR|PC|PSW|SP|P[0-3]|TMOD|TCON|TH0|TL0|TH1|TL1|SCON|SBUF|IE|IP|CY|OV|P|TR0|TR1|TF0|TF1|TI|RI|P[0-3]\.[0-7])\b/gi, '<span class="hl-reg">$1</span>');

      // Hex / numbers / immediates
      mainPart = mainPart.replace(/(#0[0-9A-Fa-f]+H|#[0-9A-Fa-f]+H|#\d+|0[0-9A-Fa-f]+H|[0-9A-Fa-f]+H|\b\d+\b)/g, '<span class="hl-number">$1</span>');

      if (commentPart) {
        return mainPart + '<span class="hl-comment">' + escapeHtml(commentPart) + '</span>';
      }
      return mainPart;
    });
  }

  function highlightC(code) {
    const lines = code.split('\n');
    let inBlockComment = false;

    return lines.map(line => {
      let result = '';
      let i = 0;
      const len = line.length;

      // Handle block comment continuation
      if (inBlockComment) {
        const endIdx = line.indexOf('*/');
        if (endIdx !== -1) {
          inBlockComment = false;
          return '<span class="hl-comment">' + escapeHtml(line.substring(0, endIdx + 2)) + '</span>' + highlightCLine(line.substring(endIdx + 2));
        } else {
          return '<span class="hl-comment">' + escapeHtml(line) + '</span>';
        }
      }

      // Check for block comment start
      const startBlockIdx = line.indexOf('/*');
      if (startBlockIdx !== -1) {
        const endIdx = line.indexOf('*/', startBlockIdx + 2);
        if (endIdx !== -1) {
          // Self-contained block comment
          const before = highlightCLine(line.substring(0, startBlockIdx));
          const comment = '<span class="hl-comment">' + escapeHtml(line.substring(startBlockIdx, endIdx + 2)) + '</span>';
          const after = highlightCLine(line.substring(endIdx + 2));
          return before + comment + after;
        } else {
          inBlockComment = true;
          return highlightCLine(line.substring(0, startBlockIdx)) + '<span class="hl-comment">' + escapeHtml(line.substring(startBlockIdx)) + '</span>';
        }
      }

      // Check for line comment //
      const lineCommentIdx = line.indexOf('//');
      if (lineCommentIdx !== -1) {
        const before = highlightCLine(line.substring(0, lineCommentIdx));
        const comment = '<span class="hl-comment">' + escapeHtml(line.substring(lineCommentIdx)) + '</span>';
        return before + comment;
      }

      return highlightCLine(line);
    });
  }

  function highlightCLine(line) {
    let s = escapeHtml(line);

    // Preprocessor #include, #define
    s = s.replace(/(#(?:include|define|ifdef|ifndef|endif|pragma))\b(.*)/g, '<span class="hl-preproc">$1</span><span class="hl-string">$2</span>');

    // Strings
    s = s.replace(/(&quot;.*?&quot;|&#39;.*?&#39;|".*?"|'.*?')/g, '<span class="hl-string">$1</span>');

    // Keywords
    s = s.replace(/\b(while|for|if|else|do|return|switch|case|break|continue|default|interrupt)\b/g, '<span class="hl-keyword">$1</span>');

    // Types
    s = s.replace(/\b(void|unsigned|char|int|long|float|double|short|const|sbit|sfr|bit|typedef|struct|enum|static)\b/g, '<span class="hl-type">$1</span>');

    // SFR registers in 8051 & Arduino functions
    s = s.replace(/\b(P[0-3]|TMOD|TCON|TH0|TL0|TH1|TL1|SCON|SBUF|IE|IP|TR0|TR1|TF0|TF1|TI|RI|PSW|CY|pinMode|digitalWrite|digitalRead|delay|delayMicroseconds|pulseIn|Serial|OUTPUT|INPUT|HIGH|LOW|LED_BUILTIN|LiquidCrystal|begin|print|println|setCursor|noDisplay|display)\b/g, '<span class="hl-func">$1</span>');

    // Numbers & Hex
    s = s.replace(/\b(0x[0-9A-Fa-f]+|\d+)\b/g, '<span class="hl-number">$1</span>');

    return s;
  }

  function escapeHtml(text) {
    return text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function renderCodeBlock(code, lang) {
    let highlightedLines;
    if (lang === 'asm') {
      highlightedLines = highlightAsm(code);
    } else {
      highlightedLines = highlightC(code);
    }

    let html = '';
    highlightedLines.forEach((line, idx) => {
      html += '<div class="code-line">' +
        '<span class="line-num">' + (idx + 1) + '</span>' +
        '<span class="line-content">' + (line || ' ') + '</span>' +
        '</div>';
    });
    return html;
  }

  // Toast
  let toastTimer = null;
  function showToast(msg) {
    if (toastTimer) clearTimeout(toastTimer);
    toast.textContent = msg;
    toast.classList.add('show');
    toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, 2200);
  }

  // Categories extraction
  const categories = ['All'];
  EXPERIMENTS.forEach(exp => {
    if (!categories.includes(exp.category)) {
      categories.push(exp.category);
    }
  });

  // Render Filters
  function renderFilters() {
    filterBar.innerHTML = '';
    categories.forEach(cat => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'filter-btn' + (cat === activeCategory ? ' active' : '');
      let count = 0;
      if (cat === 'All') {
        count = EXPERIMENTS.length;
      } else {
        count = EXPERIMENTS.filter(e => e.category === cat).length;
      }
      btn.textContent = `${cat} (${count})`;
      btn.addEventListener('click', () => {
        activeCategory = cat;
        renderFilters();
        renderGrid();
      });
      filterBar.appendChild(btn);
    });
  }

  function getCategoryClass(cat) {
    switch (cat) {
      case '8051 Assembly': return 'pill-asm';
      case 'Embedded C': return 'pill-c';
      case 'I/O Ports': return 'pill-io';
      case 'Timers & Counters': return 'pill-timer';
      case 'Serial Communication': return 'pill-serial';
      case 'Interrupts': return 'pill-interrupt';
      case 'Arduino Development Board': return 'pill-arduino';
      default: return 'pill-c';
    }
  }

  // Render Grid
  function renderGrid() {
    grid.innerHTML = '';
    const q = searchTerm.toLowerCase().trim();

    const filtered = EXPERIMENTS.filter(exp => {
      const matchesCategory = activeCategory === 'All' || exp.category === activeCategory;
      if (!matchesCategory) return false;
      if (!q) return true;

      const titleMatch = exp.title.toLowerCase().includes(q);
      const descMatch = exp.desc.toLowerCase().includes(q);
      const catMatch = exp.category.toLowerCase().includes(q);
      const hwMatch = exp.hardware.toLowerCase().includes(q);
      const fileMatch = exp.files.some(f => f.name.toLowerCase().includes(q) || f.label.toLowerCase().includes(q));
      const codeMatch = exp.files.some(f => f.code.toLowerCase().includes(q));

      return titleMatch || descMatch || catMatch || hwMatch || fileMatch || codeMatch;
    });

    countBadge.textContent = `${filtered.length} of ${EXPERIMENTS.length} Experiments`;

    if (filtered.length === 0) {
      emptyState.style.display = 'block';
    } else {
      emptyState.style.display = 'none';
      filtered.forEach(exp => {
        const card = document.createElement('div');
        card.className = 'card';
        card.setAttribute('role', 'button');
        card.setAttribute('tabindex', '0');

        card.innerHTML = `
          <div>
            <div class="card-top">
              <span class="card-num">EXP ${exp.number < 10 ? '0' + exp.number : exp.number}</span>
              <span class="category-pill ${getCategoryClass(exp.category)}">${exp.category}</span>
            </div>
            <h3 class="card-title">${escapeHtml(exp.title)}</h3>
            <p class="card-desc">${escapeHtml(exp.desc)}</p>
          </div>
          <div class="card-footer">
            <span class="card-files-count">${exp.files.length} ${exp.files.length === 1 ? 'Program' : 'Programs'}</span>
            <span class="card-action-btn">View Code &rarr;</span>
          </div>
        `;

        card.addEventListener('click', () => {
          openDetail(exp);
        });

        grid.appendChild(card);
      });
    }
  }

  // Open Detail View
  function openDetail(exp, fileIdx = 0) {
    currentExp = exp;
    currentFileIndex = fileIdx;

    window.location.hash = exp.id;

    homeView.style.display = 'none';
    detailView.style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });

    expNum.textContent = `EXP ${exp.number < 10 ? '0' + exp.number : exp.number}`;
    expCategory.className = `category-pill ${getCategoryClass(exp.category)}`;
    expCategory.textContent = exp.category;
    expTitle.textContent = exp.title;
    expDesc.textContent = exp.desc;
    expHardware.textContent = exp.hardware;

    // Previous / Next button visibility and logic
    const curIdx = EXPERIMENTS.findIndex(e => e.id === exp.id);
    prevExpBtn.disabled = curIdx <= 0;
    nextExpBtn.disabled = curIdx >= EXPERIMENTS.length - 1;
    prevExpBtn.style.opacity = curIdx <= 0 ? '0.4' : '1';
    nextExpBtn.style.opacity = curIdx >= EXPERIMENTS.length - 1 ? '0.4' : '1';

    renderTabs();
    renderCurrentFile();
  }

  function renderTabs() {
    tabsList.innerHTML = '';
    currentExp.files.forEach((file, idx) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'tab-btn' + (idx === currentFileIndex ? ' active' : '');
      btn.innerHTML = `<span style="opacity:0.7">${file.lang.toUpperCase()}</span> ${escapeHtml(file.label)}`;
      btn.addEventListener('click', () => {
        currentFileIndex = idx;
        renderTabs();
        renderCurrentFile();
      });
      tabsList.appendChild(btn);
    });
  }

  function renderCurrentFile() {
    const file = currentExp.files[currentFileIndex];
    if (!file) return;

    fileName.textContent = file.name;
    fileLang.textContent = file.lang.toUpperCase();

    codeViewer.innerHTML = renderCodeBlock(file.code, file.lang);
  }

  function closeDetail() {
    detailView.style.display = 'none';
    homeView.style.display = 'block';
    history.pushState(null, null, ' ');
    currentExp = null;
  }

  // Copy code
  copyBtn.addEventListener('click', () => {
    if (!currentExp) return;
    const file = currentExp.files[currentFileIndex];
    if (!file) return;

    navigator.clipboard.writeText(file.code).then(() => {
      showToast(`Copied ${file.name} to clipboard!`);
    }).catch(() => {
      // Fallback
      const ta = document.createElement('textarea');
      ta.value = file.code;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      showToast(`Copied ${file.name} to clipboard!`);
    });
  });

  // Download code
  downloadBtn.addEventListener('click', () => {
    if (!currentExp) return;
    const file = currentExp.files[currentFileIndex];
    if (!file) return;

    const blob = new Blob([file.code], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = file.name;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast(`Downloading ${file.name}...`);
  });

  // Event Listeners
  backBtn.addEventListener('click', closeDetail);

  prevExpBtn.addEventListener('click', () => {
    if (!currentExp) return;
    const idx = EXPERIMENTS.findIndex(e => e.id === currentExp.id);
    if (idx > 0) {
      openDetail(EXPERIMENTS[idx - 1], 0);
    }
  });

  nextExpBtn.addEventListener('click', () => {
    if (!currentExp) return;
    const idx = EXPERIMENTS.findIndex(e => e.id === currentExp.id);
    if (idx < EXPERIMENTS.length - 1) {
      openDetail(EXPERIMENTS[idx + 1], 0);
    }
  });

  searchInput.addEventListener('input', (e) => {
    searchTerm = e.target.value;
    if (detailView.style.display !== 'none') {
      closeDetail();
    }
    renderGrid();
  });

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (detailView.style.display !== 'none') {
        closeDetail();
      }
    } else if (e.key === '/' && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput.focus();
    }
  });

  // Handle URL Hash navigation
  function handleHash() {
    const hash = window.location.hash.replace('#', '');
    if (hash) {
      const exp = EXPERIMENTS.find(e => e.id === hash);
      if (exp) {
        openDetail(exp);
        return;
      }
    }
    closeDetail();
  }

  window.addEventListener('hashchange', handleHash);

  // Initialize
  renderFilters();
  renderGrid();
  if (window.location.hash) {
    handleHash();
  }

})();
