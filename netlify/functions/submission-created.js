// Fires on every Netlify Forms submission. Posts the lead to the
// "Sydney Fitouts leads" Google Sheet through its Apps Script web app.
// Env: LEAD_URL (the /exec URL), LEAD_SECRET (matches SECRET in the script).
exports.handler = async (event) => {
  const url = process.env.LEAD_URL, secret = process.env.LEAD_SECRET;
  if (!url || !secret) return { statusCode: 200, body: 'no LEAD_URL' };
  const p = JSON.parse(event.body).payload || {};
  const d = p.data || {};
  const f = (k) => (d[k] && typeof d[k] === 'object' && d[k].url) ? d[k].url : (d[k] || '');
  const row = {
    secret, date: p.created_at || new Date().toISOString(),
    name: d.name || '', phone: d.phone || '', email: d.email || '', address: d.address || '',
    notes: d.notes || '', estimate: d.calculator || '',
    photo1: f('photo1'), photo2: f('photo2'), photo3: f('photo3'), plan: f('plan'),
    source: 'cityfitouts.com.au'
  };
  try {
    const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(row), redirect: 'follow' });
    return { statusCode: 200, body: 'ok ' + r.status };
  } catch (e) {
    console.error('[lead] sheet write failed', e.message);
    return { statusCode: 200, body: 'failed' };
  }
};
