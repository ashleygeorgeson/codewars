# codewars!

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

## Challenge 06: Split Strings
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

### Tests
```
test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
```


## Challenge 08: Simple Encryption #1 Alternating Split
https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

### Tests
```
Test.describe('Basic Tests')
Test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
Test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
Test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
Test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
Test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
Test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
Test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

test.assert_equals(encrypt("", 0), "")
test.assert_equals(decrypt("", 0), "")
test.assert_equals(encrypt(None, 0), None)
test.assert_equals(decrypt(None, 0), None)
```

## Challenge 09: Multiples of 3 or 5
https://www.codewars.com/kata/514b92a657cdc65150000006

### Tests
```
test.assert_equals(solution(10), 23)
```

## Challenge 10: WeIrD StRiNg cAsE
https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python

### Tests
```
test.describe('to_weird_case')

test.it('should return the correct value for a single word')
test.assert_equals(to_weird_case('This'), 'ThIs')
test.assert_equals(to_weird_case('is'), 'Is')

test.it('should return the correct value for multiple words')
test.assert_equals(to_weird_case('This is a test'), 'ThIs Is A TeSt')
```

## Challenge 11: Sum of a Sequence
https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python

### Tests
```
test.assert_equals(sequence_sum(2, 6, 2), 12)
test.assert_equals(sequence_sum(1, 5, 1), 15)
test.assert_equals(sequence_sum(1, 5, 3), 5)
test.assert_equals(sequence_sum(0, 15, 3), 45)
test.assert_equals(sequence_sum(16, 15, 3), 0)
test.assert_equals(sequence_sum(2, 24, 22), 26)
test.assert_equals(sequence_sum(2, 2, 2), 2)
test.assert_equals(sequence_sum(2, 2, 1), 2)
test.assert_equals(sequence_sum(1, 15, 3), 35)
test.assert_equals(sequence_sum(15, 1, 3), 0)

```

## Challenge 12: Roman Numerals Decoder
https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

### Tests
```
test.describe("Example Tests")
test.assert_equals(solution('XXI'), 21, 'XXI should == 21')
test.assert_equals(solution('I'), 1, 'I should == 1')
test.assert_equals(solution('IV'), 4, 'IV should == 4')
test.assert_equals(solution('MMVIII'), 2008, 'MMVIII should == 2008')
test.assert_equals(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
```