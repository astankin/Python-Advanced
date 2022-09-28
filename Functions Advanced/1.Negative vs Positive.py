def negative_positive(*args):
    negatives = [int(x) for x in args if int(x) < 0]
    positives = [int(x) for x in args if int(x) > 0]
    return sum(negatives), sum(positives)


negative_sum, positive_sum = negative_positive(*input().split())
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
