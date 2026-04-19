scnd =int (input ("enter number"))
hour = scnd // 3600
rem= scnd % 3600
min = rem //60
scnd= rem % 60
print(scnd, hour, rem, min)
