# Deploying the Frontend to Vercel (via GitHub)

This deploys the **React frontend only**. The public site and all three dashboards
work with the built-in South Point demo data. Login and live marks/approvals need a
backend, which Vercel can't host — see the note at the bottom.

---

## Step 1 — Put the frontend on GitHub

Open a terminal in the **frontend** folder:

```powershell
cd C:\Users\Asus\Documents\projects\eduplatform\frontend
git init
git add .
git commit -m "South Point School & College site"
```

Create an empty repo on github.com (no README), then connect and push
(replace the URL with your repo's):

```powershell
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

> Only the `frontend` folder goes up. `node_modules` and `dist` are ignored by
> `.gitignore`, so they won't be committed.

---

## Step 2 — Import into Vercel

1. Go to **https://vercel.com** and sign in with GitHub.
2. Click **Add New… → Project**.
3. Pick your repo and click **Import**.
4. Vercel auto-detects Vite. Confirm these settings (they're the defaults):
   - **Framework Preset:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
   - **Install Command:** `npm install`
5. (Optional) Under **Environment Variables**, you can leave it empty for the
   demo. If you later host a backend, add:
   - Name: `VITE_API_URL`  Value: `https://your-backend-url/api`
6. Click **Deploy**.

After ~1 minute you get a live URL like `https://your-repo.vercel.app`.

---

## Step 3 — Done

Every time you `git push` to `main`, Vercel rebuilds and redeploys automatically.

The `vercel.json` in this folder handles client-side routing, so refreshing on
`/about`, `/chat`, etc. works instead of 404ing.

---

## If you want login & real data to work (backend)

Vercel can't run Django + PostgreSQL. Host the backend separately on a service
that runs Python, e.g.:

- **Render** (render.com) — free tier, good for Django + Postgres
- **Railway** (railway.app)
- **PythonAnywhere** (pythonanywhere.com)

Then, in Vercel → your project → **Settings → Environment Variables**, set
`VITE_API_URL` to your backend's URL (e.g. `https://eduplatform.onrender.com/api`)
and redeploy. Also add your Vercel domain to the backend's
`CORS_ALLOWED_ORIGINS` in `backend/.env`.
