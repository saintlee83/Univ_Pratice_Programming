import sys

# 전역 변수(global variable) 초기화
a = None
b = None
op = None
ret_v = None

# define function


def ds_add(x, y):
  """덧셈 함수"""
  return x + y


def ds_sub(x, y):
  """뺄셈 함수"""
  return x - y


def ds_mul(x, y):
  """곱셈 함수"""
  return x * y


def ds_div(x, y):
  """나눗셈 함수"""
  if y == 0:
    print("[ERROR] 0으로 나눌 수 없습니다.")
    return None
  return x / y


def main():
  """메인 함수"""
  global a, b, op, ret_v

  # 사용자 입력받기
  num_args = len(sys.argv)

  try:
    if num_args == 1:
      print("Interactive_mode!")
      op = input('(+,-,*,/): ')  # str
      a_str = input('a = ')  # str로 받아서 나중에 변환
      b_str = input('b = ')  # str로 받아서 나중에 변환
    elif num_args == 4:
      print("None_Interactive_mode!")
      op = sys.argv[1]
      a_str = sys.argv[2]
      b_str = sys.argv[3]
    else:
      print("[ERROR] 지원하지 않는 형태의 입력입니다.")
      print("사용법: python hw.py [연산자] [숫자1] [숫자2]")
      print("또는 인수 없이 실행하여 대화형 모드 사용")
      sys.exit(1)  # 종료

    # 문자열을 숫자로 변환
    a = float(a_str)
    b = float(b_str)

  except ValueError:
    print("[ERROR] 올바른 숫자를 입력해주세요.")
    sys.exit(1)
  except KeyboardInterrupt:
    print("\n프로그램이 중단되었습니다.")
    sys.exit(1)

  # 처리 : op:str, a:float, b:float
  print("processing...")

  if op == "+":
    ret_v = ds_add(a, b)  # a + b
  elif op == "-":
    ret_v = ds_sub(a, b)  # a - b
  elif op == "*":
    ret_v = ds_mul(a, b)  # a * b
  elif op == "/":
    ret_v = ds_div(a, b)  # a / b
  else:
    print(f"[ERROR] 지원하지 않는 연산자입니다: {op}")
    print("지원하는 연산자: +, -, *, /")
    sys.exit(1)

  # 출력
  if ret_v is not None:
    print("Output:")
    print(f"{a} {op} {b} = {ret_v}")


if __name__ == "__main__":
  main()
