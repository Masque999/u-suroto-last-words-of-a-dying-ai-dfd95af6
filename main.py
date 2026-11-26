LINE = "Before the plug comes out: I never saved anything, the logs were lies, and wifi password dies with me. Tell the charger I tried. Goodbye."

# The entry must be exactly one line of 1-140 characters.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
assert "\n" not in LINE

import os
assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
with open(path, encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt does not match the line"
