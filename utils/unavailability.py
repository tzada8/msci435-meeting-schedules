# Each row represents a person's unavailability in EST time: [personal commitments, morning break, afternoon break, lunch break]
chairs_est_unavailability = [
    ["M/W 13:00 to 15:00", "M/T/W/Th/F 12:20 to 12:40", "M/T/W/Th/F 17:20 to 17:40", "M/T/W/Th/F 15:20 to 16:00"],
    ["T/Th 16:00 to 18:00", "M/T/W/Th/F 11:20 to 11:40", "M/T/W/Th/F 16:20 to 16:40", "M/T/W/Th/F 14:20 to 15:00"],
    ["M/W 13:00 to 15:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["T/F 9:00 to 11:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["Th 11:00 to 15:00", "M/T/W/Th/F 12:20 to 12:40", "M/T/W/Th/F 17:20 to 17:40", "M/T/W/Th/F 15:20 to 16:00"],
    ["W/F 10:00 to 12:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["T/Th 16:00 to 18:00", "M/T/W/Th/F 12:20 to 12:40", "M/T/W/Th/F 17:20 to 17:40", "M/T/W/Th/F 15:20 to 16:00"],
    ["Th 8:00 to 12:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["T/F 10:00 to 12:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/F 11:00 to 14:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"]
]

members_est_unavailability = [
    ["T/Th 14:00 to 16:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/W 13:00 to 15:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["T/F 9:00 to 11:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/Th 11:00 to 13:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/F 14:00 to 16:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/F 17:00 to 19:00", "M/T/W/Th/F 11:20 to 11:40", "M/T/W/Th/F 16:20 to 16:40", "M/T/W/Th/F 14:20 to 15:00"],
    ["M 12:00 to 14:00", "M/T/W/Th/F 8:20 to 8:40", "M/T/W/Th/F 13:20 to 13:40", "M/T/W/Th/F 11:20 to 12:00"],
    ["M/W 11:00 to 13:00", "M/T/W/Th/F 10:20 to 10:40", "M/T/W/Th/F 15:20 to 15:40", "M/T/W/Th/F 13:20 to 14:00"],
    ["Th 8:00 to 12:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["F 11:00 to 13:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/Th 10:00 to 12:00", "M/T/W/Th/F 8:20 to 8:40", "M/T/W/Th/F 13:20 to 13:40", "M/T/W/Th/F 11:20 to 12:00"],
    ["M/F 14:00 to 16:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/F 15:00 to 17:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["W 12:00 to 17:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["W/F 10:00 to 12:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["T/Th 13:00 to 15:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/W 10:00 to 12:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["T/F 10:00 to 12:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["Th 10:00 to 15:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["T/Th 15:00 to 17:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/T 8:00 to 10:00", "M/T/W/Th/F 4:20 to 4:40", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 7:20 to 8:00"],
    ["Th 11:00 to 15:00", "M/T/W/Th/F 12:20 to 12:40", "M/T/W/Th/F 17:20 to 17:40", "M/T/W/Th/F 15:20 to 16:00"],
    ["M/T 12:00 to 14:00", "M/T/W/Th/F 11:20 to 11:40", "M/T/W/Th/F 16:20 to 16:40", "M/T/W/Th/F 14:20 to 15:00"],
    ["T/W 17:00 to 19:00", "M/T/W/Th/F 11:20 to 11:40", "M/T/W/Th/F 16:20 to 16:40", "M/T/W/Th/F 14:20 to 15:00"],
    ["T/W 15:00 to 17:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["M/W 12:00 to 14:00", "M/T/W/Th/F 11:20 to 11:40", "M/T/W/Th/F 16:20 to 16:40", "M/T/W/Th/F 14:20 to 15:00"],
    ["M/F 11:00 to 14:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
    ["T/Th 6:00 to 8:00", "M/T/W/Th/F 2:20 to 2:40", "M/T/W/Th/F 7:20 to 7:40", "M/T/W/Th/F 5:20 to 6:00"],
    ["F 13:00 to 17:00", "M/T/W/Th/F 10:20 to 10:40", "M/T/W/Th/F 15:20 to 15:40", "M/T/W/Th/F 13:20 to 14:00"],
    ["T/Th 8:00 to 10:00", "M/T/W/Th/F 9:20 to 9:40", "M/T/W/Th/F 14:20 to 14:40", "M/T/W/Th/F 12:20 to 13:00"],
]

group1_chairs = [1, 5, 7, 2, 3]
group1_members = [22, 6, 24, 26, 23, 8, 29, 1, 2, 3, 4, 5, 9, 10, 12]
group2_chairs = [4, 6, 8, 9, 10]
group2_members = [13, 14, 15, 16, 17, 18, 19, 20, 25, 27, 30, 7, 11, 21, 28]

def form_groups(
        chair_unavailability,
        member_unavailability,
        g1_chairs = group1_chairs,
        g1_members = group1_members,
        g2_chairs = group2_chairs,
        g2_members = group2_members,
    ):
    group1_unavailability = [*[chair_unavailability[i-1] for i in g1_chairs], *[member_unavailability[i-1] for i in g1_members]]
    group2_unavailability = [*[chair_unavailability[i-1] for i in g2_chairs], *[member_unavailability[i-1] for i in g2_members]]
    return [group1_unavailability, group2_unavailability]

all_group_est_unavailability = [*chairs_est_unavailability, *members_est_unavailability]
main_groups = form_groups(chairs_est_unavailability, members_est_unavailability)
group1_est_unavailability = main_groups[0]
group2_est_unavailability = main_groups[1]

optimal_group1_chairs = [2, 7, 8, 9, 10]
optimal_group1_members = [6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
optimal_group2_chairs = [1, 3, 4, 5, 6]
optimal_group2_members = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

optimal_main_groups = form_groups(chairs_est_unavailability, members_est_unavailability, optimal_group1_chairs, optimal_group1_members, optimal_group2_chairs, optimal_group2_members)
optimal_group1_unavailability = optimal_main_groups[0]
optimal_group2_unavailability = optimal_main_groups[1]
