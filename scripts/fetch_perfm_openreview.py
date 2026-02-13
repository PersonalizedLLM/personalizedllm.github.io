#!/usr/bin/env python3
"""Fetch PerFM AAAI 2026 workshop submissions from OpenReview and print forum URLs."""
import openreview
import sys

VENUE_ID = "AAAI.org/2026/Workshop/PerFM"

def get_title(n):
    c = n.content or {}
    title = c.get("title") or c.get("Title") or ""
    if isinstance(title, dict):
        title = title.get("value", "")
    return title or "(no title)"

def main():
    client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")
    submissions = []
    try:
        group = client.get_group(VENUE_ID)
        sn = group.content.get("submission_name") or {}
        sn = sn.get("value", "Submission") if isinstance(sn, dict) else "Submission"
        inv = f"{VENUE_ID}/-/{sn}"
        submissions = list(client.get_all_notes(invitation=inv))
    except Exception as e:
        sys.stderr.write(f"Group fetch: {e}\n")
    if not submissions:
        for inv in [f"{VENUE_ID}/-/Submission", f"{VENUE_ID}/-/Blind_Submission"]:
            try:
                submissions = list(client.get_all_notes(invitation=inv))
                if submissions:
                    break
            except Exception:
                continue
    for n in submissions:
        print(f"https://openreview.net/forum?id={n.id}\t{get_title(n)}")
    if not submissions:
        sys.stderr.write("No submissions found.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
