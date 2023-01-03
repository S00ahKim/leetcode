"""
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List #python3.9 부터 내장 컬렉션 형을 제네릭으로 사용 가능

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 해결 방법: nxn 배열이면 n번째 배열은 뒤배열부터 n번째 요소로 구성됨
        # res = [[] for _ in range(len(matrix))]
        # matrix.reverse()
        # for n in range(len(matrix)):
        #   for m in matrix:
        #     res[n].append(m[n])
        # matrix = res ---> 이부분이 리트코드에서 정상적으로 동작하지 않음 ;;
        # print(matrix)
        matrix.reverse()
        matrix_size = len(matrix)
        for n in range(matrix_size):
          for m in matrix:
            matrix[n].append(m[n])

        for n in range(matrix_size):
          del matrix[n][:matrix_size]

        print(matrix)

if __name__ == "__main__":
    solution = Solution()
    solution.rotate([[1,2,3],[4,5,6],[7,8,9]]) # [[7,4,1],[8,5,2],[9,6,3]]