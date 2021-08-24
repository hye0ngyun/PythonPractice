students = {x for x in range(1, 30 + 1)}
submit = set()
for _ in range(28):
    n = int(input())
    submit.add(n)
not_submit = students - submit
length = len(not_submit)
for _ in range(length):
    print(min(not_submit))
    not_submit.remove(min(not_submit))
