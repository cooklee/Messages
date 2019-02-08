import argparse
from check_args import check_args_for_changing_password, check_args_for_user_creation


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help='User Login')
parser.add_argument('-p', '--password', help='User Password')
parser.add_argument('-n', '--new_pass', help='User New Password')
parser.add_argument('-l', '--list', help='Show all users')
parser.add_argument('-d', '--delete', help='User login to delete')
parser.add_argument('-e', '--edit', help='User Login to edit')
args = parser.parse_args()

if check_args_for_changing_password(args):
    print ("zmiana hasla dla uzytkownia")
elif check_args_for_user_creation(args):
    print('tworze uzytkownia')

