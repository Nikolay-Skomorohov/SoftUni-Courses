n = int(input())

best_ball = None
message = ""

for ball in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    result = (snowball_snow / snowball_time) ** snowball_quality
    if best_ball is None:
        best_ball = result
        message = f"{snowball_snow} : {snowball_time} = {result:.0f} ({snowball_quality})"
    else:
        if best_ball < result:
            best_ball = result
            message = f"{snowball_snow} : {snowball_time} = {result:.0f} ({snowball_quality})"


print(message)