import datetime

# Your plan from Phase 0-2
TASKS = {
  0: "MON - BUCKET 1 (Big Co): Apply to 5: Capital One, JPMorgan, Amazon, Meta, Google. [ ] Resume keywords tweaked?",
  1: "TUE - BUCKET 2 (Fast Hire): Handshake + Book Alumni Meeting + Apply to 5: State Farm, UnitedHealth, Deloitte, Allstate, Liberty Mutual",
  2: "WED - BUCKET 3 (Scalis List): Push 1 GitHub README fix + Apply to 5 from Scalis PDF (Ctrl+F Data/Analyst/Quant)",
  3: "THU - BUCKET 4 (LinkedIn): Create 3 Job Alerts + Apply to 5 from alerts. 1) 'Data Sci New Grad OR Associate' 2) 'Data Analyst Applied Math' 3) 'MLE Early Career'",
  4: "FRI - BUCKET 5 (Small Co): Apply to 5 small cos: Indeed, BuiltIn, USAJobs. Weekly Goal: 15/15 done?",
  5: "SAT - SQL 30min + Clean 1 GitHub project + Log all apps in tracker",
  6: "SUN - Rest + Prep next week. Check: /5 apps per bucket?"
}

today = datetime.datetime.now().weekday()
day_name = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][today]

message = f"""Good morning! It's {day_name} - 10am check-in

TODAY'S TASKS:
{TASKS[today]}

Reply in Telegram tonight:
DONE - Applied to: [companies]
SQL: [y/n]

I'll see it tomorrow. Let's hit 15 this week."""

print(message)
