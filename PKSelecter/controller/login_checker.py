def login_check(pks_user_id, pks_user_pw):
    if pks_user_id.isdigit() != True and len(pks_user_id) != 9:
        return False
    elif len(pks_user_pw) != 6 and not (10 <= len(pks_user_pw) <= 16):
        return False
    else:
        return True