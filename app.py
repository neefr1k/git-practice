import datetime

def save_status():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"App checked at {now}\n"

    with open("status.log", "a") as f:
        f.write(text)

    print("Done!")

if __name__ == "__main__":
    save_status()