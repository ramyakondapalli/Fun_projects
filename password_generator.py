"""This module is created to generate random password for user which is minimum of 6 characters long
It is a mix of numbers, special characters, upper case and lower case characters"""

import random as rd
import string


class password_gen(object):
    """ This class generates the above mentioned password for every run"""
    def __init__(self, user_pass_length):
        self.user_pass_length = user_pass_length
        self.password = ""

    def pswd_gen(self):
        """ This function creates password for the user"""
        if self.user_pass_length == 6:
            S = string.ascii_letters
            first_character = rd.choice(S)
            second_character = str(rd.choice(range(0, 11)))
            third_character = rd.choice(S).upper()
            fourth_character = str(rd.choice('!@#$%^&*()_+:<>?|'))
            fifth_character = rd.choice(S).lower()
            sixth_character = rd.choice(S)

            self.password = first_character + second_character + third_character + fourth_character + fifth_character + sixth_character
            new_pass = []
            new_pass = rd.shuffle(self.password)


            else:
                print("Enter the valid length")


if __name__=="__main__":

    p_obj = password_gen(6)
    p_obj.pswd_gen()

