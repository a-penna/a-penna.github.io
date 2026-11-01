/* a-penna.github.io: progressive enhancement only, the page works without JS.
   Perf rules: every scroll/mouse handler is rAF-throttled, writes only
   transform/opacity/CSS vars, and never reads layout inside the frame. */
(() => {
  const d = document, root = d.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const $ = (s, el = d) => el.querySelector(s), $$ = (s, el = d) => [...el.querySelectorAll(s)];
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const raf = fn => { let q = false; return (...a) => { if (q) return; q = true; requestAnimationFrame(() => { q = false; fn(...a); }); }; };

  // ---- reveal on scroll
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -10% 0px' });
  $$('.rv').forEach(el => io.observe(el));

  // ---- pointer: one listener drives spotlight + tilts
  let mx = innerWidth / 2, my = innerHeight / 2;
  const spot = $('.spot'), pointerJobs = [];
  if (fine && !reduce) {
    const tick = raf(() => {
      if (spot) spot.style.transform = `translate3d(${mx}px,${my}px,0)`, spot.style.backgroundPosition = `${260 - mx}px ${260 - my}px,0 0`;
      pointerJobs.forEach(f => f());
    });
    addEventListener('pointermove', e => { mx = e.clientX; my = e.clientY; spot && spot.classList.add('on'); tick(); }, { passive: true });
    d.addEventListener('pointerleave', () => spot && spot.classList.remove('on'));
  }

  // ---- hero terminal
  const tb = $('#tb');
  if (tb) {
    const cfg = JSON.parse($('#term-data').textContent), dock = $('#dock'), win = $('.win');
    const P = '<span class="p">alessandro@mac</span> <span class="d">~ %</span> ';
    const esc = s => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
    const steps = [
      { cmd: 'whoami' }, { out: `<span class="h">alessandro</span> <span class="d">${esc(cfg.whoami)}</span>` },
      { cmd: 'ls ~/apps' }, { out: '<div class="ls">' + cfg.apps.map(a => `<a href="${a.href}" style="color:${a.c}">${esc(a.name.replace(/ /g, '-'))}</a>`).join('') + '</div>' },
      { cmd: 'open ~/apps/*' }, { out: `<span class="d">${esc(cfg.launching)}</span>`, fn: () => dock.classList.add('on') },
      { cmd: '' }];
    let html = '';
    const show = (tail = '') => { tb.innerHTML = html + tail; };
    async function run() {
      if (reduce) { // final state, no typing
        steps.forEach(s => { if (s.out !== undefined) html += s.out + '<br>'; else if (s.cmd) html += P + `<span class="h">${s.cmd}</span><br>`; });
        show(P + '<span class="cur"></span>'); dock.classList.add('on'); return;
      }
      await wait(900);
      for (const s of steps) {
        if (s.out !== undefined) { html += s.out + '<br>'; show(); s.fn && s.fn(); await wait(420); continue; }
        await wait(s.cmd ? 450 : 0);
        for (let i = 0; i <= s.cmd.length; i++) { show(P + `<span class="h">${s.cmd.slice(0, i)}</span><span class="cur"></span>`); await wait(55 + Math.random() * 55); }
        if (s.cmd) { html += P + `<span class="h">${s.cmd}</span><br>`; await wait(320); }
      }
    }
    run();
    if (fine && !reduce && win) {
      let heroVisible = true;
      new IntersectionObserver(([e]) => heroVisible = e.isIntersecting).observe(win);
      pointerJobs.push(() => { if (heroVisible && innerWidth > 900) win.style.transform = `rotateY(${-10 + (mx / innerWidth - .5) * 12}deg) rotateX(${6 - (my / innerHeight - .5) * 10}deg)`; });
    }
  }

  // ---- portfolio: sticky stage driven by scroll position (layout cached)
  const pf = $('#pf');
  if (pf) {
    const chs = $$('.chap', pf), sics = $$('.sic', pf), tilts = $$('.sic .tilt', pf), rail = $('.rail', pf), ris = $$('a', rail), snum = $('.snum', pf);
    let tops = [], hs = [], pfTop = 0, pfH = 0, act = -1, mobile = false;
    const measure = () => {
      const y = scrollY; mobile = innerWidth <= 900;
      chs.forEach((c, i) => { const r = c.getBoundingClientRect(); tops[i] = r.top + y; hs[i] = r.height; });
      const r = pf.getBoundingClientRect(); pfTop = r.top + y; pfH = r.height; update();
    };
    const setAct = i => {
      if (i === act) return; act = i;
      sics.forEach((s, j) => { s.classList.toggle('on', j === i); s.classList.toggle('past', j < i); });
      ris.forEach((r, j) => r.classList.toggle('on', j === i));
      chs.forEach((c, j) => c.classList.toggle('on', j === i));
      pf.style.setProperty('--pc', chs[i].style.getPropertyValue('--c'));
      snum.textContent = String(i + 1).padStart(2, '0');
      const img = $('img', sics[i + 1] || sics[i]); if (img && img.loading === 'lazy') img.loading = 'eager'; // prefetch next
    };
    const update = () => {
      const vh = innerHeight, mid = scrollY + vh * (mobile ? .68 : .5);
      let best = 0, bd = Infinity;
      tops.forEach((t, i) => { const dd = Math.abs(t + hs[i] / 2 - mid); if (dd < bd) { bd = dd; best = i; } });
      setAct(best);
      if (!reduce) {
        const lp = (mid - (tops[best] + hs[best] / 2)) / hs[best];
        tilts[best].style.setProperty('--py', (-lp * 60).toFixed(1) + 'px');
        tilts[best].style.setProperty('--rx', (lp * 14).toFixed(2) + 'deg');
      }
      rail.style.setProperty('--prog', Math.min(1, Math.max(0, (mid - pfTop) / (pfH - vh * .5))).toFixed(3));
    };
    addEventListener('scroll', raf(update), { passive: true });
    addEventListener('resize', raf(measure));
    addEventListener('load', measure);
    if (d.fonts) d.fonts.ready.then(measure);
    measure(); setAct(0);
    ris.forEach((r, i) => r.addEventListener('click', e => { e.preventDefault(); scrollTo({ top: tops[i] + hs[i] / 2 - innerHeight * (mobile ? .68 : .5), behavior: reduce ? 'auto' : 'smooth' }); }));
    if (fine && !reduce) pointerJobs.push(() => { if (act >= 0 && !mobile) tilts[act].style.setProperty('--ry', ((mx / innerWidth - .25) * 24).toFixed(2) + 'deg'); });
  }

  // ---- app page: icon tilt + document switcher
  const aicon = $('.aicon .tilt');
  if (aicon && fine && !reduce) pointerJobs.push(() => {
    aicon.style.setProperty('--ry', ((mx / innerWidth - .5) * 22).toFixed(2) + 'deg');
    aicon.style.setProperty('--rx', ((.5 - my / innerHeight) * 14).toFixed(2) + 'deg');
  });
  const docs = $('#docs');
  if (docs) {
    let type = docs.dataset.type, lang = docs.dataset.lang;
    const types = $$('[data-t]', docs), langs = $$('[data-l]', docs), panes = $$('.doc', docs);
    const render = (push) => {
      const has = l => panes.some(p => p.dataset.doc === `${type}-${l}`);
      if (!has(lang)) lang = has(docs.dataset.lang) ? docs.dataset.lang : (panes.find(p => p.dataset.doc.startsWith(type + '-')) || {}).dataset?.doc?.split('-')[1];
      panes.forEach(p => p.hidden = p.dataset.doc !== `${type}-${lang}` && p.dataset.doc !== type);
      types.forEach(b => b.setAttribute('aria-selected', b.dataset.t === type));
      langs.forEach(b => { b.setAttribute('aria-selected', b.dataset.l === lang); b.hidden = !has(b.dataset.l); });
      $('.seg.l', docs).hidden = !langs.some(b => !b.hidden) || langs.filter(b => !b.hidden).length < 2;
      if (push) history.replaceState(null, '', '#' + type + (lang && has(lang) ? '-' + lang : ''));
    };
    const body = $('.dbody', docs), dhead = $('.dhead', docs);
    const pick = fn => () => { fn(); render(true); body.scrollTop = 0; };
    types.forEach(b => b.addEventListener('click', pick(() => type = b.dataset.t)));
    langs.forEach(b => b.addEventListener('click', pick(() => lang = b.dataset.l)));
    body.addEventListener('scroll', raf(() => dhead.classList.toggle('sh', body.scrollTop > 4)), { passive: true });
    const fromHash = () => {
      const m = location.hash.match(/^#(privacy|terms)(?:-(\w\w))?$/);
      if (m) { type = m[1]; if (m[2]) lang = m[2]; render(false); const go = () => docs.scrollIntoView({ behavior: 'instant' }); go(); addEventListener('load', go, { once: true }); }
    };
    addEventListener('hashchange', fromHash);
    render(false); fromHash();
  }
})();
