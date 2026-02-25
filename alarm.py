import datetime
import time
import threading

alarms = []

def is_valid_time(time_str):
    
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def add_alarm():
    print("\n🔔 Установка нового будильника")
    
    while True:
        time_input = input("Введите время (HH:MM): ").strip()
        if is_valid_time(time_input):
            break
        else:
            print("❌ Ошибка: некорректный формат времени. Используйте ЧЧ:ММ (например, 09:30)")

    label = input("Название будильника (по умолчанию 'Будильник'): ").strip()
    if not label:
        label = "Будильник"

    sound = input("Файл звука (например, alarm.mp3, Enter — без звука): ").strip()

    repeat_input = input("Повторять ежедневно? (да/нет): ").strip().lower()
    repeat = repeat_input in ['да', 'д', 'yes', 'y']

    alarm = {
        "time": time_input,
        "label": label,
        "sound": sound if sound else None,
        "repeat": repeat,
        "active": True
    }
    alarms.append(alarm)
    print(f"✅ Будильник '{label}' установлен на {time_input}.")


def play_sound_async(sound_file):
    """Проигрывает звук в отдельном потоке."""
    if sound_file:
        try:
            playsound(sound_file)
        except Exception as e:
            print(f"🔊 Не удалось воспроизвести звук: {e}")


def trigger_alarm(alarm):
    print(f"\n⏰ СРАБОТАЛ БУДЕЛЬНИК: {alarm['label']}!")
    print(f"   Время: {alarm['time']}")
    
    
    if alarm["sound"]:
        thread = threading.Thread(target=play_sound_async, args=(alarm["sound"],), daemon=True)
        thread.start()
    else:
        print("🔕 Звук отсутствует.")


def check_alarms():
    
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")

        for alarm in alarms:
            if alarm["active"] and alarm["time"] == current_time:
                trigger_alarm(alarm)
                if not alarm["repeat"]:
                    alarm["active"] = False  
        time.sleep(1)


def list_alarms():
    if not alarms:
        print("⏰ Нет установленных будильников.")
        return
    print("\n📋 Текущие будильники:")
    for i, a in enumerate(alarms, 1):
        repeat_text = "🔁 Ежедневно" if a["repeat"] else "⚪ Один раз"
        status = "Активен" if a["active"] else "Отключён"
        print(f"  {i}. {a['time']} — {a['label']} | {repeat_text} | [{status}]")


def main():
    print("⏰ Добро пожаловать в систему будильников!")

    
    thread = threading.Thread(target=check_alarms, daemon=True)
    thread.start()

    
    while True:
        print("\n--- Меню ---")
        print("1. Добавить будильник")
        print("2. Показать все будильники")
        print("3. Выход")
        
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            add_alarm()
        elif choice == "2":
            list_alarms()
        elif choice == "3":
            print("👋 До новых встреч!")
            break
        else:
            print("❗ Неверный ввод. Введите 1, 2 или 3.")

if __name__ == "__main__":
    main()