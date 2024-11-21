# website
import datetime

events = []

def addEvent():
    title = input("Event title: ")
    date = input("Event date (YYYY/MM/DD): ")
    time  = input("Event time (HH:MM): ")

    try:
        event_date = datetime.datetime.strptime(date, "%Y/%m/%d").date()
        event_time = datetime.datetime.strptime(time, "%H:%M").time()
    except ValueError:
        print("Invalid format or data.")
        return
    
    events.append({"Title":title, "Date": date, "Time": time})
    print("Event added!")

def listEvent():
    if events:
        print("Event: ")
        for i, event in enumerate(events, start = 0):
            print(f"{i}.{event}")
    else:
        print("No events scheduled.")

# remove event
def removeEvent():
    listEvent()
    try:
        eventToRemove = int(input("Enter # to remove: "))
        if eventToRemove < len(events):
            events.pop(eventToRemove)
            print(f"Event {eventToRemove} has been removed.")
        else:
            print(f"Event {eventToRemove} not found.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    print("---Event Calendar---")
    print("---Options---")
    print("1. Add event")
    print("2. List event")
    print("3. Remove event")
    print("4. Exit")

    choices = {
            "1" : addEvent,
            "2" : listEvent,
            "3" : removeEvent
        }
    
    while True:
        choice = input("Your choice: ")
        if choice == "4":
            print("Exiting program.")
            break
        action = choices.get(choice)
        if action:
            action()
        else:
            print("Invalid input. Try again.")
