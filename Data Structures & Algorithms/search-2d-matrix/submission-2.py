class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        m x n array, integer target, each row is sorted in ascending order
        first int of the row is > than the last int of the previous row
        return true is a target exists within the matrix or false
        """

        s, e = 0, len(matrix) - 1
        while s <= e:
            m = (s + e) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                array = matrix[m]
                s_a, e_a = 0, len(array) - 1
                while s_a <= e_a:
                    m_a =  (s_a + e_a) // 2
                    if array[m_a] > target:
                        e_a = m_a - 1
                    elif array[m_a] < target:
                        s_a = m_a + 1
                    else:
                        return True
                return False
            elif matrix[m][0] > target:
                e = m - 1
            elif matrix[m][-1] < target:
                s = m + 1

        return False