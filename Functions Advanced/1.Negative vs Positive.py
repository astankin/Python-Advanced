numbers = [int(num) for num in input().split()]
negatives_nums = sum([x for x in numbers if x < 0])
positives_nums = sum(filter(lambda x: x > 0, numbers))
print(negatives_nums)
print(positives_nums)
if abs(negatives_nums) > positives_nums:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
