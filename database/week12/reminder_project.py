import uuid
import logging
from dataclasses import dataclass, field
from typing import List, Dict

logging.basicConfig(
    level=logging.INFO,
    filename="reminder.log",
    format="%(asctime)s | %(levelname)s | %(message)s"
)


@dataclass
class Reminder:
    title: str
    time: str
    reminder_id: str = ""

    def __post_init__(self):
        if not self.reminder_id:
            self.reminder_id = str(uuid.uuid4())

    def remind(self):
        return f"Reminder: {self.title} at {self.time}"


@dataclass
class SimpleReminder(Reminder):
    def remind(self):
        return f"reminder for {self.title} at {self.time}"


@dataclass
class MeetingReminder(Reminder):
    participants: List[str] = field(default_factory=list)

    def remind(self):
        names = ", ".join(self.participants) if self.participants else "—"
        return f"Meeting Reminder: your {self.title} is at {self.time} with {names}"


@dataclass
class DailyRoutineReminder(Reminder):
    daily_active: bool = True

    def remind(self):
        flag = "activated daily routine" if self.daily_active else "unactivated daily routine"
        return f"Daily Routine: {self.title} at {self.time} {flag}"


class ReminderManager:
    def __init__(self):
        self._reminders: Dict[str, Reminder] = {}

    def add_reminder(self, reminder: Reminder):
        self._reminders[reminder.reminder_id] = reminder
        logging.info(f"Reminder added: id={reminder.reminder_id}, title={reminder.title}, time={reminder.time}")

    def remove_reminder(self, reminder_id: str):
        if reminder_id in self._reminders:
            del self._reminders[reminder_id]
            logging.info(f"Reminder removed: id={reminder_id}")
            return True
        logging.warning(f"Reminder not found: id={reminder_id}")
        return False

    def list_reminders(self) -> List[Reminder]:
        return list(self._reminders.values())

    def execute_all(self):
        for r in self._reminders.values():
            print(r.remind())
            logging.info(f"Reminder executed: id={r.reminder_id}, type={type(r).__name__}")


if __name__ == "__main__":
    manager = ReminderManager()

    while True:
        print("\n--- Reminder Menu ---")
        print("1. Add Simple Reminder")
        print("2. Add Meeting Reminder")
        print("3. Add Daily Routine Reminder")
        print("4. Show All Reminders")
        print("5. Execute All Reminders")
        print("6. Remove Reminder by ID")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter reminder description: ")
            time = input("Enter reminder time (00:00): ")
            r = SimpleReminder(title=title, time=time)
            manager.add_reminder(r)
            print(f"Added SimpleReminder with ID {r.reminder_id}")

        elif choice == "2":
            title = input("Enter meeting subject: ")
            time = input("Enter meeting time (00:00): ")
            participants = input("Enter participants (comma separated): ").split(",")
            r = MeetingReminder(title=title, time=time, participants=[p.strip() for p in participants])
            manager.add_reminder(r)
            print(f"Added MeetingReminder with ID {r.reminder_id}")

        elif choice == "3":
            title = input("Enter daily routine: ")
            time = input("Enter routine time (00:00): ")
            repeat = input("Repeat daily? (yes/no): ").lower() == "yes"
            r = DailyRoutineReminder(title=title, time=time, daily_active=repeat)
            manager.add_reminder(r)
            print(f"Added DailyRoutineReminder with ID {r.reminder_id}")

        elif choice == "4":
            for r in manager.list_reminders():
                print(f"{r.reminder_id} → {r.remind()}")

        elif choice == "5":
            manager.execute_all()

        elif choice == "6":
            rid = input("Enter reminder ID to remove: ")
            if manager.remove_reminder(rid):
                print("Reminder removed.")
            else:
                print("Reminder not found.")

        elif choice == "7":
            print("all noted ! bye")
            break

        else:
            print("Invalid choice, try again.")

