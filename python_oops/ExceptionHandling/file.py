try:
    file=open("read.txt",'rb')
except (IOError,EOFError) as e:
    # print('An error occured.{}'.format(e.args[-1]))
    print(e)