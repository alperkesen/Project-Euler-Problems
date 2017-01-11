largestFactor :: Integer -> Integer -> Integer
largestFactor x c
    | x `div` c == 1 && x `mod` c == 0   = c
    | x `mod` c == 0                     = largestFactor (x `div` c) c
    | otherwise                          = largestFactor x (c+1)


main :: IO()
main = print (largestFactor 600851475143 2)