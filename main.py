class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self, n, arr):
        maximum, secondMaximum = -1, -1
        for x in arr:
            if x > maximum:
                if secondMaximum != maximum:
                    secondMaximum = maximum
                maximum = x
            if x > secondMaximum and x < maximum:
                secondMaximum = x

        return [maximum, secondMaximum]


def main():

    # testcase input
    testcases = int(input())

    # looping through all testcases
    while testcases > 0:

        n = int(input())

        arr = [int(x) for x in input().split()]

        li = Solution().largestAndSecondLargest(n, arr)
        print(li[0], end=' ')
        print(li[1])

        testcases -= 1


if __name__ == '__main__':
    main()
