## Sets

nums  = {1, 2, 3, 4}
nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

## No duplicates are allowed
nums3 = { 1, 2, 2, 3}
print(nums3)

## True is a dupe of 1, false is a dupe of zero
nums4 = {1, True, 2, False, 3, 4, 0}
print(nums4)

## Check if a value is in a set
print(2 in nums)

## Remember you cannot refer to an element in the set with an index position or a key

## add new elements to a set
nums.add(8)

## add elements from one set to another
more_nums ={5, 6, 7}
nums.update(more_nums)
print(nums)

## you can use update with lists, tuples, and dictionaries, too


## Merge two sets to get a new set
one = { 1, 2, 3}
two = { 5, 6, 7}
my_new_set = one.union(two)
print(my_new_set)


three = { 1, 2, 3}
four = { 2, 3, 4}

## return common values
print(three.intersection(four))

## Keep only the duplicates from two sets
three.intersection_update(four)
print(three)

three = { 1, 2, 3}
four = { 2, 3, 4}

## in thisc ase keep everyhting except the duplcaites
four.symmetric_difference_update(three)
print(four)