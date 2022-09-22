import pywhatkit
import time

hours = 9
minutes = 0

def main(hours, minutes) -> None:
    pywhatkit.sendwhatmsg(
        "+526461834219",
        '''Good Morning, Axel!
        Today's tasks are the following
        • 11:00 --> Go to school 
        • 17:00 --> Get a package
        • 20:00 --> Do homework''',
        hours,
        minutes,
        8, 
        True, 
        2
    )


if __name__ == "__main__":
    seconds = 84780
    contador = 1
    while True:
        print(f"Corrida #{contador}...")
        main(hours, minutes)
        time.sleep(seconds)
        contador += 1
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
            if hours == 25:
                hours = 1
           

