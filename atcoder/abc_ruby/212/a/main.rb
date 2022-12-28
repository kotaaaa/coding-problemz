a,b = gets.split(" ").map(&:to_i)
# ans
if a > 0 and b == 0 then
    ans = "Gold"
elsif a == 0 and b > 0 then
    ans = "Silver"
else
    ans = "Alloy"
end
puts ans
