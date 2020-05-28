# def centered_average(nums):
#     min_num = nums[0]
#     max_num = nums[0]
#     sum = 0
#     length = 0
#     for n in nums:
#         sum += n
#         length += 1
#         if n < min_num:
#             min_num = n
#         if n > max_num:
#             max_num = n

# return(sum - min_num - max_num) / (length - 2)

def centered_average(nums):
    min_num = min(nums)
    max_num = max(nums)
    total_sum = sum(nums)
    length = len(nums)

    return int((total_sum - min_num - max_num) /(length - 2))