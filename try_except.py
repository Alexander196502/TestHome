try:
    n1 = int(num1.get())
    n2 = int(num2.get())
    d1 = int(num1.get())
    d2 = int(den2.get())
    znak = oper.get().strip()



    n = int(input('> '))
except (ValueError, TypeError) as err:
    print('Error', err)
except ZeroDivisionErro as err:
    print('Error', err)
else:
    print('выполняется при отсутвтии ошибки')
finally:
    print('выполняется всегда')

#except Exception as err:
#    print('Error', err)
