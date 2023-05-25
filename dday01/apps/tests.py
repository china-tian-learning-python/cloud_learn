# from django.test import TestCase
#
# # Create your tests here.
# def count_rabbits(month):
#     if month == 1:
#         return 1
#     elif month == 2:
#         return 2
#     else:
#         nums = [1, 2]  # 前两个月的兔子总数
#         for i in range(2, month):
#             nums.append(nums[i-1] + nums[i-2])  # 当前月的兔子总数
#         return nums[-1]  # 返回第12个月的兔子总数
# print(count_rabbits(13))
#
#
# '''
#
# {#    <li>#}
# {#      <a href="#" aria-label="Previous">#}
# {#        <span aria-hidden="true">&laquo;</span>#}
# {#      </a>#}
# {#    </li>#}
# {#    <li><a href="?page=1" class="active">1</a></li>#}
# {#    <li><a href="?page=2">2</a></li>#}
# {#    <li><a href="?page=3">3</a></li>#}
# {#    <li><a href="?page=4">4</a></li>#}
# {#    <li><a href="?page=5">5</a></li>#}
# {#    <li>#}
# {#      <a href="#" aria-label="Next">#}
# {#        <span aria-hidden="true">&raquo;</span>#}
# {#      </a>#}
# {#    </li>#}
#
#
# '''
list1=[14,2,1]
list2=[2,4,2]
win=0
list1.sort()
list2.sort()

for i in range(len(list2)):
    for j in range(i,len(list1)):
        if list1[j] <list2[i]:
           continue

        else:
            win += 1
            print(f"{list1[j], j}赢了{list2[i], i}")
            break

