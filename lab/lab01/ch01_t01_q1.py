def main():
    while True:
        mun = int(input("Type an integer:"))
        break
    except ValueError:
    print('Please enter an integer.')
    # Remove pass with your answer.
    if num % 10 == 0 and mun % 3 != 0:
        print(f'{num} is divisible by 10 and not divisible by 3.')
    else:
        print(f'{num} is not divisible by 10 or divisible by 3.')

if __name__ == "__main__":
    # execute only if run as a script
    main()
