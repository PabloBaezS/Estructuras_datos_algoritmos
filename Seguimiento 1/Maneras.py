answers = []
lst = [3, 5, 7]
number = int(input())


def f(target):
    if number < 0:
        print(0)
        return
    val = 0
    for i in lst:  # O(lst.count())
        current = target - i
        if current > 0:
            val += answers[current - 1]
    if lst.__contains__(target):  # O(lst.count())
        val += 1
    answers.insert(target, val)


j = 1;
while j <= number:  # O(n) for while loop
    f(j)
    j += 1


if number < 0:
    print(0)
else:
    print(answers[number-1])