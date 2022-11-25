from csv import writer

def create_problems():
    with open('results/problems.csv', 'w', encoding='utf8', newline='') as f:
        the_writer = writer(f)
        count = 0
        while count != 100:
            # num1, num2 = random.randint(0, 944799), random.randint(0, 944799)
            num1, num2 = count, count + 2
            if num1 != num2:
                count += 1
                info = [num1, num2]
                the_writer.writerow(info)


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    create_problems()
