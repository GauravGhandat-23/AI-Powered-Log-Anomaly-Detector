# detect_anomalies.py
import argparse
import json
import os
from config import GROQ_API_KEY, MODEL_NAME
from groq import Groq
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from utils import extract_json, read_log_file, chunk_logs

client = Groq(api_key=GROQ_API_KEY)

def analyze_log_with_groq(log_chunk):
    user_prompt = USER_PROMPT_TEMPLATE.format(log_chunk="".join(log_chunk))

    try:
        completion = client.chat.completions.create(
            model="qwen-qwq-32b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.6,
            max_tokens=4096,
            top_p=0.95,
            stream=False
        )

        content = completion.choices[0].message.content.strip()
        print("[DEBUG] Raw LLM Response:")
        print(content)
        
        return extract_json(content)

    except Exception as e:
        print(f"[!] Groq API Error: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Log Anomaly Detector using Groq")
    parser.add_argument("--log", required=True, help="Path to log file (e.g., /var/log/auth.log)")
    parser.add_argument("--output",default="text", choices=["text","json"], help="Output format")
    parser.add_argument("--quiet", action="store_true", help="Suppress all debug output, return only JSON")
    
    args = parser.parse_args()

    log_lines = read_log_file(args.log)
    if not log_lines:
        print("[!] No log data found.")
        return

    all_anomalies = []

    for i, chunk in enumerate(chunk_logs(log_lines)):
        print(f"[+] Processing log chunk {i+1}")
        anomalies = analyze_log_with_groq(chunk)
        all_anomalies.extend(anomalies)

    if args.output == "json":
        print(json.dumps(all_anomalies, indent=2))
    else:
        for anomaly in all_anomalies:
            print(f"[{anomaly['severity'].upper()}] {anomaly['timestamp']}: {anomaly['description']}")
     
    if not args.quiet:
        for anomaly in all_anomalies:
            print(f"[{anomaly['severity'].upper()}] {anomaly['timestamp']}: {anomaly['description']}")
    else:
        print(json.dumps(all_anomalies, indent=2))
    
if __name__ == "__main__":
    main()