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

def listEvent():
    if events:
        print("Event: ")
        for i, events in enumerate(events, start = 1):
            print(f"{i},{events}")
        else:
            print("No events scheduled.")

def removeEvent():
    return

if __name__ == "__main__":
    print("---Event Calendar---")