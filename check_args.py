def check_args_for_user_creation(args):
    u = args.username is not None
    p = args.password is not None
    d = args.delete is None
    e = args.edit is None
    return u and p and d and e

def check_args_for_changing_password(args):
    u = args.username is not None
    p = args.password is not None
    n = args.new_pass is not None
    e = args.edit is None
    return u and p and n and e