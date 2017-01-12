leastCommon :: Integer -> Integer -> Integer
leastCommon x y
    | mod x y == 0  = x
    | gcd x y == 1  = x * y
    | otherwise     = x * (y `div` (gcd x y))

main :: IO()
main = print (foldl leastCommon 1 [1..20])