import matplotlib.pyplot as plt

from timeslots import timeslot_times
import utils_functions

# Table Colours.
header_grey = "#ADADAD"
break_grey = "#D3D3D3"

def map_timeslots_to_num_rooms(group1_data, group2_data):
    # Map selected columns to number of occupied rooms.
    num_members_to_rooms = {
        0: 0,
        6: 1,
        12: 2,
        18: 3,
        24: 4,
    }

    group1_rooms_used_per_timeslot = {}
    for pattern in group1_data:
        group1_rooms_used_per_timeslot[pattern[0]] = num_members_to_rooms[sum(pattern[1])]

    group2_rooms_used_per_timeslot = {}
    for pattern in group2_data:
        group2_rooms_used_per_timeslot[pattern[0]] = num_members_to_rooms[sum(pattern[1])]

    # Merge both dictionaries
    rooms_per_timeslot = group1_rooms_used_per_timeslot.copy()
    for key, value in group2_rooms_used_per_timeslot.items():
        if key in rooms_per_timeslot:
            rooms_per_timeslot[key] += value
        else:
            rooms_per_timeslot[key] = value
        if rooms_per_timeslot[key] > 4:
            print(f"ERROR! Overbooking in timeslot {key}")

    print("Rooms per Timeslot:", dict(sorted((rooms_per_timeslot.items()))))
    return rooms_per_timeslot

def display_master_schedule(rooms_per_timeslot, saved_file_path):
    # Define the grid dimensions
    rows = 34
    cols = 20

    plt.figure(1, (10, 12))
    for i in range(cols):
        for j in range(rows):
            day = int(i/4)
            room = i%4+1
            timeslot = (j+1) + (day*rows)
            style = "bo" if timeslot in rooms_per_timeslot and rooms_per_timeslot[timeslot] >= room else "bx"
            plt.plot(i, rows - 1 - j, style)

    # Group columns into subsets of 4 and draw lines to separate the groups
    for col in range(4, cols, 4):
        plt.axvline(x=col - 0.5, color='red', linestyle='--')

    # Draw a vertical bar to separate labels from dots
    plt.axvline(x=-0.5, color='black', linewidth=1)

    # Add flipped labels to the rows (8:00 - 8:20 on the top)
    for i, label in enumerate(reversed(timeslot_times)):
        plt.text(-1, i, label, va='center', ha='right')

    plt.axis('off')
    plt.savefig(saved_file_path, bbox_inches="tight")
    plt.show()

# Creates table mapping for a person.
def person_availability_mapping(optimal_sol, person_index, group_unavailability):
    person_availability = {}
    person_busy = group_unavailability[person_index]

    for pattern in optimal_sol:
        if pattern[1][person_index] == 1:
            person_availability[pattern[0]] = ("Meeting", "red")

    personal_busy = utils_functions.calculate_unavailability([[person_busy[0]]])
    for slot in personal_busy[0]:
        person_availability[slot] = ("Busy", "yellow")

    break_busy = utils_functions.calculate_unavailability([[person_busy[1], person_busy[2]]])
    for slot in break_busy[0]:
        person_availability[slot] = ("BREAK", break_grey)

    lunch_busy = utils_functions.calculate_unavailability([[person_busy[3]]])
    for slot in lunch_busy[0]:
        person_availability[slot] = ("LUNCH", break_grey)

    for time in range(1, 171):
        if time not in person_availability:
            person_availability[time] = (None, "white")
    return person_availability

# Setup table data for a person.
def setup_table_schedule(person_title, availability):
    table_data = [
        [(person_title, "white"), ("Monday", header_grey), ("Tuesday", header_grey), ("Wednesday", header_grey), ("Thursday", header_grey), ("Friday", header_grey)],
    ]
    for i, time in enumerate(timeslot_times):
        row_data = [(time, header_grey)]
        for day in range(0, 5):
            cell = (i + 1) + (day * len(timeslot_times))
            row_data.append(availability[cell])
        table_data.append(row_data)
    return table_data

# Save schedules as images.
def save_group_schedules(group_people, optimal_sol, group_unavailability, prefix_path):
    for i, person in enumerate(group_people):
        person_title = f"Chair {person}" if i < 5 else f"Member {person}"
        person_availability = person_availability_mapping(optimal_sol, i, group_unavailability)
        table_data = setup_table_schedule(person_title, person_availability)
        text_data = [[cell[0] for cell in row] for row in table_data]
        colour_data = [[cell[1] for cell in row] for row in table_data]

        # Save schedule.
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis("off")
        table = ax.table(cellText=text_data, cellColours=colour_data, loc="center", cellLoc="center")
        plt.savefig(f"{prefix_path}/{person_title}.png", bbox_inches="tight")
        plt.close()
