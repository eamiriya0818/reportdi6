import random
from datetime import datetime

# 題庫
questions = [
    {"hint": "動物", "word": "animal"},
    {"hint": "書", "word": "book"},
    {"hint": "學校", "word": "school"},
    {"hint": "蘋果", "word": "apple"},
    {"hint": "朋友", "word": "friend"},
    {"hint": "家庭", "word": "family"},
    {"hint": "跑", "word": "run"},
    {"hint": "聽", "word": "listen"},
    {"hint": "笑", "word": "laugh"},
    {"hint": "學習", "word": "learn"}
]

# 產生填空字串
def generate_puzzle(word):
    if len(word) <= 3:
        return word[0] + '_' * (len(word) - 1)
    else:
        return word[0] + '_' * (len(word) - 2) + word[-1]

# 儲存紀錄
def save_log(log_list, score, total):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rate = round(score / total * 100, 1)
    with open("score_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== 測驗時間：{now} ===\n")
        for item in log_list:
            f.write(item + "\n")
        f.write(f"總分：{score} / {total}，正確率：{rate}%\n")

# 顯示所有紀錄
def show_all_logs():
    try:
        with open("score_log.txt", "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                print("\n📂 所有歷史紀錄：\n")
                print(content)
            else:
                print("⚠️ 尚無紀錄。")
    except FileNotFoundError:
        print("⚠️ 尚未建立紀錄檔。")

# 顯示最近一次紀錄
def show_last_log():
    try:
        with open("score_log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        last_index = None
        for i in range(len(lines)-1, -1, -1):
            if lines[i].startswith("=== 測驗時間："):
                last_index = i
                break
        if last_index is not None:
            print("\n🕓 最近一次紀錄：\n")
            print("".join(lines[last_index:]).strip())
        else:
            print("⚠️ 尚無最近紀錄。")
    except FileNotFoundError:
        print("⚠️ 尚未建立紀錄檔。")

# 主練習流程
def start_quiz():
    score = 0
    log = []
    qset = random.sample(questions, 10)
    print("\n📘 開始單字填空練習，共 10 題：\n")

    for i, q in enumerate(qset, 1):
        puzzle = generate_puzzle(q["word"])
        print(f"{i}. 提示：{q['hint']} → {puzzle}")
        ans = input("你的答案：").strip().lower()
        if ans == q["word"]:
            print("✅ 正確！\n")
            score += 1
            log.append(f"[{i}] {q['hint']} → {puzzle}\n你的答案：{ans} ✅")
        else:
            print(f"❌ 錯誤，正確答案是：{q['word']}\n")
            log.append(f"[{i}] {q['hint']} → {puzzle}\n你的答案：{ans} ❌ 正確答案：{q['word']}")

    rate = round(score / 10 * 100, 1)
    print(f"🎉 測驗完成！你答對 {score} / 10 題，正確率：{rate}%\n")
    save_log(log, score, 10)

# 主選單
def main_menu():
    while True:
        print("\n📋 主選單：")
        print("1️⃣ 開始練習")
        print("2️⃣ 顯示最近一次紀錄")
        print("3️⃣ 顯示所有紀錄")
        print("4️⃣ 離開程式")
        choice = input("請選擇（1/2/3/4）：").strip()

        if choice == "1":
            start_quiz()
        elif choice == "2":
            show_last_log()
        elif choice == "3":
            show_all_logs()
        elif choice == "4":
            print("👋 感謝使用，再見！")
            break
        else:
            print("⚠️ 請輸入有效選項（1～4）")

# 執行主程式
main_menu()
