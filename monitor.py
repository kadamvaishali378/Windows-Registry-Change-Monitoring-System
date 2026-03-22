import winreg
import json
from datetime import datetime

BASELINE_FILE = "baseline.json"
LOG_FILE = "logs.txt"

# ---------- Utility ----------
def log_alert(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} {message}\n")
    print("🚨 ALERT:", message)


# ---------- Autorun Monitoring ----------
def get_current_run_key():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    data = {}

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        key_path,
        0,
        winreg.KEY_READ
    )

    i = 0
    while True:
        try:
            name, value, _ = winreg.EnumValue(key, i)
            data[name] = value
            i += 1
        except OSError:
            break

    winreg.CloseKey(key)
    return data


def check_autorun_changes():
    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)["HKCU_Run"]

    current = get_current_run_key()

    for key in current:
        if key not in baseline:
            log_alert(f"[AUTORUN] New startup entry: {key} -> {current[key]}")


# ---------- Malware-Like Detection ----------
def check_defender_tampering():
    defender_key_path = r"Software\Policies\Microsoft\Windows Defender"

    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            defender_key_path,
            0,
            winreg.KEY_READ
        )

        # 🔴 TEMP TEST ALERT (SAFE — REMOVE AFTER TEST)
        log_alert("[SECURITY] Suspicious Defender policy detected (TEST)")

        try:
            value, _ = winreg.QueryValueEx(key, "DisableAntiSpyware")
            if value == 1:
                log_alert("[SECURITY] Windows Defender appears DISABLED via registry")
        except FileNotFoundError:
            pass

        winreg.CloseKey(key)

    except FileNotFoundError:
        pass



# ---------- MAIN ----------
if __name__ == "__main__":
    print("\n🔍 Running registry security checks...\n")
    check_autorun_changes()
    check_defender_tampering()
    print("\n✅ Scan complete.")
