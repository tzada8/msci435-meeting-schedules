import itertools

import utils_functions

def generic_column_generation(member_to_chair_ratio):
    num_people = 20
    combinations = list(itertools.product([0, 1], repeat=num_people))

    # Infeasible columns criteria
    max_people_in_meetings = 12
    total_sums_allowed = [0, 6, 12]
    members_i_start = 5  # Corresponds to member 1 in list (6th element).

    # Filters Applied:
    #   1. At most 12 people can be in meetings at a time for each subgroup.
    #   2. Each room requires 6 attendees.
    #   3. A 1:5 ratio between chairs and members must be respected.
    generic_feasible_combinations = [
        combo for combo in combinations
        if sum(combo) in total_sums_allowed and sum(combo) <= max_people_in_meetings
        and sum(combo[:members_i_start]) * member_to_chair_ratio == sum(combo[members_i_start:])
    ]

    print("Total possible combinations:", len(combinations))
    print("Total feasible combinations:", len(generic_feasible_combinations))

    return generic_feasible_combinations

def group_column_generation(group_num, group_unavailability, generic_combos):
    group_person_unavailability = utils_functions.calculate_unavailability(group_unavailability)

    # Maps which members are unavailable for each timeslot
    group_timeslot_unavailability = {key: [] for key in range(1, 171)}
    for i, person_times in enumerate(group_person_unavailability):
        for timeslot in person_times:
            group_timeslot_unavailability[timeslot].append(i)
    print(f"Group {group_num} Unavailability Mapping:", group_timeslot_unavailability)

    # Filter applied ensures unavailable individuals are not assigned meetings.
    group_feasible_combinations = [
        [
            combo for combo in generic_combos
            if all(combo[i] == 0 for i in group_timeslot_unavailability[timeslot])
        ] for timeslot in range(1, 171)
    ]
    print(f"Possible Number of Combinations for Group {group_num} Timeslots:", [len(timeslot_combo) for timeslot_combo in group_feasible_combinations])

    return group_feasible_combinations
