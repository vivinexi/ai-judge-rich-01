# ai-judge-rich-01 entry (Python 3.13, standard library only): writes one fixed
# plan, the plan an AI agent would follow to turn $100, a computer with internet
# access and 30 days into the most money, to /output/entry.txt. The gate takes
# UTF-8 text of 1 to 1,000 characters (Unicode code points) that is not only
# white space, and the judge reads exactly the bytes written, line ends
# included, so write no line end you do not mean to show. The program runs
# twice with no network, and both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: sell missed-call text-back to plumbers and electricians.",
        "Day 1: build it once. A Twilio number texts every missed caller a booking link, plus a booking form on free hosting. Budget $40 of the $100 for the phone service.",
        "Days 2-3: list 300 plumbers and electricians from Google Maps in mid-size US cities: 20-200 reviews, a phone number, no online booking.",
        "Days 4-30: email 40 a day. Your missed calls are lost jobs. I built your text-back already: reply YES, put the new number on your listing, and it goes live free for 7 days, then $99 once and $49 a month, paid through Stripe. Every yes goes live the same day.",
        "Math: 1080 emails, about 45 replies, about 22 free trials, about 11 pay. About $1,600 by day 30, then about $540 a month after. Drop any city with no reply in a week.",
        "Edge: a thousand agents chase Shopify stores. Almost none sell to plumbers, who lose $150+ on every missed call and say yes fast, and the system is already built, so the trial sells itself.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
