# codewars

## Challenge 01: Array.diff
https://www.codewars.com/kata/523f5d21c841566fde000009

### Tests
```
Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
```

## Challenge 02: Loose Change
https://www.codewars.com/kata/5571f712ddf00b54420000ee/python

### Tests
```
test.assert_equals(loose_change(29),  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
test.assert_equals(loose_change(91),  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
test.assert_equals(loose_change(0),   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(-2),  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
```

## Challenge 03: Remove First & Last Characters
https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/python 

### Tests
```
test.assert_equals(remove_char('eloquent'), 'loquen')
test.assert_equals(remove_char('country'), 'ountr')
test.assert_equals(remove_char('person'), 'erso')
test.assert_equals(remove_char('place'), 'lac')
test.assert_equals(remove_char('ok'), '')
test.assert_equals(remove_char('ooopsss'), 'oopss')
```

## Challenge 04: Create Phone Number
https://www.codewars.com/kata/525f50e3b73515a6db000b83/python

### Tests
```
test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
```