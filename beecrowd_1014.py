# distance = int(input())
# fuel = float(input())
# avarage_cons = distance / fuel
# print("{:.3f}km/l".format(avarage_cons))
#

def cal_avg_con(dis, litter):
    avarage_cons = dis / litter
    return avarage_cons


dis = int(input())
litter = float(input())

result = cal_avg_con(dis, litter)
print("{:.3f} km/l".format(result))
