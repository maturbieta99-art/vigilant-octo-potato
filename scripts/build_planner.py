"""Builds product/Debt-Freedom-Planner.xlsx."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.chart import LineChart, Reference
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.comments import Comment
import datetime

F = "Arial"
NAVY, TEAL, CREAM, INPUT = "1F2A44", "2A9D8F", "F7F5EF", "FFF4C2"
H1 = Font(name=F, size=20, bold=True, color=NAVY)
H2 = Font(name=F, size=12, bold=True, color="FFFFFF")
B = Font(name=F, size=10)
BB = Font(name=F, size=10, bold=True)
BLUE = Font(name=F, size=10, color="0000FF")
NOTE = Font(name=F, size=9, italic=True, color="666666")
BIG = Font(name=F, size=16, bold=True, color=TEAL)
HFILL = PatternFill("solid", fgColor=NAVY)
IFILL = PatternFill("solid", fgColor=INPUT)
SFILL = PatternFill("solid", fgColor=CREAM)
thin = Side(style="thin", color="D0D0D0")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
USD = '$#,##0.00;($#,##0.00);"-"'
PCT = '0.00%'

wb = Workbook()

def base(ws, widths):
    ws.sheet_view.showGridLines = False
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[L(i)].width = w

def header(ws, row, labels, col=2):
    for i, t in enumerate(labels):
        c = ws.cell(row, col + i, t)
        c.font, c.fill, c.border = H2, HFILL, BOX
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 30

def cell(ws, ref, v, font=B, fmt=None, fill=None):
    c = ws[ref]; c.value = v; c.font = font; c.border = BOX
    if fmt: c.number_format = fmt
    if fill: c.fill = fill
    return c

# ---------------- Start Here ----------------
s = wb.active; s.title = "Start Here"; base(s, [3, 90])
s["B2"] = "Debt Freedom Planner"; s["B2"].font = H1
s["B3"] = "Budget · Debt Payoff (Snowball or Avalanche) · Savings Goals"; s["B3"].font = NOTE
lines = [
    ("HOW TO USE", True),
    ("1.  Only edit the YELLOW cells. Everything else calculates automatically.", False),
    ("2.  Monthly Budget: enter your take-home income and planned vs. actual spending.", False),
    ("3.  Debt Payoff: list up to 8 debts, choose Snowball or Avalanche, and add any extra monthly payment.", False),
    ("     The sheet tells you your debt-free date, total interest, and when each debt is paid off.", False),
    ("4.  Savings Goals: enter each goal, what you've saved, and your monthly contribution.", False),
    ("5.  The example values are there to show the format. Overwrite them with your own numbers.", False),
    ("", False),
    ("SNOWBALL vs. AVALANCHE", True),
    ("Snowball pays the smallest balance first. Quick wins keep you motivated.", False),
    ("Avalanche pays the highest interest rate first. It costs the least in total interest.", False),
    ("Either way, when a debt is paid off its payment rolls into the next one.", False),
    ("", False),
    ("ASSUMPTIONS", True),
    ("Interest is calculated monthly (APR ÷ 12) on each debt's starting balance for the month.", False),
    ("Your total monthly payment stays the same (sum of minimums + extra) until every debt is paid.", False),
    ("The projection runs up to 360 months (30 years). It's an estimate; your lender's statement is the final word.", False),
    ("This planner is an educational tool and is not financial advice.", False),
    ("", False),
    ("Works in Microsoft Excel and Google Sheets (File → Import), and in LibreOffice.", False),
]
for i, (t, bold) in enumerate(lines, 5):
    s.cell(i, 2, t).font = BB if bold else B
s["B26"] = "Example cell to edit"; s["B26"].fill = IFILL; s["B26"].font = BLUE; s["B26"].border = BOX

# ---------------- Monthly Budget ----------------
b = wb.create_sheet("Monthly Budget"); base(b, [3, 28, 16, 16, 16, 4, 30, 18])
b["B2"] = "Monthly Budget"; b["B2"].font = H1
header(b, 4, ["Income", "Planned", "Actual", "Difference"])
income = [("Paycheck 1", 2100, 2100), ("Paycheck 2", 2100, 2100), ("Side income", 300, 240), ("Other", 0, 0)]
r = 5
for name, p, a in income:
    cell(b, f"B{r}", name, BLUE, fill=IFILL); cell(b, f"C{r}", p, BLUE, USD, IFILL)
    cell(b, f"D{r}", a, BLUE, USD, IFILL); cell(b, f"E{r}", f"=D{r}-C{r}", B, USD); r += 1
cell(b, "B9", "Total income", BB); cell(b, "C9", "=SUM(C5:C8)", BB, USD)
cell(b, "D9", "=SUM(D5:D8)", BB, USD); cell(b, "E9", "=D9-C9", BB, USD)

header(b, 11, ["Expense", "Planned", "Actual", "Left / (Over)"])
exp = [("Rent / Mortgage", 1400, 1400), ("Utilities", 180, 195), ("Groceries", 450, 510),
       ("Transportation", 250, 230), ("Insurance", 160, 160), ("Phone / Internet", 110, 110),
       ("Subscriptions", 45, 62), ("Dining out", 150, 210), ("Personal / Fun", 120, 95),
       ("Health", 60, 40), ("Debt payments", "='Debt Payoff'!D17", "='Debt Payoff'!D17"),
       ("Savings", "='Savings Goals'!E15", "='Savings Goals'!E15"), ("Other", 0, 0), ("Other", 0, 0)]
r = 12
for name, p, a in exp:
    linked = isinstance(p, str)
    cell(b, f"B{r}", name, B if linked else BLUE, fill=None if linked else IFILL)
    cell(b, f"C{r}", p, Font(name=F, size=10, color="008000") if linked else BLUE, USD, None if linked else IFILL)
    cell(b, f"D{r}", a, Font(name=F, size=10, color="008000") if linked else BLUE, USD, None if linked else IFILL)
    cell(b, f"E{r}", f"=C{r}-D{r}", B, USD); r += 1
end = r - 1
b["B22"].comment = Comment("Pulled automatically from the Debt Payoff tab (total monthly payment).", "Planner")
b["B23"].comment = Comment("Pulled automatically from the Savings Goals tab (total monthly contributions).", "Planner")
cell(b, f"B{r}", "Total expenses", BB); cell(b, f"C{r}", f"=SUM(C12:C{end})", BB, USD)
cell(b, f"D{r}", f"=SUM(D12:D{end})", BB, USD); cell(b, f"E{r}", f"=C{r}-D{r}", BB, USD)
tot = r
b.conditional_formatting.add(f"E12:E{tot}", CellIsRule(operator="lessThan", formula=["0"], font=Font(name=F, color="C0392B", bold=True)))

# summary panel
b["G4"] = "This month at a glance"; b["G4"].font = BB
summ = [("Income (actual)", "=D9", USD), ("Spending (actual)", f"=D{tot}", USD),
        ("Left over", f"=D9-D{tot}", USD), ("Savings rate", f"=IFERROR('Savings Goals'!E15/D9,0)", "0.0%"),
        ("Unassigned (planned)", f"=C9-C{tot}", USD)]
for i, (k, f, fmt) in enumerate(summ, 5):
    cell(b, f"G{i}", k, B, fill=SFILL); cell(b, f"H{i}", f, BB, fmt, SFILL)
b["H7"].font = BIG
b["G11"] = "Tip: aim for 'Unassigned (planned)' = $0. Give every dollar a job."; b["G11"].font = NOTE
b.conditional_formatting.add("H7", CellIsRule(operator="lessThan", formula=["0"], font=Font(name=F, size=16, bold=True, color="C0392B")))

# ---------------- Debt Payoff ----------------
d = wb.create_sheet("Debt Payoff"); base(d, [3, 24, 15, 11, 15, 12, 4, 15, 16, 18])
d["B2"] = "Debt Payoff Planner"; d["B2"].font = H1
cell(d, "B4", "Payoff method", BB); cell(d, "C4", "Avalanche", BLUE, fill=IFILL)
dv = DataValidation(type="list", formula1='"Snowball,Avalanche"', allow_blank=False); d.add_data_validation(dv); dv.add("C4")
cell(d, "B5", "Extra payment / month", BB); cell(d, "C5", 200, BLUE, USD, IFILL)
cell(d, "B6", "Start month", BB); cell(d, "C6", datetime.date(2026, 11, 1), BLUE, "mmm yyyy", IFILL)
d["D4"] = "← pick from list"; d["D4"].font = NOTE
d["D5"] = "← on top of all minimum payments"; d["D5"].font = NOTE

header(d, 8, ["Debt name", "Balance", "APR", "Min payment", "Pay order", "", "Paid off in (months)", "Paid off", "Interest paid"])
debts = [("Credit card A", 4200, 0.2449, 120), ("Credit card B", 1350, 0.1999, 40), ("Car loan", 9800, 0.069, 285),
         ("Student loan", 14500, 0.055, 160), ("", 0, 0, 0), ("", 0, 0, 0), ("", 0, 0, 0), ("", 0, 0, 0)]
for i, (n, bal, apr, mn) in enumerate(debts):
    r = 9 + i
    cell(d, f"B{r}", n or None, BLUE, fill=IFILL); cell(d, f"C{r}", bal, BLUE, USD, IFILL)
    cell(d, f"D{r}", apr, BLUE, PCT, IFILL); cell(d, f"E{r}", mn, BLUE, USD, IFILL)
    # hidden sort key in column L; rank shown in F
    d[f"L{r}"] = f'=IF(N(C{r})<=0,1E+12,IF($C$4="Snowball",C{r},-D{r}))+ROW()/1E+9'
    cell(d, f"F{r}", f'=IF(N(C{r})<=0,"",COUNTIF($L$9:$L$16,"<"&L{r})+1)', BB)
    d[f"F{r}"].alignment = Alignment(horizontal="center")
    col = L(2 + i)  # calc column for Start bal block uses i
    endcol = L(51 + i)   # AY.. End balances
    intcol = L(10 + i)   # J.. Interest
    cell(d, f"H{r}", f'=IF(N(C{r})<=0,"",IF(INDEX(Calc!{endcol}:{endcol},363)>0.005,"30+ yrs",COUNTIF(Calc!{endcol}3:{endcol}362,">0.005")+1))', B)
    cell(d, f"I{r}", f'=IF(N(C{r})<=0,"",IF(ISNUMBER(H{r}),EDATE($C$6,H{r}-1),"—"))', B, "mmm yyyy")
    cell(d, f"J{r}", f'=IF(N(C{r})<=0,"",SUM(Calc!{intcol}3:{intcol}362))', B, USD)
d.column_dimensions["L"].hidden = True
d.conditional_formatting.add("B9:J16", FormulaRule(formula=['$F9=1'], fill=PatternFill("solid", fgColor="D8F3EF")))

cell(d, "B17", "Totals", BB); cell(d, "C17", "=SUM(C9:C16)", BB, USD)
cell(d, "D17", "=SUM(E9:E16)+C5", BB, USD); d["D17"].comment = Comment("Total monthly payment = all minimums + extra.", "Planner")
d["E17"] = "← total paid / month"; d["E17"].font = NOTE
cell(d, "J17", "=SUM(J9:J16)", BB, USD)

d["B19"] = "Your results"; d["B19"].font = BB
res = [("Debt-free date", '=IF(Calc!BG362>0.005,"Over 30 years: raise your payment",EDATE(C6,COUNTIF(Calc!BG3:BG362,">0.005")))', "mmmm yyyy"),
       ("Months to debt-free", '=IF(Calc!BG362>0.005,"360+",COUNTIF(Calc!BG3:BG362,">0.005")+1)', "0"),
       ("Total interest you'll pay", "=J17", USD),
       ("Paid first", '=IFERROR(INDEX(B9:B16,MATCH(1,F9:F16,0)),"")', None)]
for i, (k, f, fmt) in enumerate(res, 20):
    cell(d, f"B{i}", k, B, fill=SFILL); d.merge_cells(f"C{i}:E{i}")
    cell(d, f"C{i}", f, BIG if i == 20 else BB, fmt, SFILL)
d["B25"] = "Rows highlighted green are the debt to attack first. Try switching the method and changing the extra payment to see how your date moves."
d["B25"].font = NOTE
d["B26"] = "If a minimum payment doesn't cover the monthly interest, that debt will never shrink. Check 'Paid off in' for '30+ yrs'."
d["B26"].font = NOTE

# ---------------- Calc (month-by-month engine) ----------------
c = wb.create_sheet("Calc")
c["A1"] = "Month-by-month engine for the Debt Payoff tab. Don't edit."; c["A1"].font = NOTE
blocks = ["Start", "Interest", "Owed", "MinPay", "Remain", None, "Extra", "End"]
# column starts: Start B(2), Interest J(10), Owed R(18), MinPay Z(26), Remain AH(34), Pool AP(42), Extra AQ(43), End AY(51), Total BG(59)
starts = {"Start": 2, "Interest": 10, "Owed": 18, "MinPay": 26, "Remain": 34, "Extra": 43, "End": 51}
c["A2"] = "Month"; c["AP2"] = "Pool"; c["BG2"] = "Total end bal"
for k, s0 in starts.items():
    for i in range(8):
        c.cell(2, s0 + i, f"{k} {i+1}")
# rank row in row 1 for Remain block (AH1:AO1) so SUMPRODUCT can compare
for i in range(8):
    c.cell(1, 34 + i, f"=IF('Debt Payoff'!F{9+i}=\"\",99,'Debt Payoff'!F{9+i})")
remain_rng = "$AH{r}:$AO{r}"
for m in range(1, 361):
    r = m + 2
    c.cell(r, 1, m)
    for i in range(8):
        dr = 9 + i
        S, I, O, M, R, X, E = (L(starts[k] + i) for k in ["Start", "Interest", "Owed", "MinPay", "Remain", "Extra", "End"])
        c[f"{S}{r}"] = f"=N('Debt Payoff'!C{dr})" if m == 1 else f"={E}{r-1}"
        c[f"{I}{r}"] = f"={S}{r}*N('Debt Payoff'!D{dr})/12"
        c[f"{O}{r}"] = f"={S}{r}+{I}{r}"
        c[f"{M}{r}"] = f"=MIN({O}{r},N('Debt Payoff'!E{dr}))"
        c[f"{R}{r}"] = f"={O}{r}-{M}{r}"
        rank = f"{R}$1"
        c[f"{X}{r}"] = f"=MIN({R}{r},MAX(0,$AP{r}-SUMPRODUCT(($AH$1:$AO$1<{rank})*$AH{r}:$AO{r})))"
        c[f"{E}{r}"] = f"=ROUND({R}{r}-{X}{r},2)"
    c[f"AP{r}"] = f"=MAX(0,'Debt Payoff'!$D$17-SUM(Z{r}:AG{r}))"
    c[f"BG{r}"] = f"=SUM(AY{r}:BF{r})"
# row 363: final end balances for "never paid" check
for i in range(8):
    E = L(51 + i); c[f"{E}363"] = f"={E}362"
c.sheet_state = "hidden"

# chart on Debt Payoff
ch = LineChart(); ch.title = "Total debt over time"; ch.height = 7.5; ch.width = 16
ch.y_axis.title = "Balance ($)"; ch.x_axis.title = "Month"; ch.legend = None
ch.add_data(Reference(c, min_col=59, min_row=2, max_row=122), titles_from_data=True)
ch.set_categories(Reference(c, min_col=1, min_row=3, max_row=122))
ch.series[0].graphicalProperties.line.solidFill = TEAL; ch.series[0].graphicalProperties.line.width = 28000
ch.y_axis.number_format = '$#,##0'; ch.y_axis.delete = False; ch.x_axis.delete = False
d.add_chart(ch, "B28")

# ---------------- Savings Goals ----------------
g = wb.create_sheet("Savings Goals"); base(g, [3, 26, 15, 15, 16, 14, 16, 16])
g["B2"] = "Savings Goals"; g["B2"].font = H1
cell(g, "B4", "Today's date", BB); cell(g, "C4", "=TODAY()", B, "mmm d, yyyy")
header(g, 6, ["Goal", "Target", "Saved so far", "Monthly contribution", "Progress", "Months to go", "Reach it by"])
goals = [("Emergency fund", 6000, 1500, 250), ("Vacation", 2500, 400, 100), ("New laptop", 1400, 600, 0),
         ("", 0, 0, 0), ("", 0, 0, 0), ("", 0, 0, 0), ("", 0, 0, 0), ("", 0, 0, 0)]
for i, (n, t, sv, mc) in enumerate(goals):
    r = 7 + i
    cell(g, f"B{r}", n or None, BLUE, fill=IFILL); cell(g, f"C{r}", t, BLUE, USD, IFILL)
    cell(g, f"D{r}", sv, BLUE, USD, IFILL); cell(g, f"E{r}", mc, BLUE, USD, IFILL)
    cell(g, f"F{r}", f'=IF(N(C{r})<=0,"",MIN(1,D{r}/C{r}))', B, "0%")
    cell(g, f"G{r}", f'=IF(N(C{r})<=0,"",IF(D{r}>=C{r},0,IF(N(E{r})<=0,"Add a contribution",ROUNDUP((C{r}-D{r})/E{r},0))))', B, "0")
    cell(g, f"H{r}", f'=IF(ISNUMBER(G{r}),EDATE($C$4,G{r}),"")', B, "mmm yyyy")
from openpyxl.formatting.rule import DataBarRule
g.conditional_formatting.add("F7:F14", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=TEAL))
cell(g, "B15", "Totals", BB); cell(g, "C15", "=SUM(C7:C14)", BB, USD)
cell(g, "D15", "=SUM(D7:D14)", BB, USD); cell(g, "E15", "=SUM(E7:E14)", BB, USD)
cell(g, "F15", "=IFERROR(D15/C15,0)", BB, "0%")

from openpyxl.worksheet.properties import PageSetupProperties
for ws, area in [(s, "B2:B26"), (b, "B2:H26"), (d, "B2:J43"), (g, "B2:H15")]:
    ws.sheet_properties.tabColor = TEAL
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.print_area = area
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    ws.print_options.horizontalCentered = True
wb.save("/home/user/vigilant-octo-potato/product/Debt-Freedom-Planner.xlsx")
print("saved")
