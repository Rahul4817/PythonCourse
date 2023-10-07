try:
    file=open("read.txt",'rb')
except EOFError as e:
    print('An EOF Error occurred.{}'.format(e.args[-1]))
    # raise e
    print(e)

except IOError as e:
    print('An error occurred.{}'.format(e.args[-1]))
    raise e
