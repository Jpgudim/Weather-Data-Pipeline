import schedule
import time
from extract_weather import main

main()

schedule.every().hour.do(main)

print("Schedule stared. Pipeline is running...")
print("Press Ctrl+C to exit.")

while True:
    schedule.run_pending()
    time.sleep(60)


