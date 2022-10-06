list_gachimuchi = ["Billy Herrington", "Van Darkholme", "Steve Rambo"]

def group_by_surname(list_of_enrollees):
    a_i_group = []
    j_p_group = []
    q_t_group = []
    u_z_group = []

    for elem in list_of_enrollees:
        first_letter = elem.split(" ")[1][0]
        if ord(first_letter) in range(ord("A"), ord("I")):
            a_i_group.append(first_letter)
        elif ord(first_letter) in range(ord("J"), ord("P")):
            j_p_group.append(first_letter)
        elif ord(first_letter) in range (ord("Q"), ord("T")):
            q_t_group.append(first_letter)
        elif ord(first_letter) in range (ord("U"), ord("Z")):
            u_z_group.append(first_letter)


    return(len(a_i_group), len(j_p_group), len(q_t_group), len(u_z_group))

group_by_surname(list_gachimuchi)