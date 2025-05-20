# utils.py
import re
import json
from datetime import datetime

def read_log_file(path):
    try:
        with open(path, 'r') as f:
            return f.readlines()
    except Exception as e:
        print(f"[!] Error reading log file: {e}")
        return []

def chunk_logs(log_lines, size=20):
    """Split logs into chunks for better analysis"""
    for i in range(0, len(log_lines), size):
        yield log_lines[i:i+size]

def extract_timestamp(line):
    """Try to extract timestamp from common log formats"""
    match = re.match(r'^(\w+\s+\d+\s+\d+:\d+:\d+)', line)
    if match:
        try:
            return datetime.strptime(match.group(1), "%b %d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None
    return None

def extract_json(content):
    """Try to extract JSON from raw LLM response"""
    if not content:
        return []
    # Try to find JSON array or object
    match = re.search(r'\[.*\]|\{.*\}', content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return []