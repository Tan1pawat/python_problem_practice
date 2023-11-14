# my_solution

# def bouncing_ball(h, bounce, window):
#     if h < 0 or bounce <= 0 or bounce >= 1 or window >= h: 
#         return -1
#     count = 0
#     ball_heigth = h*bounce
#     while ball_heigth > window:
#         count += 2
#         ball_heigth = ball_heigth*bounce
#     return count+1

# better solution

def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    return 2 + bouncing_ball(h * bounce, bounce, window)

print(bouncing_ball(10, 0.5, 5))