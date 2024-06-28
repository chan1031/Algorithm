'''
이진탐색을 사용하는 경우는 다음과 같다
O(logn)의 시간 복잡도가 필요한 경우
즉, 데이터의 개수가 1000만개를 넘어가거나 탐색 범위의 크기가 1000억 이상인 경우
이진탐색을 사용한다.

이진탐색의 경우 우선 정렬이 되어 있어야 함을 기억한다.
구현 방법은 크게 두가지 (재귀함수, 일반 반복문)이다.

이진탐색 구현 방법은 암기를 해두도록 하자
'''
#재귀 함수로 구현
def binary_search(array, target, start, end):
  if start > end:
    return None
  #평균값을 구하기
  mid = (start + end) // 2
  #찾은 경우 반환
  if array[mid] == target:
    return mid

  #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽확인
  elif array[mid] > target:
      return binary_search(array, target, start,mid-1)

  #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽을 확인
  elif array[mid] < target:
      return binary_search(array, target, mid+1, end)

#일반 반복문으로 구현
def binary_search2(array, target, start,end):
  while start <=end:
    mid = (start + end) //2
    #찾은 경우 반환
    if array[mid] == target:
      return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽확인
    elif array[mid] > target:
      end = mid -1
    else:
      start = mid +1
  #반복문이 끝날떄까지 못찾으면 없다는 뜻이므로 None 반환
  return None

#원소의 개수와 찾고자 하는 값을 입력받음
n, target = list(map(int, input().split()))

#전체 배열의 값
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
  print("찾는 값이 없다")
else:
  print(result+1)

