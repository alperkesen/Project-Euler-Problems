triplet :: [(Int, Int, Int)]
triplet = [(a,b,c) | b <- [1..1000], a <- [1..b],
           let c = 1000 - a - b, a^2 + b^2 == c^2]

productOfTriplet :: (Int, Int, Int) -> Int
productOfTriplet (x, y, z) = x * y * z

main :: IO()
main = (print . productOfTriplet) $ head triplet
