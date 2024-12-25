from datetime import datetime
from pathlib import Path
from tts.gtts import gtts_local

def greeting_based_on_time():
    current_hour = datetime.now().hour
    current_directory = Path(__file__).parent
    
    morning = current_directory / '..' / 'assets' / 'good morning.mp3'
    morning = morning.resolve()
    
    day = current_directory / '..' / 'assets' / 'good day.mp3'
    day = day.resolve()
    
    evening = current_directory / '..' / 'assets' / 'good evening.mp3'
    evening = evening.resolve()

    night = current_directory / '..' / 'assets' / 'good night.mp3'
    night = night.resolve()
    
    # Визначаємо привітання в залежності від години
    if 6 <= current_hour < 12:
        gtts_local(morning)
    elif 12 <= current_hour < 18:
        gtts_local(day)
    elif 18 <= current_hour < 22:
        gtts_local(evening)
    else:
        gtts_local(night)

