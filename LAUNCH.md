# Debt Freedom Planner: Launch Plan

**Product:** `product/Debt-Freedom-Planner.xlsx`, a budget, debt payoff (snowball/avalanche) and savings-goals spreadsheet.
**Price:** $12 (launch at $9 for the first ~20 sales to collect reviews).
**Rebuild:** `python scripts/build_planner.py`

## Why marketplaces first
You have no audience, so sell where buyers already search. Etsy and Gumroad Discover bring their own traffic. The landing page (`site/index.html`) is for traffic you send yourself, such as Reddit, Pinterest and TikTok.

## Step 1: Etsy (highest traffic for digital planners)
1. Open an Etsy shop. There's a $0.20 listing fee, and Etsy takes 6.5% of each sale plus payment processing.
2. Create a **digital** listing and upload the .xlsx file.
3. Make 5 to 10 listing images. Screenshot each tab in Excel or Google Sheets, then add a big headline image ("See your debt-free date").
4. Paste in the title, tags and description below.

**Title** (140 characters max):
`Debt Payoff Planner Spreadsheet, Snowball & Avalanche Debt Tracker, Monthly Budget Template, Savings Goal Tracker, Excel & Google Sheets`

**13 tags:** debt payoff planner, debt snowball, debt avalanche, budget spreadsheet, google sheets budget, excel budget template, debt tracker, savings tracker, monthly budget, financial planner, debt free, budget template, paycheck budget

**Description:**
> See the exact month you'll be debt-free.
>
> Enter your debts once and the planner builds a month-by-month payoff plan. Choose Snowball (smallest balance first) or Avalanche (highest interest first) and watch your debt-free date and total interest update instantly.
>
> INCLUDED
> • Debt Payoff: up to 8 debts, automatic payment rollover, payoff date per debt, total interest, balance chart
> • Monthly Budget: planned vs. actual, leftover cash, savings rate
> • Savings Goals: progress bars and target dates
> • Start Here guide
>
> Works in Microsoft Excel, Google Sheets and LibreOffice. Instant download. This is a digital file; nothing will be shipped.

## Step 2: Gumroad (free, 10% fee). Same copy, and link the landing page to it.
Or use a **Stripe Payment Link**: create a $12 product in the Stripe dashboard and set the after-payment confirmation to redirect to a download link (for example, a Google Drive file shared as "anyone with link").
Then replace `https://buy.stripe.com/REPLACE_ME` in `site/index.html` (it appears twice).

## Step 3: Host the landing page for free
GitHub Pages (Settings → Pages → deploy from `/site`) or drag the `site/` folder onto Netlify Drop.

## Step 4: Traffic (free, about 30 to 60 minutes a day)
- **Pinterest:** 3 pins a day with a tall image ("I'll be debt-free in May 2030") linking to the Etsy listing. Finance pins keep circulating for months.
- **Reddit:** r/personalfinance and r/povertyfinance ban self-promotion. Answer questions honestly and offer the *free* calculator logic. Only post in subs that allow it, such as r/sideproject.
- **TikTok/Shorts:** screen-record changing the extra payment from $0 to $200 while the debt-free date jumps years earlier. That before-and-after is the hook.

## Realistic expectations
Most new Etsy shops sell nothing in their first few weeks. The shops that succeed usually have **several** listings. Once this one gets its first sale, run `scripts/build_planner.py` variants such as a wedding budget, a sinking-funds tracker, a freelancer tax planner, or a bundle at $19.
