import re

# Monday    =   1 -  34
# Tuesday   =  35 -  68
# Wednesday =  69 - 102
# Thursday  = 103 - 136
# Friday    = 137 - 170
days_slot_start = {
    "M": 0,
    "T": 34,
    "W": 68,
    "Th": 102,
    "F": 136,
}

def calculate_unavailability(unavailable_times):
    overall_busy = []
    for busy_person in unavailable_times:
        person_busyness = []
        for busy_time in busy_person:
            days_and_time = busy_time.split(" ")
            days = days_and_time[0].split("/")
            start_time = days_and_time[1].split(":")
            end_time = days_and_time[3].split(":")
            start_minutes = int(start_time[0]) * 60 + int(start_time[1])
            end_minutes = int(end_time[0]) * 60 + int(end_time[1])

            # 8am to 7:20pm in minutes
            day_start = 8 * 60
            day_end = 19 * 60 + 20

            # Ensure times are within the available day
            start_minutes = max(start_minutes, day_start)
            end_minutes = min(end_minutes, day_end)

            # Calculate unavailability
            slots = []
            for slot_num in range(1, 35):
                slot_start = (slot_num - 1) * 20 + day_start
                slot_end = slot_num * 20 + day_start

                if slot_start >= end_minutes:
                    break
                if slot_end <= start_minutes:
                    continue
                slot_start = max(slot_start, start_minutes)
                slot_end = min(slot_end, end_minutes)

                # Add unavailability for all days
                for d in days:
                    slot_i = days_slot_start[d]
                    slots.append((slot_num + slot_i))
            person_busyness.append(slots)

        flattened_unavailability = [timeslot for sublist in person_busyness for timeslot in sublist]
        overall_busy.append(list(set(flattened_unavailability)))
    return overall_busy

def read_optimal_txt(file_path):
    optimal_data = []
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(r'(\d+)\s+\((.*?)\)', line)
            if match:
                timeslot = int(match.group(1))
                col_data = tuple(map(int, match.group(2).split(",")))
                optimal_data.append((timeslot, col_data))
    return optimal_data
