#!/usr/bin/env python3
"""cityfitouts.com.au - generates every page. Edit copy here, run python3 tools/build.py.
City Fitouts is a BUILDER. No design services are offered or mentioned anywhere on the site."""
import os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://cityfitouts.com.au"
PHONE = "0411 250 058"; PHONE_TEL = "0411250058"
PHONE2 = "0450 084 175"; PHONE2_TEL = "0450084175"
EMAIL = "info@cityfitouts.com.au"
GA = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-9XJ7DRJZG0"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-9XJ7DRJZG0");</script>'
ICON = """<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Cpath d='M1 1h22v22zM25 1h22v22zM25 25h22v22z' fill='%231E2C4F'/%3E%3C/svg%3E">"""
LOGO = """<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M1 1h22v22zM25 1h22v22zM25 25h22v22z" fill="#1E2C4F"/></svg>"""

PAGES = [  # (file, clean url, title, description)
    ("index.html", "/", "City Fitouts - Commercial builders and fitout contractors, Sydney",
     "Commercial fitouts, alterations and refurbishments across Sydney. Office, retail, hospitality, medical and childcare. Check what your fitout will cost, then get a fixed price."),
    ("our-projects.html", "/our-projects", "Our projects - City Fitouts",
     "Recent commercial fitouts and refurbishments by City Fitouts: retail, hospitality and pharmacy projects."),
    ("commercial-fitouts-sydney.html", "/commercial-fitouts-sydney", "Commercial fitouts Sydney - City Fitouts",
     "Office, retail and hospitality fitouts across Sydney, built to a fixed price and a fixed program."),
    ("fitout-cost.html", "/fitout-cost", "What will your fitout cost? - City Fitouts",
     "Enter your floor area, the type of space and the level of finish. Get a Sydney fitout cost range, a program and the approval path in ten seconds."),
    ("about.html", "/about", "About City Fitouts",
     "City Fitouts is a Sydney commercial builder. Fitouts, alterations and refurbishments for tenants, landlords and their architects."),
    ("contact.html", "/contact", "Contact City Fitouts",
     "Talk to City Fitouts about a commercial fitout, alteration or refurbishment in Sydney."),
]

def head(title, desc, url, extra=""):
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{url}">
<meta property="og:type" content="website">
<meta property="og:image" content="{DOMAIN}/images/ricketty-street-mascot.jpg">
{ICON}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="/city.css">
{GA}{extra}
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="brand" href="/">{LOGO}<b>City<br>Fitouts</b></a>
    <nav><a href="/commercial-fitouts-sydney">Fitouts</a><a href="/our-projects">Projects</a><a href="/fitout-cost">Cost Calculator</a><a href="/about">About</a><a href="/contact">Contact</a><a class="cta" href="/contact">Get a fixed price</a></nav>
  </header>
"""

FOOT = f"""
  <footer>
    <div class="fcols">
      <div><b>City Fitouts</b><br>Commercial builders and fitout contractors, Sydney.<br>Fitouts, alterations and refurbishments for tenants, landlords and their architects.</div>
      <div><b>Talk to us</b><br>6 Ossary Street, Mascot NSW 2020<br>Mon - Fri 9am - 5pm, weekends by appointment<br><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="tel:{PHONE2_TEL}">{PHONE2}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      <div><b>Pages</b><br><a href="/commercial-fitouts-sydney">Commercial fitouts</a><br><a href="/office-fitouts-sydney">Office</a> · <a href="/retail-fitouts-sydney">Retail</a> · <a href="/cafe-restaurant-fitouts-sydney">Cafe</a> · <a href="/medical-fitouts-sydney">Medical</a> · <a href="/childcare-fitouts-sydney">Childcare</a><br><a href="/our-projects">Projects</a><br><a href="/fitout-cost">Fitout cost</a><br><a href="/about">About</a><br><a href="/contact">Contact</a></div>
    </div>
    <p class="fine">Cost ranges on this site are a guide only; every job is priced after a walk-through.</p>
  </footer>
</div>
</body></html>
"""

PROJECTS = [
    ("Macpac, Warringah Mall", "Retail", "macpac-warringah-mall.jpg",
     "A full-tenancy outdoor-retail fitout inside a trading centre: display joinery, feature flooring, lighting and services, built to the centre's out-of-hours program and handed over on the opening date."),
    ("KFC, Garbutt", "Hospitality refurbishment", "kfc-garbutt.jpg",
     "A live-trading quick-service restaurant refurbished in stages: kitchen, dining room, counters and the external works, with the store open through most of the program."),
    ("Kareela Community Pharmacy", "Retail", "kareela-pharmacy.jpg",
     "A community pharmacy fitout: dispensary and consulting rooms, retail shelving and counters, new lighting and the hydraulics and electrical to suit a health use."),
]

def projects_html(n=None):
    out = '<div class="projects">'
    for name, kind, img, blurb in PROJECTS[:n]:
        out += f'<figure><img src="/images/{img}" alt="{name}" loading="lazy"><figcaption><span class="kick">{kind}</span><b>{name}</b><p>{blurb}</p></figcaption></figure>'
    return out + "</div>"

CALC = """
  <div class="calc" id="calc">
    <div>
      <div class="q"><label class="h" for="area">1. Floor area (m²)</label><input type="number" id="area" value="150" min="20" max="5000" step="5"></div>
      <div class="q"><label class="h">2. What is the space?</label>
        <div class="opts" id="type">
          <button class="opt on" data-v="office">Office</button>
          <button class="opt" data-v="retail">Retail shop</button>
          <button class="opt" data-v="hospo">Cafe or restaurant</button>
          <button class="opt" data-v="medical">Medical or dental</button>
          <button class="opt" data-v="childcare">Childcare centre</button>
        </div></div>
      <div class="q"><label class="h">3. Level of finish</label>
        <div class="opts" id="grade">
          <button class="opt on" data-v="basic">Basic<small>existing services, paint, carpet, basic joinery</small></button>
          <button class="opt" data-v="mid">Mid<small>new partitions, joinery, lighting, some services</small></button>
          <button class="opt" data-v="premium">Premium<small>feature joinery, new services and mechanical</small></button>
        </div></div>
      <div class="q"><label class="h">4. Does the use change?</label>
        <div class="opts" id="use">
          <button class="opt on" data-v="same">Same use as the last tenant</button>
          <button class="opt" data-v="new">New use (e.g. shop to cafe)</button>
        </div></div>
      <div class="q"><label class="chk"><input type="checkbox" id="heritage"> Heritage-listed building, or in a heritage conservation area (older shopping strips - ask the agent)</label></div>
    </div>
    <aside class="result" id="result">
      <div class="cap">Estimated cost</div>
      <div class="big" id="cost">$180,000 - $270,000</div>
      <div class="sub" id="perm2">$1,200 - $1,800 per m² · <span id="areaOut">150 m²</span></div>
      <div class="row"><span>Construction</span><b id="cCon">-</b></div>
      <div class="row"><span>Design (your architect or designer)</span><b id="cDes">-</b></div>
      <div class="row"><span>Approvals and certification</span><b id="cApp">-</b></div>
      <div class="row"><span>Program on site</span><b id="weeks">4 - 6 weeks</b></div>
      <div class="appr" id="appr"><b>Likely exempt development</b><span>Internal, non-structural work in a commercial building usually needs no council approval under the NSW Codes SEPP. Fire and electrical work still needs certification.</span></div>
      <div class="fine">Ranges based on Sydney design-and-construct pricing, 2026, excluding GST, base-building works, furniture and loose equipment. <span id="splitNote"></span> Every site is different - a fixed price needs a walk-through.</div>
      <p style="margin:16px 0 0"><a class="btn" href="/contact">Get a fixed price for this fitout</a></p>
    </aside>
  </div>
"""

CALC_JS = """
<script>
const RATES={office:{basic:[1200,1800],mid:[1800,2500],premium:[2500,3500]},retail:{basic:[1000,1500],mid:[1500,2200],premium:[2200,3200]},hospo:{basic:[2500,3200],mid:[3200,4000],premium:[4000,5500]},medical:{basic:[2200,2800],mid:[2800,3500],premium:[3500,4500]},childcare:{basic:[2000,2600],mid:[2600,3300],premium:[3300,4200]}};
const WEEKS={office:{basic:[4,6],mid:[6,9],premium:[9,14]},retail:{basic:[3,5],mid:[5,8],premium:[8,12]},hospo:{basic:[6,9],mid:[9,13],premium:[12,18]},medical:{basic:[8,10],mid:[10,14],premium:[14,20]},childcare:{basic:[10,14],mid:[14,18],premium:[18,24]}};
const LABEL={office:'Office',retail:'Retail shop',hospo:'Cafe or restaurant',medical:'Medical or dental',childcare:'Childcare centre',basic:'Basic',mid:'Mid',premium:'Premium',same:'Same use',new:'New use'};
const APPR={
 exempt:['Likely exempt development','Internal, non-structural work in a commercial building usually needs no council approval under the NSW Codes SEPP. Fire and electrical work still needs certification.'],
 cdc:['Complying development (CDC)','A private certifier can approve internal alterations, shopfronts and many changes of use in about 2-4 weeks, without a DA. Food premises also need council registration.'],
 da:['Development application (DA)','Heritage buildings and some changes of use go to council. Allow 8-16 weeks and budget extra for approvals and certification.']};
const S={type:'office',grade:'basic',use:'same'};
const $=id=>document.getElementById(id);
const money=n=>'$'+(n<20000?Math.round(n/500)*500:Math.round(n/1000)*1000).toLocaleString('en-AU');
function calc(){
  let a=Math.max(20,Math.min(5000,+$('area').value||150));
  let [lo,hi]=RATES[S.type][S.grade]; let f=a<80?1.15:1;
  const D={basic:.05,mid:.08,premium:.10}[S.grade];
  const clo=a*lo*f, chi=a*hi*f; const [wlo,whi]=WEEKS[S.type][S.grade];
  const her=$('heritage').checked;
  let k='exempt';
  if(her||(S.type==='medical'&&S.use==='new')||(S.type==='childcare'&&S.use==='new')) k='da';
  else if(S.type==='childcare') k='cdc';
  else if(S.use==='new'||S.type==='hospo'||S.grade==='premium') k='cdc';
  const A={exempt:.015,cdc:.03,da:.06}[k];
  const div=1+D+A;
  const con=[clo/div,chi/div], des=[con[0]*D,con[1]*D], app=[con[0]*A,con[1]*A];
  const rng=r=>money(r[0])+' - '+money(r[1]);
  $('cost').textContent=money(clo)+' - '+money(chi);
  $('perm2').textContent='$'+Math.round(lo*f).toLocaleString('en-AU')+' - $'+Math.round(hi*f).toLocaleString('en-AU')+' per m² · '+a+' m²';
  $('cCon').textContent=rng(con); $('cDes').textContent=rng(des); $('cApp').textContent=rng(app);
  const AN={exempt:'exempt development',cdc:'complying development',da:'a DA'};
  $('splitNote').textContent='Design allowed at '+Math.round(D*100)+'% of construction for a '+LABEL[S.grade].toLowerCase()+' finish (we build from your designer\'s drawings); approvals and certification '+(A*100)+'% for '+AN[k]+'.';
  $('weeks').textContent=wlo+' - '+whi+' weeks';
  $('appr').innerHTML='<b>'+APPR[k][0]+'</b><span>'+APPR[k][1]+'</span>';
  const line=`${a} m2 | ${LABEL[S.type]} | ${LABEL[S.grade]} finish | ${LABEL[S.use]} | heritage: ${her?'yes':'no'} | ${money(clo)}-${money(chi)} (construction ${rng(con)}, design ${rng(des)}, approvals ${rng(app)}) | ${wlo}-${whi} weeks | ${APPR[k][0]}`;
  try{sessionStorage.setItem('cf_calc',line)}catch(e){}
  const cf=$('calcField'); if(cf) cf.value=line;
}
['type','grade','use'].forEach(g=>$(g).addEventListener('click',e=>{const b=e.target.closest('.opt');if(!b)return;[...$(g).children].forEach(x=>x.classList.remove('on'));b.classList.add('on');S[g]=b.dataset.v;calc();}));
$('area').addEventListener('input',calc); $('heritage').addEventListener('change',calc);
const pre=new URLSearchParams(location.search).get('type'); if(pre&&RATES[pre]){S.type=pre;[...$('type').children].forEach(x=>x.classList.toggle('on',x.dataset.v===pre));}
calc();
</script>"""

def quote_form(page):
    return f"""
    <form class="form" name="fitout-quote" method="POST" enctype="multipart/form-data" data-netlify="true" action="/thanks.html">
      <input type="hidden" name="form-name" value="fitout-quote">
      <input type="hidden" name="calculator" id="calcField">
      <input type="hidden" name="page" value="{page}">
      <div class="two"><div><label for="name">Name</label><input id="name" name="name" required></div><div><label for="phone">Phone</label><input id="phone" name="phone" type="tel" required></div></div>
      <label for="email">Email</label><input id="email" name="email" type="email" required>
      <label for="address">Site address or suburb</label><input id="address" name="address" required>
      <label for="ptype">Type of project</label>
      <select id="ptype" name="project_type"><option>Office fitout</option><option>Retail fitout</option><option>Cafe or restaurant fitout</option><option>Medical or dental fitout</option><option>Childcare centre</option><option>Alterations or refurbishment</option><option>Make-good</option><option>Something else</option></select>
      <label for="notes">Tell us about the job (optional)</label><textarea id="notes" name="notes" rows="4"></textarea>
      <label>Photos of the space (optional, up to 3, 8 MB each)</label>
      <div class="two" style="grid-template-columns:1fr 1fr 1fr"><input type="file" name="photo1" accept="image/*"><input type="file" name="photo2" accept="image/*"><input type="file" name="photo3" accept="image/*"></div>
      <label for="plan">Floor plan, lease plan or architect's drawings (optional, PDF or image)</label><input type="file" id="plan" name="plan" accept="image/*,.pdf">
      <p style="margin:16px 0 0"><button class="btn" type="submit">Send me a fixed price</button></p>
    </form>
    <script>try{{var v=sessionStorage.getItem('cf_calc');if(v&&!document.getElementById('calcField').value)document.getElementById('calcField').value=v}}catch(e){{}}</script>"""

APPROACH = """
  <section class="band">
    <h2>The City Fitouts approach</h2>
    <div class="steps">
      <div><span class="num">01</span><h3>Price</h3><p>We walk the site with you and your drawings, measure what is there, and come back with a fixed price and a program. Not an estimate that grows - a number you can sign a lease against.</p></div>
      <div><span class="num">02</span><h3>Build</h3><p>Our own site manager runs the job every day. Licensed trades, a certifier engaged from the start, centre and landlord conditions handled, and weekly progress reports with photos.</p></div>
      <div><span class="num">03</span><h3>Hand over</h3><p>Occupation certificate, fire and electrical certification, as-built drawings and warranties in one folder, on the handover date we agreed at the start.</p></div>
    </div>
  </section>"""

TRUSTED = """
  <section class="band">
    <h2>Trusted by national brands and local operators</h2>
    <p>Retail chains inside trading centres, quick-service restaurants that stay open while we work, pharmacies, medical rooms and offices - delivered for national brands, franchisees and first-time tenants alike.</p>
  </section>"""

def home():
    h = head(*PAGES[0][2:], PAGES[0][1])
    return h + f"""
  <section class="hero split">
    <div>
      <div class="kick">Commercial builders, Sydney</div>
      <h1>Commercial builds and fitouts. Built with care, delivered on the date.</h1>
      <p>City Fitouts builds offices, shops, cafes and restaurants, medical rooms and childcare centres across Sydney. Fixed price, fixed program, one site manager from the first day to handover.</p>
      <p><a class="btn" href="/contact">Get a fixed price</a> &nbsp; <a class="textlink" href="#checker">Check what your fitout will cost &rarr;</a></p>
    </div>
    <div class="heroimg" role="img" aria-label="38-40 Ricketty Street, Mascot" style="background-image:url(/images/ricketty-street-mascot.jpg)"></div>
  </section>

  <section class="band">
    <h2>What we build</h2>
    <div class="spaces">
      <a href="/office-fitouts-sydney"><img src="/images/office-open-plan.jpg" alt="Office fitout" loading="lazy"><div><b>Offices</b><span>Partitions, joinery, services and make-good</span></div></a>
      <a href="/retail-fitouts-sydney"><img src="/images/retail-boutique.jpg" alt="Retail fitout" loading="lazy"><div><b>Retail</b><span>Shopfronts, display joinery, centre fitouts</span></div></a>
      <a href="/cafe-restaurant-fitouts-sydney"><img src="/images/cafe.jpg" alt="Cafe fitout" loading="lazy"><div><b>Cafes and restaurants</b><span>Kitchens, exhaust, grease traps, front of house</span></div></a>
      <a href="/medical-fitouts-sydney"><img src="/images/medical-dental.jpg" alt="Medical fitout" loading="lazy"><div><b>Medical and dental</b><span>Consult rooms, surgeries, specialised services</span></div></a>
      <a href="/childcare-fitouts-sydney"><img src="/images/childcare-preschool.jpg" alt="Childcare fitout" loading="lazy"><div><b>Childcare</b><span>Playrooms, bathrooms, kitchens, outdoor areas</span></div></a>
      <a href="/commercial-fitouts-sydney"><img src="/images/office-lobby.jpg" alt="Refurbishment" loading="lazy"><div><b>Alterations and refurbishments</b><span>Lobbies, amenities, live-trading refurbs</span></div></a>
    </div>
  </section>
  {APPROACH}
  <section class="band">
    <h2>Recent projects</h2>
    {projects_html(3)}
    <p style="margin-top:14px"><a class="textlink" href="/our-projects">All projects &rarr;</a></p>
  </section>

  <section class="band" id="checker">
    <h2>What will your fitout cost?</h2>
    <p>Answer four questions and get a Sydney cost range, a realistic program and the approval path - in ten seconds. No email needed to see the result.</p>
    {CALC}
  </section>
  {TRUSTED}
  <section class="band" id="quote">
    <h2>Get a fixed price</h2>
    <p>Your calculator answers come with the request, so the first call is about your site, not a form. Or ring <a href="tel:{PHONE_TEL}">{PHONE}</a> or <a href="tel:{PHONE2_TEL}">{PHONE2}</a>.</p>
    {quote_form("home")}
  </section>
{FOOT}
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"GeneralContractor","name":"City Fitouts","url":"{DOMAIN}/","telephone":"+61 {PHONE}","email":"{EMAIL}","image":"{DOMAIN}/images/ricketty-street-mascot.jpg","areaServed":"Sydney, NSW","address":{{"@type":"PostalAddress","streetAddress":"6 Ossary Street","addressLocality":"Mascot","addressRegion":"NSW","postalCode":"2020","addressCountry":"AU"}},"description":"Commercial builders and fitout contractors in Sydney: offices, retail, hospitality, medical and childcare fitouts, alterations and refurbishments."}}</script>
{CALC_JS}"""

def projects_page():
    p = PAGES[1]
    return head(p[2], p[3], p[1]) + f"""
  <section class="hero"><div class="kick">Our projects</div><h1>Built, handed over, trading.</h1><p>A selection of recent fitouts and refurbishments. Every one priced fixed, run by our own site manager and handed over with its certificates on the agreed date.</p></section>
  <section class="band">{projects_html()}</section>
  <section class="cta-band"><h2>Have a site in mind?</h2><p>Send the lease plan or your architect's drawings and we will walk it with you.</p><p><a class="btn" href="/contact">Get a fixed price</a></p></section>
{FOOT}"""

def fitouts_page():
    p = PAGES[2]
    return head(p[2], p[3], p[1]) + f"""
  <section class="hero"><div class="kick">Commercial fitouts Sydney</div><h1>Office, retail and hospitality fitouts, built to a fixed price.</h1><p>We build what your architect or shopfitter has drawn, and we build it for the figure we quoted. City Fitouts works for tenants, landlords, franchisees and the architects who look after them.</p></section>
  <section class="band">
    <div class="cols">
      <div class="card"><h3><a href="/office-fitouts-sydney">Office fitouts</a></h3><p>Partitions and glazing, ceilings, lighting and power, meeting rooms, kitchens and breakout areas, joinery and flooring. Mechanical and fire services coordinated with the building. Make-good at lease end.</p></div>
      <div class="card"><h3><a href="/retail-fitouts-sydney">Retail fitouts</a></h3><p>Shopfronts, display and counter joinery, lighting, flooring and signage installation inside shopping centres and on the high street. Centre out-of-hours programs, landlord approvals and shop drawings handled.</p></div>
      <div class="card"><h3><a href="/cafe-restaurant-fitouts-sydney">Cafe and restaurant fitouts</a></h3><p>Commercial kitchens, exhaust and mechanical, grease arrestors and hydraulics, cool rooms, bars and counters, front-of-house finishes. Food-premises compliance built in from day one.</p></div>
      <div class="card"><h3><a href="/medical-fitouts-sydney">Medical and dental</a> / <a href="/childcare-fitouts-sydney">childcare</a></h3><p>Consult rooms, surgeries and treatment rooms with their specialised plumbing and electrical; childcare playrooms, bathrooms and kitchens to the National Quality Framework.</p></div>
    </div>
  </section>
  <section class="band">
    <h2>How we work</h2>
    <div class="steps four">
      <div><span class="num">01</span><h3>Walk-through</h3><p>We meet you on site with the drawings and the lease, measure up and check the base building.</p></div>
      <div><span class="num">02</span><h3>Fixed price</h3><p>A lump-sum price with a program and a clear list of what is in and what is not. No provisional sums hiding the real number.</p></div>
      <div><span class="num">03</span><h3>Build</h3><p>One site manager, licensed trades, weekly photo reports, certifier inspections booked ahead.</p></div>
      <div><span class="num">04</span><h3>Handover</h3><p>Certificates, as-builts, warranties and keys, on the date we agreed.</p></div>
    </div>
  </section>
  <section class="band">
    <h2>Where we work</h2>
    <p>All of Sydney: the CBD and city fringe, North Sydney and the Lower North Shore, the Northern Beaches, the Eastern Suburbs, the Inner West, Parramatta and Western Sydney, the Hills, St George and the Sutherland Shire. Shopping-centre and quick-service-restaurant work is taken interstate for national brands.</p>
  </section>
  <section class="band faq">
    <h2>Questions people ask</h2>
    <details open><summary>Do you do the design as well?</summary><p>No. City Fitouts is a builder. We build from your architect's, designer's or shopfitter's drawings, and we are happy to price early sketches so the design can be adjusted to the budget before it is finished. If you do not have a designer yet we can point you to several we have built for.</p></details>
    <details><summary>How long does a fitout take?</summary><p>A basic office or shop refresh runs four to six weeks on site; a full hospitality or medical fitout twelve to twenty. The <a href="/fitout-cost">cost checker</a> gives a program for your space type and finish.</p></details>
    <details><summary>Do I need council approval?</summary><p>Often not. Internal, non-structural work in a commercial building is usually exempt under the NSW Codes SEPP. A change of use, a new shopfront or a food premises can go through a private certifier as complying development. Heritage buildings and some changes of use need a DA. We engage the certifier and manage the approval as part of the job.</p></details>
    <details><summary>Will the price change?</summary><p>Only if the scope does. The lump sum covers everything on the drawings and in the scope list; anything the base building hides (asbestos, undersized services) is flagged the day we find it, priced, and only done when you say so.</p></details>
  </section>
  <section class="cta-band"><h2>Ready to price your fitout?</h2><p>Check the <a href="/fitout-cost">cost range</a> first, or send us the drawings for a fixed price.</p><p><a class="btn" href="/contact">Get a fixed price</a></p></section>
{FOOT}"""

def cost_page():
    p = PAGES[3]
    return head(p[2], p[3], p[1]) + f"""
  <section class="hero"><div class="kick">Fitout cost checker</div><h1>What will your fitout cost?</h1><p>Office, shop, cafe, restaurant, medical or childcare. Answer four questions and get a Sydney cost range, a realistic program and the approval path - in ten seconds. No email needed to see the result.</p></section>
  {CALC}
  <section class="band" id="rates">
    <h2>Sydney fitout rates, 2026</h2>
    <div class="cols">
      <div>
        <table>
          <tr><th>$ per m²</th><th style="text-align:right">Basic</th><th style="text-align:right">Mid</th><th style="text-align:right">Premium</th></tr>
          <tr><td>Office</td><td class="n">1,200-1,800</td><td class="n">1,800-2,500</td><td class="n">2,500-3,500</td></tr>
          <tr><td>Shop</td><td class="n">1,000-1,500</td><td class="n">1,500-2,200</td><td class="n">2,200-3,200</td></tr>
          <tr><td>Cafe, restaurant</td><td class="n">2,500-3,200</td><td class="n">3,200-4,000</td><td class="n">4,000-5,500</td></tr>
          <tr><td>Medical, dental</td><td class="n">2,200-2,800</td><td class="n">2,800-3,500</td><td class="n">3,500-4,500</td></tr>
          <tr><td>Childcare</td><td class="n">2,000-2,600</td><td class="n">2,600-3,300</td><td class="n">3,300-4,200</td></tr>
        </table>
        <p class="fine">All-in: construction, design and certification, excluding GST. Small tenancies under 80 m² run about 15% higher - fixed costs over less floor.</p>
      </div>
      <div>
        <h3 style="color:var(--navy);margin:0 0 6px">What drives the number</h3>
        <ul style="margin:0;padding-left:18px">
          <li>Services - mechanical, electrical, hydraulics - are the biggest swing.</li>
          <li>A commercial kitchen and exhaust roughly doubles a hospitality budget.</li>
          <li>Joinery is where premium money goes.</li>
          <li>The base-building condition (make-good state) matters.</li>
          <li>Approvals add time more than money.</li>
        </ul>
      </div>
    </div>
  </section>
  <section class="band" id="quote">
    <h2>Turn the range into a fixed price</h2>
    <p>Your answers above come with the request. Or ring <a href="tel:{PHONE_TEL}">{PHONE}</a> or <a href="tel:{PHONE2_TEL}">{PHONE2}</a>.</p>
    {quote_form("fitout-cost")}
  </section>
{FOOT}
{CALC_JS}"""

def about_page():
    p = PAGES[4]
    return head(p[2], p[3], p[1]) + f"""
  <section class="hero"><div class="kick">About</div><h1>Built on collaboration, a clear price and a kept date.</h1><p>City Fitouts is a Sydney commercial builder. We work alongside tenants, landlords, architects and designers to turn a set of drawings into a finished, certified, trading space - without the price moving and without the date slipping.</p></section>
  <section class="band">
    <h2>What we do</h2>
    <div class="cols">
      <div class="card"><h3>Commercial fitouts</h3><p>Offices, retail, hospitality, medical and childcare, from a single tenancy to a centre roll-out.</p></div>
      <div class="card"><h3>Alterations and additions</h3><p>Reworking an existing premises for a new tenant or a new use, including structural work and services upgrades.</p></div>
      <div class="card"><h3>Refurbishments</h3><p>Lobbies, amenities, facades and live-trading refurbs where the business stays open while we work.</p></div>
      <div class="card"><h3>Make-good</h3><p>Returning a tenancy to its lease condition at the end of the term, priced against the lease and the landlord's schedule.</p></div>
    </div>
  </section>
  <section class="band">
    <h2>How we are set up</h2>
    <p>Licensed NSW commercial builder with contract works and public liability insurance. Our own site managers run every job; trades are long-standing subcontractors we have worked with across many fitouts. Architects and designers get a builder who prices their drawings fairly and builds them as drawn; owners and tenants get one point of contact from the first walk-through to the keys.</p>
  </section>
  <section class="cta-band"><h2>Talk to us about your project</h2><p><a class="btn" href="/contact">Get a fixed price</a></p></section>
{FOOT}"""

def contact_page():
    p = PAGES[5]
    return head(p[2], p[3], p[1]) + f"""
  <section class="hero"><div class="kick">Contact</div><h1>Tell us about the job.</h1><p>Send the address, the drawings if you have them and a line about what you need. We will come back within one business day to arrange a walk-through. Or ring <a href="tel:{PHONE_TEL}">{PHONE}</a> or <a href="tel:{PHONE2_TEL}">{PHONE2}</a>, Monday to Friday, 9am to 5pm, or weekends by appointment.</p></section>
  <section class="band">
    <div class="cols" style="grid-template-columns:1.3fr .7fr">
      <div>{quote_form("contact")}</div>
      <div>
        <div class="card"><h3>Phone</h3><p><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="tel:{PHONE2_TEL}">{PHONE2}</a></p></div>
        <div class="card" style="margin-top:12px"><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
        <div class="card" style="margin-top:12px"><h3>Office</h3><p>6 Ossary Street, Mascot NSW 2020</p></div>
        <div class="card" style="margin-top:12px"><h3>Hours</h3><p>Monday to Friday, 9am to 5pm; weekends by appointment</p></div>
        <div class="card" style="margin-top:12px"><h3>Not sure of the budget yet?</h3><p><a href="/fitout-cost">Check what your fitout will cost</a> first - it takes ten seconds and the answers come with your enquiry.</p></div>
      </div>
    </div>
  </section>
{FOOT}"""

THANKS = f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Thanks - City Fitouts</title><meta name="robots" content="noindex"><link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&display=swap" rel="stylesheet"><style>body{{font-family:Jost,system-ui,sans-serif;color:#2B3A49;max-width:640px;margin:80px auto;padding:0 20px;line-height:1.5}}h1{{color:#1E2C4F;font-weight:600}}a{{color:#1E2C4F}}</style>{GA}
</head><body><h1>Thanks - we have it.</h1><p>City Fitouts will come back to you within one business day to arrange a walk-through and a fixed price. If it is urgent, ring <a href="tel:{PHONE_TEL}">{PHONE}</a> or <a href="tel:{PHONE2_TEL}">{PHONE2}</a>.</p><p><a href="/">Back to City Fitouts</a></p></body></html>
"""

CITY_CSS = """/* City Fitouts additions on top of style.css (shared with Sydney Fitouts). Navy only - no amber accent. */
:root{--amber:#1E2C4F}
.kick{color:var(--navy);margin-bottom:22px}
.textlink{color:var(--navy)}
nav a.cta{background:var(--navy)}
.appr{border-left-color:var(--navy)}
.btn.amber{background:var(--navy)}
header.top .brand b{font-size:30px;line-height:27px;display:block;margin-top:-3px}.hero p{margin:0 0 14px}.hero p:last-child{margin-top:26px}header.top .brand svg{width:48px;height:48px;flex:none}
.hero{padding:30px 0 10px}.hero h1{max-width:760px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.steps.four{grid-template-columns:repeat(4,1fr)}
@media(max-width:820px){.steps,.steps.four{grid-template-columns:1fr}}
.steps .num{font-size:13px;letter-spacing:.14em;color:var(--muted);font-weight:600}
.steps h3{margin:4px 0 6px;color:var(--navy);font-size:19px}.steps p{margin:0;font-size:15.5px}
.projects{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
.projects figure{margin:0;background:var(--tint);border-radius:12px;overflow:hidden}
.projects img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block}
.projects figcaption{padding:14px 16px 18px}.projects figcaption b{display:block;color:var(--navy);font-size:18px;margin:2px 0 6px}
.projects figcaption p{margin:0;font-size:15px}.projects .kick{margin:0}
.fcols{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px;margin-bottom:14px}
.fcols a{text-decoration:none}
.form select{width:100%;font:inherit;padding:10px 12px;border:1.5px solid var(--lgrey);border-radius:8px;background:#fff}
@media(max-width:820px){.cols[style]{grid-template-columns:1fr!important}}
"""

def main():
    os.chdir(ROOT)
    out = {"index.html": home(), "our-projects.html": projects_page(), "commercial-fitouts-sydney.html": fitouts_page(),
           "fitout-cost.html": cost_page(), "about.html": about_page(), "contact.html": contact_page(), "thanks.html": THANKS,
           "city.css": CITY_CSS}
    for f, s in out.items():
        open(f, "w").write(s)
    lines = ["/netlify/*  /404.html  404", "/tools/*  /404.html  404", "", "# .html twins retired", "/index.html  /  301!"]
    lines += [f"/{f}  {u}  301!" for f, u, _, _ in PAGES[1:]]
    lines += ["", "/thanks  /thanks.html  200"]
    lines += [f"{u}  /{f}  200" for f, u, _, _ in PAGES[1:]]
    open("_redirects", "w").write("\n".join(lines) + "\n")
    today = datetime.date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{today}</lastmod></url>\n" for _, u, _, _ in PAGES) + "</urlset>\n"
    open("sitemap.xml", "w").write(sm)
    open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /thanks.html\nSitemap: {DOMAIN}/sitemap.xml\n")
    # guard: a builder-only site
    for f, s in out.items():
        for w in ("design &", "Design &", "designer-led", "design and construct", "Design and Construct", "Republic", "Trevor"):
            assert w not in s, (f, w)
    print("built", ", ".join(out))

# ---------------------------------------------------------------- space pages (SEO)
SPACES = [
 dict(slug="office-fitouts-sydney", key="office", name="Office fitouts", h1="Office fitouts, Sydney", img="office-breakout.jpg",
  title="Office fitouts Sydney - fixed price commercial builder | City Fitouts",
  desc="Office fitout builders in Sydney. Partitions, glazing, ceilings, joinery, services and make-good, built to a fixed price and program from your designer's drawings.",
  lede="From a 100 m2 suite to a whole floor: City Fitouts builds office fitouts across Sydney for tenants, landlords and the architects and designers who draw them. Fixed price, fixed program, one site manager.",
  scope=["Partitions and glazed offices, meeting rooms and boardrooms","Ceilings, acoustic treatment, lighting and power","Reception and kitchen joinery, breakout and collaboration areas","Mechanical, fire and data coordinated with the base building","Flooring, painting and feature finishes","Make-good at the end of the lease"],
  program="A basic refresh runs four to six weeks on site; a full new-partition fitout with services nine to fourteen. Out-of-hours work in occupied buildings is priced in, not added later.",
  approvals="Most internal office work is exempt development under the NSW Codes SEPP. A new use, a mezzanine or work in a heritage building goes to a private certifier as complying development or to council. We engage the certifier and run the approval as part of the job.",
  faqs=[("Do you work in occupied buildings?","Yes. Most office fitouts happen while the rest of the building trades. We work to the building manager's rules - after-hours noisy work, protected lifts and lobbies, dust control - and price it from the start."),
        ("Can you price before the design is finished?","Yes, and it is the best time. We price your designer's sketch set so the design can be trimmed to the budget before the drawings are complete."),
        ("Do you do make-good?","Yes. We price the make-good against the lease and the landlord's schedule, so the tenant hands back exactly what is required and no more.")]),
 dict(slug="retail-fitouts-sydney", key="retail", name="Retail fitouts", h1="Retail and shop fitouts, Sydney", img="eyewear.jpg",
  title="Retail fitouts Sydney - shopfitting builder for shopping centres and high street | City Fitouts",
  desc="Retail and shop fitout builders in Sydney. Shopfronts, display joinery, lighting and signage, built inside shopping centres and on the high street to the centre's program.",
  lede="We build shops. Shopfronts, display and counter joinery, lighting, flooring and signage installation, inside Westfield, Stockland and Scentre centres and on the high street, for national brands and first-time retailers alike.",
  scope=["Shopfronts, glazing and roller shutters","Display, counter and point-of-sale joinery","Lighting layouts, track and feature lighting","Flooring, wall finishes and fitting rooms","Signage installation and shop drawings","Centre out-of-hours program, landlord approvals and defects"],
  program="A refresh of an existing shop runs three to five weeks; a new-tenancy fitout with services eight to twelve. Centre fitout guides, hoarding and night work are built into the program.",
  approvals="Inside a shopping centre the landlord's tenancy coordinator approves the design and the centre's own rules apply. A new shopfront on the street or a change of use can need complying development through a private certifier; we handle it.",
  faqs=[("Have you worked in the major centres?","Yes - Macpac at Warringah Mall and Kareela Community Pharmacy are both centre fitouts, built on the centre's out-of-hours program and handed over for the opening date."),
        ("Do you build from the brand's standard drawings?","Yes. National brands send a standard fitout package; we price it against the actual tenancy and build it to the brand's specification."),
        ("Can you do a roll-out?","Yes. Several tenancies on one program with the same team and the same pricing basis.")]),
 dict(slug="cafe-restaurant-fitouts-sydney", key="hospo", name="Cafe and restaurant fitouts", h1="Cafe and restaurant fitouts, Sydney", img="restaurant.jpg",
  title="Cafe and restaurant fitouts Sydney - hospitality builder | City Fitouts",
  desc="Cafe, restaurant and quick-service fitout builders in Sydney. Commercial kitchens, exhaust, grease traps, bars and front of house, built to a fixed price with food-premises compliance from day one.",
  lede="Hospitality is the hardest fitout to get right: the kitchen, the exhaust, the grease arrestor and the hydraulics all have to pass before a single coffee is sold. City Fitouts builds cafes, restaurants and quick-service outlets with those approvals designed in from the start.",
  scope=["Commercial kitchens, cool rooms and dry stores","Mechanical exhaust and make-up air","Grease arrestors, hydraulics and gas","Bars, counters and servery joinery","Front-of-house finishes, seating and lighting","Live-trading refurbishments in stages"],
  program="A cafe in an existing food tenancy runs six to nine weeks; a new restaurant with a full kitchen twelve to eighteen. Staged refurbishments keep the venue trading, as at KFC Garbutt.",
  approvals="A food premises needs council registration and usually complying development through a private certifier for the change of use, exhaust and grease arrestor. Sydney Water trade-waste approval is separate. We run all of it.",
  faqs=[("Can you keep us trading during a refurb?","Yes. We stage the work - kitchen, then dining, then counters - so the venue stays open for most of the program. KFC Garbutt was refurbished that way."),
        ("Who designs the kitchen?","Your kitchen designer or equipment supplier. We build to their layout and coordinate the services to it."),
        ("Why does hospitality cost more per square metre?","The kitchen, exhaust and hydraulics roughly double the budget of an office of the same size. The cost checker shows the range for your floor area.")]),
 dict(slug="medical-fitouts-sydney", key="medical", name="Medical and dental fitouts", h1="Medical and dental fitouts, Sydney", img="medical-consult.jpg",
  title="Medical and dental fitouts Sydney - healthcare builder | City Fitouts",
  desc="Medical, dental and allied-health fitout builders in Sydney. Consult rooms, surgeries, treatment rooms, specialised plumbing and electrical, infection control, built to a fixed price.",
  lede="Medical rooms carry requirements an office never sees: infection-control surfaces, medical gases, dental plumbing and suction, lead lining for imaging, accessibility to every room. City Fitouts builds GP, dental, specialist and allied-health practices with those details costed in.",
  scope=["Consult, treatment and procedure rooms","Dental surgeries with suction, compressed air and plumbing to the chair","Reception, waiting and accessible amenities","Infection-control finishes, hand-wash stations and sterilisation rooms","Specialised electrical, data and mechanical","Imaging rooms with shielding where required"],
  program="A medical suite in an existing health tenancy runs eight to ten weeks; a new practice with dental chairs or imaging fourteen to twenty.",
  approvals="A health use in a tenancy that was not one before is a change of use and usually needs complying development or a DA. Accessibility (AS 1428) applies to the whole fitout. We engage the certifier and the access consultant early.",
  faqs=[("Do you coordinate with the dental equipment supplier?","Yes. The chair, suction and compressor suppliers give us their service points and we build the floor and wall penetrations to them before the slab is closed."),
        ("Can a shop become a medical centre?","Often, but it is a change of use with parking, accessibility and sometimes acoustic requirements. We check the tenancy before you sign the lease."),
        ("What about the base-building services?","Medical rooms draw more power and air than offices. We check the switchboard and mechanical capacity at the walk-through, so the price includes any upgrade.")]),
 dict(slug="childcare-fitouts-sydney", key="childcare", name="Childcare centre fitouts", h1="Childcare centre fitouts, Sydney", img="childcare-toddlers.jpg",
  title="Childcare centre fitouts Sydney - early-learning builder | City Fitouts",
  desc="Childcare and early-learning centre builders in Sydney. Playrooms, bathrooms, kitchens, cot rooms and outdoor play areas built to the National Quality Framework, to a fixed price.",
  lede="A childcare centre is built around the regulations: unencumbered space per child, a bathroom for every playroom group, a cot room, a kitchen, a laundry and the outdoor area. City Fitouts builds new centres and converts existing buildings for operators and developers.",
  scope=["Playrooms, cot rooms and sleep rooms","Children's bathrooms and nappy-change areas for each group","Commercial kitchen and laundry","Staff rooms, office and parent reception","Outdoor play areas, soft-fall and shade","Fencing, access control and fire services"],
  program="Converting an existing building runs ten to fourteen weeks; a full new centre fitout eighteen to twenty-four. The program is built around the operator's licensing inspection date.",
  approvals="A new centre always needs a DA, and the Education and Care Services National Regulations set the spaces. The provider approval and service approval from the NSW regulator follow the build. We work to the operator's consultant and the approved plans.",
  faqs=[("Can you convert a house or a shop into a centre?","Sometimes. It needs a DA and the right zoning, parking and outdoor area. We walk the building with you before you commit."),
        ("Do you build the outdoor area?","Yes - soft-fall, shade structures, fencing, landscaping and the covered verandah are part of the job."),
        ("How much does a childcare fitout cost?","Roughly $2,000-4,200 per m2 of indoor area in 2026, before the outdoor area. The cost checker gives the range for your floor area.")]),
]

def space_page(sp):
    url = "/" + sp["slug"]
    scope = "".join(f"<li>{x}</li>" for x in sp["scope"])
    faqs = "".join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(sp["faqs"]))
    others = " · ".join(f'<a href="/{o["slug"]}">{o["name"]}</a>' for o in SPACES if o is not sp)
    import json
    ld = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in sp["faqs"]]})
    ld2 = json.dumps({"@context":"https://schema.org","@type":"Service","serviceType":sp["name"],"provider":{"@type":"GeneralContractor","name":"City Fitouts","telephone":"+61 "+PHONE,"url":DOMAIN+"/"},"areaServed":"Sydney, NSW","url":DOMAIN+url})
    return head(sp["title"], sp["desc"], url) + f"""
  <section class="hero split">
    <div><div class="kick">{sp["name"]}</div><h1>{sp["h1"]}</h1><p>{sp["lede"]}</p>
    <p><a class="btn" href="/contact">Get a fixed price</a> &nbsp; <a class="textlink" href="/fitout-cost?type={sp["key"]}">Check the cost range &rarr;</a></p></div>
    <div class="heroimg" role="img" aria-label="{sp["name"]}" style="background-image:url(/images/{sp["img"]})"></div>
  </section>
  <section class="band"><div class="cols">
    <div><h2>What we build</h2><ul class="tick">{scope}</ul></div>
    <div><h2>Program</h2><p>{sp["program"]}</p><h2>Approvals</h2><p>{sp["approvals"]}</p></div>
  </div></section>
  {APPROACH}
  <section class="band faq"><h2>Questions people ask</h2>{faqs}</section>
  <section class="cta-band"><h2>Price your {sp["name"].lower()[:-1] if sp["name"].endswith("s") else sp["name"].lower()}</h2><p>Check the <a href="/fitout-cost?type={sp["key"]}">cost range</a> in ten seconds, or send us the drawings for a fixed price.</p><p><a class="btn" href="/contact">Get a fixed price</a></p></section>
  <p class="fine">Other spaces: {others}</p>
{FOOT}
<script type="application/ld+json">{ld}</script>
<script type="application/ld+json">{ld2}</script>"""

for sp in SPACES:
    PAGES.append((sp["slug"] + ".html", "/" + sp["slug"], sp["title"], sp["desc"]))

_main = main
def main():
    # extra outputs, then the standard build (which writes _redirects/sitemap from PAGES)
    os.chdir(ROOT)
    for sp in SPACES:
        open(sp["slug"] + ".html", "w").write(space_page(sp))
    _main()

if __name__ == "__main__":
    main()
