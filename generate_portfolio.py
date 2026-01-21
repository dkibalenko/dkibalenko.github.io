import json
from datetime import UTC, datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Load JSON data
with Path("portfolio-den.json").open(encoding="utf-8") as f:
    data = json.load(f)

# Add current year
data["current_year"] = datetime.now(tz=UTC).year

# Normalize phone numbers if stored as a single string
if isinstance(data["contact"].get("phone"), str):
    phones = [p.strip() for p in data["contact"]["phone"].split(",")]
    data["contact"]["phone_list"] = phones
else:
    data["contact"]["phone_list"] = data["contact"]["phone"]

# Load SVG icons
if "social_links" in data:
    for link in data["social_links"]:
        if link.get("svg_path"):
            svg_path = Path(link["svg_path"])
            if svg_path.exists():
                link["svg_data"] = svg_path.read_text(encoding="utf-8")

# Jinja environment
env = Environment(loader=FileSystemLoader("."), autoescape=True)

index_template = env.get_template("index_template.html")
resume_template = env.get_template("resume_template.html")

# Render HTML
index_output = index_template.render(**data)
resume_output = resume_template.render(**data)

# Write files
Path("index.html").write_text(index_output, encoding="utf-8")
Path("resume.html").write_text(resume_output, encoding="utf-8")

print("Portfolio and resume generated successfully.")
