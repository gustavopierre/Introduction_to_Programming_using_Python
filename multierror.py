def main():
    try:
        f=open('filex.txt')
        x = 1/0
    except FileNotFoundError as e:
        print('problem is ', e)
    except ZeroDivisionError as e:
        print("A problem occured ", e)

main()
