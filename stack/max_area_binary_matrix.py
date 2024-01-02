from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def next_smaller_left(arr):
            ans = []
            stack = []
            for i in range(len(arr)):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if not stack:
                    ans.append(0)
                else:
                    ans.append(stack[-1] + 1)
                stack.append(i)
            return ans

        def next_smaller_right(arr):
            ans = [0] * len(arr)
            stack = []
            for i in range(len(arr) - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if not stack:
                    ans[i] = len(arr) - 1
                else:
                    ans[i] = stack[-1] - 1
                stack.append(i)
            return ans

        def max_area_histogram(arr):
            width = [0] * len(arr)
            area = [0] * len(arr)
            right = next_smaller_right(arr)
            left = next_smaller_left(arr)
            for i in range(len(arr)):
                width[i] = right[i] - left[i] + 1
            
            for i in range(len(arr)):
                area[i] = width[i] * arr[i]
            
            ans = max(area)
            return ans

        histogram = list(map(int, matrix[0]))
        area = [max_area_histogram(histogram)]
        for row in range(1, len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == '1':
                    histogram[col] += 1
                else:
                    histogram[col] = int(matrix[row][col])
            ans = max_area_histogram(histogram)
            area.append(ans)
        max_area = max(area)
        return max_area

# Example usage:
matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]

solution = Solution()
ans = solution.maximalRectangle(matrix)
print(ans)
