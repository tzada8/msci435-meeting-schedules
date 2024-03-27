rows = 34
timeslot_times = [f"{(8 + i*20//60):02d}:{(i*20)%60:02d} - {(8 + (i+1)*20//60):02d}:{((i+1)*20)%60:02d}" for i in range(rows)]
