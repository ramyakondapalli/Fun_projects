""" Testing password generator"""

from password_generator import password_gen


class test_pass_gen(password_gen):

    random_password = password_gen(6)
    random_password.pswd_gen()