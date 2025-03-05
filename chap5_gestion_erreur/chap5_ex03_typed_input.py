def typed_intput(user_input ='>', type_ = int):

    while True:
        try:
            value = input(user_input)
            return type_(value)
        except ValueError:
            print(f'Vous devez fournir une entrée de type: {type_}')


#typed_intput('>', int)
typed_intput('>', float)
#typed_intput('>')