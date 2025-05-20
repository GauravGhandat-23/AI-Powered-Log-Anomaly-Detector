<h1 align="center">🛡️🚨 AI-Powered Log Anomaly Detector 🚨🛡️</h1>

![Python](https://img.shields.io/badge/Python-3.9%2B-blueviolet) ![Groq AI](https://img.shields.io/badge/Groq%20AI-Powered-blue)

---
# Detects suspicious patterns in system logs using AI and NLP via the **Groq API**.

## Supports detection of:
- Brute force SSH attacks
- Failed login attempts
- Privileged user activity
- Unusual login times/locations

Runs from the command line, accepts log files like `/var/log/auth.log`, and outputs anomalies in plain text or JSON format.

---

## 🧰 Features

- ✅ CLI interface for easy use: `python detect_anomalies.py --log /var/log/auth.log`
- ✅ Tokenization and basic vector embedding support (future-ready)
- ✅ Uses Groq API with supported models (`llama3-70b-8192`, `mixtral-8x7b-32768`)
- ✅ Detects brute-force SSH attacks, failed login attempts, root access issues
- ✅ Outputs structured results in either **text** or **JSON**

---

## 📦 Requirements

```bash
pip install python-dotenv groq
```

Set your Groq API key in `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---
## ✅ Recommended Fix: Use a **Virtual Environment**

### Step-by-step guide to safely install your project dependencies:

#### 1. **Create a Virtual Environment**

```bash
python3 -m venv venv
```

This creates a folder called `venv` containing an isolated Python environment.

#### 2. **Activate the Virtual Environment**

```bash
source venv/bin/activate
```

Your terminal prompt will change to show `(venv)` indicating the virtual environment is active.

#### 3. **Install Requirements in Isolation**

Now run:

```bash
pip install -r requirements.txt
```

✅ This time it will work, because `pip` is installing into your local virtual environment, not the system-wide one.

---

## 🧪 Test Your App

With the virtual environment still active, run your script:

```bash
python detect_anomalies.py --log test_auth.log
```

---

## 📦 Deactivate When Done

To exit the virtual environment:

```bash
deactivate
```

---

## 🛠️ Optional: Install Required Tools

If you get an error about missing `venv`, install it first:

```bash
sudo apt install python3-venv
```

---

## 🧾 Summary

| Action | Command |
|-------|---------|
| Create virtual env | `python3 -m venv venv` |
| Activate it | `source venv/bin/activate` |
| Install packages | `pip install -r requirements.txt` |
| Run script | `python detect_anomalies.py --log test_auth.log` |
| Deactivate | `deactivate` |

## 📁 Project Structure

```
AI-Powered Log Anomaly Detector/
├── config.py
├── utils.py
├── prompts.py
├── detect_anomalies.py
├── README.md
└── test_auth.log  # Sample file for testing
```

---

## 🖥️ Usage

### 🔍 Basic Usage

```bash
python detect_anomalies.py --log /var/log/auth.log
```

### 📄 Output in Text Format

```bash
[+] Processing log chunk 1
[HIGH] 2023-03-28 03:15:01: Failed password attempt for root user from 192.168.1.100
[HIGH] 2023-03-28 03:15:02: Failed password attempt for invalid user 'admin' from 192.168.1.100 on non-standard port 23
```

### 📊 Output in JSON Format

```bash
python detect_anomalies.py --log /var/log/auth.log --output json
```

```json
[
    {
        "timestamp": "2023-03-28 03:15:01",
        "description": "Failed password attempt for root user from 192.168.1.100",
        "severity": "high"
    },
    {
        "timestamp": "2023-03-28 03:15:02",
        "description": "Failed password attempt for invalid user 'admin' from 192.168.1.100 on non-standard port 23",
        "severity": "high"
    }
]
```

---

## 🖥️ Windows Example

```powershell
PS D:\Projects\AI-Powered Log Anomaly Detector> python detect_anomalies.py --log test_auth.log
[+] Processing log chunk 1
[HIGH] 2023-03-28 03:15:01: Failed password attempt for root user from 192.168.1.100
[HIGH] 2023-03-28 03:15:02: Failed password attempt for invalid user 'admin' from 192.168.1.100 on non-standard port 23
```

---

## 🐧 Linux Example

```bash
$ sudo python3 detect_anomalies.py --log /var/log/auth.log
[+] Processing log chunk 1
[HIGH] 2023-03-28 03:15:01: Failed password attempt for root user from 192.168.1.100
[HIGH] 2023-03-28 03:15:02: Failed password attempt for invalid user 'admin' from 192.168.1.100 on non-standard port 23
```

---

## ⚙️ Future Enhancements

- 🔍 Real-time log streaming (e.g., journalctl, syslog-ng)
- 🤖 Local LLM integration (Ollama, HuggingFace Transformers)
- 📈 Machine learning-based anomaly pattern recognition
- 🧩 SIEM integrations (Splunk, Graylog, ELK)

---
## 🤝 Contributing
Feel free to **fork** the repository, submit **issues**, or contribute **pull requests** to improve the project.

---
## 🔗 Contact & Support
Have questions or suggestions? Feel free to reach out:

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)














