# test task: multiply each element by 3
test = [10, 25, 33, 24, 15, 20]

# Not right
# for i in range(len(test)):
#     test[i] *= 3
#     print(test[i])
# print()


# Right - but incomplete
for item in test:
    item *= 3
    print(item)
print()


# Right - complete
for index, item in enumerate(test):
    item *= 3
    print(f"Item: {item}, Index: {index}")
print()


# Right - if only idex is needed
for index, _ in enumerate(test):
    test[index] *= 3
    print(test[index])
print()


# List Comprehension - for first case (which is not right)
elements = [3 * item for item in test]
print(elements)