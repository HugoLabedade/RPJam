def heal(max_pv_user, compétence) :
    
    if compétence.id == 8 :
        return round(max_pv_user/4)

    elif compétence.id == 9 :
        return round(max_pv_user/2)

    elif compétence.id == 10 :
        return max_pv_user

    else :
        return 0