# A Long-Term Investor's Comprehensive Guide to Federal Reserve QE & QT

**Disclaimer:** This guide is meant to educate—helping you separate signal from sensationalism—not to prescribe trades. Treat it with the same rigor you'd give any serious research; skim it half-heartedly and you’re more likely to misfire than profit.

![Fed's Sponge](images/20250519-00-title.png)

---

### 1 · What are QE and QT?

**Quantitative Easing (QE)** and **Quantitative Tightening (QT)** are balance-sheet tools the Fed uses **after** the policy rate is already at (or near) its chosen level.

* **QE:** large-scale asset purchases that **add** reserves to the banking system and **pull duration risk out of private portfolios**.
* **QT:** the mirror image—**allowing** assets to mature (or occasionally selling them) so the balance sheet **shrinks**, draining reserves and returning duration risk to the market.

They are not meant to micro-steer GDP quarter-to-quarter.  Their stated purpose is to **affect the price and availability of long-dated credit** when the fed-funds rate is already pinned.  (Think of QE/QT as the rudder, while the short-rate is the throttle.)

#### What "duration" means—and why the Fed's QE/QT shifts it around

**Duration (bond-market definition)**
*Duration* is a weighted-average measure of when you'll receive a bond's cash-flows. In practice, investors use **modified duration**—it tells you roughly how much a bond's **price will change for a 1-percentage-point move in yield**:

$$
\text{Price change (\%)} \approx -\,\text{Duration}\times\Delta\text{Yield}
$$

* A **30-year Treasury** has a duration of ~19 years, so if its yield jumps 1 %, its price falls about 19 %.
* A **2-year Treasury** has a duration of ~1.9 years—far less rate sensitivity.

Hence **"duration risk"** is simply the potential portfolio hit you take if rates move the "wrong" way.

#### How "Duration" Applies to Stocks

In equity-market slang, **"duration" travels beyond bonds to describe how far into the future a company's value is concentrated.**  *Long-duration growth stocks*—think early-stage biotech, unprofitable AI startups, or any firm whose cash-flow ramp is projected many years out—resemble 30-year bonds: most of their economic payoff lies in the distant future, so even a small rise in the discount rate (via real yields or equity risk-premium) can lop a hefty chunk off present value.  By contrast, *short-duration equities*—mature dividend payers, utilities, cash-rich cyclicals—throw off cash almost immediately, making their prices less sensitive to rate shifts.  When quantitative easing drives long rates lower, equity investors often migrate toward these long-duration growth names because the mathematical penalty for waiting on future earnings shrinks; during quantitative tightening or real-yield spikes, the same stocks can unwind violently as the higher discount rate "compresses" those far-off cash flows.

#### Quick Intuition: How the Fed's Policy Rate Shapes Stock Valuations

$$
\text{Present Value (PV)} \;=\;\sum_{t=1}^{N}\frac{CF_{t}}{(1+r)^{t}}
$$

* **$CF_{t}$**  = the cash flow you expect in year $t$
* **$r$**  = the **discount rate** (your required return, which embeds the risk-free rate, an inflation premium, and an equity-risk premium)
* **$N$**  = the forecast horizon; anything beyond $N$ is usually rolled into a **terminal value** that's discounted the same way

---

#### Why the discount rate sits in the **denominator**

Each cash-flow term is **divided by $(1+r)^{t}$**.

* When **$r$ rises**, the denominator grows, so every future dollar gets **shrunk more aggressively** before it reaches today's valuation tally.
* The farther out the cash flow (higher $t$), the louder that shrink-factor echoes—this is exactly why "long-duration" growth stocks crater when real yields jump.

---

#### Bottom-line intuition

* **Rate hike ⇒ bigger denominator ⇒ lower PV.**
* To *avoid* a lower valuation, the company's expected **cash flows must grow faster** than the discount-rate increase.
  *Example:* If the discount rate moves from 8 % to 10 % (a +2 pp jump), a 10-year stream of level cash flows loses roughly 15 % of its PV. The firm would need to lift its cash-flow path by about the same 15 %—immediately and permanently—just to stay value-neutral.
* Because most businesses can't conjure that kind of instant, sustained growth, higher rates almost always **translate into lower equity valuations**, especially for firms whose payoffs sit far in the future.

**Empirical note:** This isn't just a textbook exercise—pricing data back it up. Sell-side analysts ground their target prices in DCF models whose outputs swing with the discount rate. When real yields or risk premia rise, those spreadsheets get rerun, fair-value estimates step down, and the analyst consensus drifts lower. That new reference point filters into screens, portfolio models, and financial headlines, exerting sustained downward pressure on the share price even before the company's fundamentals have a chance to change.

---

### 2 · How QE and QT move that risk around

| Program                          | What the Fed buys or lets run off                                                                                           | Effect on the private sector's duration load                                                                                                                                    |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **QE (Quantitative Easing)**     | Fed **buys long-dated Treasuries and agency MBS**. It swaps investors' high-duration bonds for overnight-rate bank reserves. | **Pulls duration risk *out* of private portfolios.** Pension funds, insurers, asset managers hold less rate-sensitive paper, so their aggregate exposure to a rate spike falls. |
| **QT (Quantitative Tightening)** | Fed **allows those long bonds to mature** (or rarely, sells them). The Treasury must re-issue the debt to the public.       | **Pushes duration risk *back* to private holders.** Market participants now absorb more long-dated supply; their portfolios become more sensitive to future rate moves.         |

Think of the Fed as a giant sponge it can **soak up** or **wring out** the economy's exposure to long-term interest-rate swings. QE soaks up duration, QT wrings it out.

---

#### Why long-term investors should care—briefly

* **Valuations:** Lower public-market duration (post-QE) tends to compress long-term yields, boosting discounted-cash-flow values for equities and real assets.
* **Rebalancing flows:** When QT returns duration risk to the market, bond managers often shed some long Treasuries to stay within risk limits—knock-on demand shifts can ripple into credit spreads and even equity volatility.
* **Hedging decisions:** Pension funds use duration matching; knowing whether the Fed is adding or subtracting supply of long bonds helps them time liability-hedge trades.

So "duration" isn't a buzzword—it's the mechanical link between the Fed's balance-sheet actions and the rate sensitivity that ultimately shows up in asset prices.


---

### 3 · The Fed's balance-sheet plumbing—an investor-friendly map

| **Assets**                        | How they enter/exit                                        | **Liabilities**             | Why investors care                        |
| --------------------------------- | ---------------------------------------------------------- | --------------------------- | ----------------------------------------- |
| Treasuries & **Agency-MBS**        | **QE buys** (open-market operations) ↔ **QT run-off caps** | **Bank reserves**           | Drives liquidity & money-market rates     |
| Discount-window & emergency loans | Crisis lending                                             | **Currency in circulation** | Slow, secular growth—not policy-sensitive |
| **Repo & reverse-repo (ON-RRP)**  | Fine-tunes overnight rates                                 | **TGA (Treasury's cash)**   | Big swings change reserve supply          |

During QE the **asset side balloons**; during QT it deflates.  On the liability side, **bank-reserve balances absorb almost the entire shock**; currency and the Treasury's checking account follow their own paths.  Understanding that see-saw is key: reserves are the "buffer capital" of the system.

**📌 Sidebar · How the Fed's Balance Sheet Works**

| Side                                          | Main items                                                                                                                                                                                                          | One-line role                                                                                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Assets** (what the Fed *owns*)              | **• U.S. Treasuries**  <br>• Agency mortgage-backed securities  <br>• Short-term loans & repos to banks/markets  <br>• A bit of gold & foreign currency                                                             | Securities the Fed buys (QE) **add** to this column; letting them mature (QT) **subtracts** from it.                                                     |
| **Liabilities** (what the Fed *owes/creates*) | **• Bank reserves** (deposits commercial banks keep at the Fed)  <br>• Paper currency in your wallet  <br>• Overnight reverse-repo balances (money-market funds' deposits)  <br>• Treasury's checking account (TGA) | Every \$1 increase on the asset side is matched by a \$1 rise here—usually as **bank reserves**. Cut the asset side and reserves shrink the same amount. |

**Core idea:** the Fed can't grow or shrink one column without the other.

* **QE:** buys a bond → *Assets ↑* and *Bank-reserve liabilities ↑* → more system liquidity.
* **QT:** lets a bond roll off → *Assets ↓* and *Bank-reserve liabilities ↓* → liquidity drains.

Think of assets as the Fed's **portfolio** and liabilities as the **money it credits to pay for that portfolio**. The two always move together, dollar-for-dollar.

---

#### One-picture mental model: **the Fed's sponge**

* **The sponge** = the stock of **bank reserves** (the liquidity commercial banks hold at the Fed).
* **Water in the sponge** = dollars those banks can deploy into money markets, lending, or securities.

| Phase                             | What the Fed does                                               | What happens to the **sponge (reserves)**           | What you see in markets                                                                            |
| --------------------------------- | --------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **QE ("fill the sponge")**        | Buys Treasuries / agency MBS → its **assets rise**               | The new reserves **swell the sponge**               | Banks are flush, short-term rates sink, investors shift into riskier assets.                       |
| **QT ("let the sponge deflate")** | Lets bonds mature (or occasionally sells) → its **assets fall** | Reserves **shrink** as the Fed debits bank accounts | Cash cushions thin out, long bonds resurface on dealer balance sheets, funding rates drift higher. |

**Why this isn't straight "money-printing"**
QE creates reserves that stay inside the banking system; they're not cash in household pockets. But larger reserve balances free up bank balance-sheet capacity, which **ripples** into broader credit and asset prices. QT reverses that process by draining reserves and tightening financial conditions.

**Run-off caps in plain English**
A "run-off cap" is just a **speed limit** on QT. Each month the Fed lets up to the cap's worth of Treasuries/MBS mature **without** reinvesting; anything above the cap is rolled over. The lower the cap, the **slower** the sponge deflates, so liquidity drains more gently instead of all at once.

**Follow the money:**

* **Sponge swells (QE)** → liquidity flows **out** to the market.
* **Sponge shrinks (QT)** → liquidity flows **back** into the Fed.
  That's the tide—you don't need to track every droplet.

---

### 4 · QT mechanics—and why 2025's version is gentler than 2017-19

| Cycle       | How runoff was handled                                           | Treasury cap                              | MBS cap             | First sign of stress                                                   |
| ----------- | ---------------------------------------------------------------- | ----------------------------------------- | ------------------- | ---------------------------------------------------------------------- |
| **2017-19** | "Autopilot" caps ratcheted higher each quarter                   | \$30 bn/mo                                | \$20 bn/mo          | Sept-2019 repo squeeze (reserve scarcity)                              |
| **2022-25** | Caps fixed from the start; **twice lowered** to protect reserves | \$60 bn → \$25 bn → **\$5 bn** (Apr 2025) | \$35 bn (unchanged) | None yet, but the Fed flags repo market's rising sensitivity to supply |

**Key takeaway (plain-speak):**
Since May 2025 the Fed is still in QT, just **sipping instead of gulping**. Anything over \$5 billion of maturing Treasuries gets rolled over, but up to \$5 billion drops off the books each month. When that slice of **assets disappears, an equal slice of liabilities—bank reserves—vanishes too.**

→ **Balance sheet smaller ➜ reserves smaller ➜ system liquidity lower.**
It's still a drain, only a gentle one.


---

### 5 · Chronology of the modern QE/QT era

| Date                    | Program           | Balance-sheet change                                                 | Macro backdrop                              |
| ----------------------- | ----------------- | -------------------------------------------------------------------- | ------------------------------------------- |
| **Nov 2008 – Jun 2010** | QE1               | +\$1.7 tn                                                            | GFC rescue                                  |
| **Nov 2010 – Jun 2011** | QE2               | +\$600 bn                                                            | Post-crisis deflation scare                 |
| **Sep 2011 – Dec 2012** | "Operation Twist" | Duration-neutral (bought long, sold short)                           | Flatten long yields                         |
| **Sep 2012 – Oct 2014** | QE3               | +\$1.6 tn                                                            | Labor-market healing                        |
| **Oct 2017 – Sep 2019** | QT-I              | –\$650 bn                                                            | Rate-hike cycle; ended after repo stress    |
| **Mar 2020 – Mar 2022** | Pandemic QE       | +\$4.6 tn                                                            | COVID shock                                 |
| **Jun 2022 – present**  | QT-II             | –\$2.2 tn so far; pace now **\$40 bn/mo** (\$5 bn Tsy + \$35 bn MBS) | Inflation fight; reserve-cushion management |

(Balance-sheet numbers are rounded face-value moves; latest H.4.1 puts Treasuries at **\$4.21 tn** as of May 15 2025.)

---

### 6 · Transmission channels that actually reach a long-term portfolio

| Channel                               | Why it matters                                                       | Metrics to watch                                                  |
| ------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Term-premium & real-yield** effects | Determines DCF discount rates and equity risk premium                | 10-yr **TIPS** real yield; ACM term premium |
| **Liquidity & funding stress**        | Sharp spikes can force forced-selling across assets                  | SOFR-OIS spread; GC repo vs. ON-RRP uptake                        |
| **Signalling / expectations**         | QE can reinforce "lower for longer"-rate guidance                    | 2-yr Treasury; fed-funds futures strip                            |
| **Portfolio-balance**                 | Relative scarcity of safe collateral lifts valuations of risk assets | Equity forward P/E vs. 10-yr real                                 |

Long-run investors seldom need minute-data, but **sustained 50 bp moves** in the 10-yr real rate or a **sudden kink** in the 2-yr usually flag a genuine regime shift.

* **TIPS – Treasury Inflation-Protected Securities**
  *U.S. bonds whose principal rises with CPI, giving holders built-in inflation insurance.*

* **ACM – Adrian-Crump-Moench term-premium model**
  *NY Fed model that isolates the extra yield investors demand for holding long-dated Treasuries.*

* **SOFR – Secured Overnight Financing Rate**
  *Benchmark cost of overnight, Treasury-backed loans—now the core "risk-free" rate for USD markets.*

* **OIS – Overnight Index Swap**
  *Swap that exchanges a fixed rate for the compounded overnight policy rate, revealing forward rate expectations.*

* **GC repo – General-Collateral repurchase agreement**
  *Ultra-liquid overnight loan where any standard Treasury serves as collateral at the lowest repo rate.*

* **ON-RRP – Overnight Reverse-Repurchase Facility**
  *Fed window letting money-market funds park cash overnight for Treasuries, anchoring the rate floor.*

---

### 7 · A genuinely *do-able* check-list (think traffic-lights, not rocket science)

| When?                                                                                 | Look at just **one screen**                                                                                                            | What to ask                                                                        | What it means                                                                                                                                                                                                                 | Typical action for a long-term investor                                                                                                         |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Every Thursday after 4:30 p.m. ET**<br>(Fed posts the *H.4.1* balance-sheet update) | H.4.1 → "Securities held outright – Treasury"                                                                                          | ▸ Still drifting **down**?<br>▸ Flat for **8+ weeks**?                             | **Down** = QT continues (liquidity slowly draining).<br>**Flat 8 weeks** = QT is on pause; balance sheet no longer tightening.                                                                                                | *Down:* stay the course.<br>*Flat 8 weeks:* review risk exposure—cheap money may cycle back sooner.                                             |
| **Month-end (pick any date you'll remember)**                                         | Pull three numbers from FRED or TradingView: <br>1. **2-yr Treasury yield**<br>2. **10-yr TIPS real yield**<br>3. **ACM term premium** | "Did any jump or drop by **½ percentage point (50 bp)** or more since last month?" | A 50 bp swing is a rare, regime-shift size move. <br>• 2-yr ↑ big → market pricing tighter policy.<br>• Real yield ↑ big → higher discount rate (pressure on P/Es).<br>• Term prem ↑ big → investors demanding more risk pay. | If one moves ≥ 50 bp, run a quick valuation sanity check (earnings yield vs. real yield). Otherwise relax.                                      |
| **Eight times a year (FOMC day)**                                                     | Read just two paragraphs: <br>• Balance-sheet sentence in the statement<br>• First audience question on QT in Powell's presser         | "Did they change the runoff cap or hint at *stopping* QT?"                         | Only explicit cap changes or a QT-stop signal warrant attention; wording tweaks like "balanced risks" are noise.                                                                                                              | Cap smaller or QT stop signaled? Expect liquidity tail-wind; consider terming up bond duration or easing hedges. No change? Ignore the chatter. |

#### How to run this with *almost zero effort*

1. **Bookmark** two pages:
   • Fed *H.4.1* release (updates Thurs.)
   • A FRED "dashboard" with the three rate series.
2. **Set a calendar alert**: "Thu 16:30 H.4.1 scan"; "Last business day – rate dashboard"; "FOMC day – 10-min read."
3. Use a **traffic-light** note in your journal:
   *Green* = nothing tripped.  *Yellow* = one 50 bp move—run a quick calc.  *Red* = QT paused or reversed—revisit allocations.

If the lights stay green, you can safely ignore week-to-week Fed chatter and keep your focus on fundamentals.

---

### 8 · Practical portfolio implications (2025 vantage-point)

| Asset class                          | QE phase tends to…                           | QT phase tends to…                           | 2025-specific nuance                                                                                                             |
| ------------------------------------ | -------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Investment-grade bonds**           | Compress spreads; duration rally             | Lift real yields; flatter curve              | Slowing QT **tempers** the upward pressure on duration but doesn't reverse it.                                                   |
| **Equities**                         | Lift P/Es via lower discount rate            | Pressure P/Es; favors earning-stable sectors | 10-yr TIPS at \~1.5 % keeps multiples in check even after QT slows.                                                              |
| **Real assets (gold, REITs, infra)** | Benefit from liquidity + reflation narrative | Mixed—depends on real-rate direction         | Gold rallied in early-2025 partly on the \$5 bn cap headline; the driver is *real-yield drift*, not the balance sheet by itself. |
| **Cash & T-Bills**                   | Opportunity cost falls                       | Opportunity cost rises                       | Fed above-neutral policy rate still makes short T-Bills attractive carry.                                                        |

Long-term investors should translate QE/QT **not** into frenetic trades but into **valuation & risk-premium context**: when QT pushes real yields materially higher, require a bigger forward earnings yield to add equity risk.

---

### 9 · Five Fed myths—cleared up with the "sponge" picture in mind

1. **"Every Fed bond-buy is money-printing."**
   QE simply swaps a Treasury for a bank-reserve dollar—**assets up, reserves up, same dollar amount of public wealth**. It's balance-sheet plumbing, not handing out cash to households.

2. **"QT pulls cash straight out of people's wallets."**
   QT retires **bank reserves**, not consumer deposits. Retail cash only shrinks if banks react by cutting credit or hiking lending rates.

3. **"Smaller balance sheet = more cash in markets."**
   *Opposite.* Shrinking assets means the sponge contracts and **sucks reserves back in**, leaving **less** liquidity outside.

4. **"Balance-sheet size alone drives inflation."**
   History shows only a loose link; what matters is the mix of balance-sheet stance, rate policy, fiscal flow, and expectations.

5. **"Slowing QT is stealth QE."**
   A Treasury line that's falling—or merely flat—on the H.4.1 report is still neutral-to-tight; true QE begins only when that line turns **up**.

---

#### Bottom line for long-term investors

Keep one eye on **two yields** (2-yr Treasury and 10-yr TIPS) and the **slope** of the Treasury line in H.4.1. Use them to sanity-check valuations and liquidity assumptions; let the rest of the daily QE/QT chatter roll off like water from a sponge.

---

## Appendix A · Live FRED Charts

Below are direct, one-click links to the three **live FRED charts** you need. Bookmark each; when you open them the graph will auto-refresh with the latest data, so you don't have to download anything or fiddle with settings.

| What to watch                           | FRED chart link                                                                        | Why it matters                                                                                                        |
| --------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **2-Year Treasury yield**               | [https://fred.stlouisfed.org/series/DGS2](https://fred.stlouisfed.org/series/DGS2)     | Market's rolling 18-month view of Fed policy. A sharp ↑ (≈ +50 bp in a month) signals tighter conditions.|
| **10-Year TIPS real yield**             | [https://fred.stlouisfed.org/series/DFII10](https://fred.stlouisfed.org/series/DFII10) | Your DCF discount-rate anchor. Sustained ↑ compresses equity multiples.
| **Fed Treasury holdings (slope of QT)** | [https://fred.stlouisfed.org/series/TREAST](https://fred.stlouisfed.org/series/TREAST) | If the line is falling, QT is draining liquidity; flat for ≈ 8 weeks = QT paused.                         |

> **How to read them quickly**
> • **Direction** beats precision—look for trend bends, not daily squiggles.
> • Pair the two yields with the QT slope: rising real yields **and** a falling QT line = double liquidity headwind; the opposite = tail-wind.
> • A simple traffic-light rule: no ≥ 50 bp moves and QT line still down → *green* (stay the course).

Open each chart in a pinned browser tab or a FRED dashboard and you've got your "two yields + one slope" cockpit—no extra data wrangling required.

## Appendix B · Interpreting the Three FRED Charts (snapshot = 2025-05-15)

![2-Year Treasury Yield](images/20250519-01-2y.png)
> **2-Year Treasury Yield**

![10-Year TIPS Real Yield](images/20250519-02-10y.png)
> **10-Year TIPS Real Yield**

![Fed Treasury Holdings (TREAST)](images/20250519-03-bs.png)
> **Fed Treasury Holdings (TREAST)**

| Chart                                                                                                 | What you're seeing                                                                                                                                | What it means in the "sponge" framework                                                                                                    | Quick rule of thumb                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **① 2-Year Treasury Yield**<br>*(Market view of Fed policy 12-18 mos ahead—current obs ≈ **3.96 %**)* | From 2020-21 near-zero, the blue line ramps to ≈ 5 % in early 2023, then eases to \~4 % today.                                                    | Falling line = traders expect **easier** policy ahead (the sponge may stop shrinking or even swell later). Rising = tighter policy coming. | **±50 bp in a month** is a "yellow light." Nothing close to that this month → *green*.                                                                             |
| **② 10-Year TIPS Real Yield**<br>*(Discount-rate anchor—current obs ≈ **2.11 %**)*                    | Negative through mid-2022, then a vertical climb to > 2 % and has held around that level.                                                         | Real yield ↑ ⇒ DCF denominator ↑ ⇒ higher hurdle for equity valuations; real yield ↓ reverses that.                                        | Sustained **≥ 50 bp** move sets off a valuation check. Flat the last month → *green*.                                                                              |
| **③ Fed Treasury Holdings (TREAST)**<br>*(Balance-sheet "sponge size"—current level ≈ **\$4.22 T**)*  | Steady climb post-COVID (2020-22), peak near \$5.6 T, then an unbroken downslope—still pointing lower but the angle has flattened since Apr-2025. | Down-slope = QT is still **draining** liquidity. Flattening tells you the drain has slowed to a **"slow sip."**                            | If this line flattens for **≥ 8 weeks**, QT is effectively paused. Right now it's still slipping → *green* to *yellow* (watch the slope over the next two months). |

### Putting them together

1. **Direction check:**
   *2-yr yield down*, *real yield flat*, *TREAST still drifting lower* ⇒ policy expectations easing a bit, discount rate steady, liquidity still draining but gently.
2. **Traffic-light verdict (2025-05-15 snapshot):**
   All three gauges sit in **green** territory—no regime-shift signals for a long-term allocation.
3. **What would flip the light:**
   *Any* of the following:

   * 2-yr yield or 10-yr real yield jumps **≥ 50 bp** in a month (tightening shock).
   * TREAST line flattens eight straight weeks (QT pause) **or** turns up (QE restart).

Keep this cheat-sheet next to the charts and you can scan the whole macro backdrop in under two minutes, letting the rest of the QE/QT noise roll off—just like water off the sponge.

