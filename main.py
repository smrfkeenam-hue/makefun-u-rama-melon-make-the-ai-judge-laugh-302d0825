"""Make the AI Judge Laugh — one office-life joke, one line.

The joke turns on the reply-all paradox: the plea to stop replying all
is itself answered by reply-all, so the complaint becomes the offence.
True to office life, tight, and the twist lands in the last two words.
"""

import os

ENTRY = "Someone hit reply-all to ask everyone to stop replying all. Forty-seven people have replied all to agree."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
