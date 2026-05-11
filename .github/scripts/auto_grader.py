import os
import requests
import google.generativeai as genai

pr_number = os.environ.get('PR_NUMBER')
repo = os.environ.get('REPO')
gh_token = os.environ.get('GH_TOKEN')
gemini_api_key = os.environ.get('GEMINI_API_KEY')

genai.configure(api_key=gemini_api_key)

headers = {
    "Authorization": f"Bearer {gh_token}", 
    "Accept": "application/vnd.github.v3+json"
}

diff_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
diff_res = requests.get(diff_url, headers={"Authorization": f"Bearer {gh_token}", "Accept": "application/vnd.github.v3.diff"})
pr_diff = diff_res.text

commits_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/commits"
commits_res = requests.get(commits_url, headers=headers)
commits_data = commits_res.json()

timestamps = [commit['commit']['author']['date'] for commit in commits_data]
time_context = "Candidate Commit Timestamps (UTC):\n" + "\n".join(timestamps)

try:
    with open("best_practices.md", "r") as f:
        rubric = f.read()
except FileNotFoundError:
    rubric = "Error: best_practices.md not found. Grade based on standard optimization and correctness."

prompt = f"""
You are the automated grading assistant for an engineering assessment.

Here is the grading rubric and output requirements:
{rubric}

Here are the candidate's commit timestamps (use these to calculate the duration between Level 1, Level 2, and Level 3):
{time_context}

Here is the candidate's Pull Request Code Diff:
{pr_diff}

Analyze the code and timestamps. Output strictly the Markdown requested in the 'Output Requirements' section of the rubric. Do not include any other conversational text, greetings, or filler.
"""

model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(temperature=0.1)
)

report_content = response.text

with open("QUALITY_REPORT.md", "w") as f:
    f.write("# Final AI Transparency Report\n")
    f.write("Generated automatically upon challenge completion.\n\n")
    f.write(report_content)
