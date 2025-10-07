import argparse


def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  if y == 0:
    raise ValueError("0으로 나눌 수 없습니다.")
  return x / y


def main():
  # ArgumentParser 객체 생성
  parser = argparse.ArgumentParser(description="간단한 CLI 계산기 프로그램")

  # 명령어 추가
  parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"],
                      help="수행할 연산: add, subtract, multiply, divide")
  parser.add_argument("x", type=float, help="첫 번째 숫자")
  parser.add_argument("y", type=float, help="두 번째 숫자")

  # 인자 파싱
  args = parser.parse_args()

  # 연산 매핑
  operations = {
      "add": add,
      "subtract": subtract,
      "multiply": multiply,
      "divide": divide
  }

  # 선택된 연산 실행
  try:
    result = operations[args.operation](args.x, args.y)
    print(f"결과: {result}")
  except ValueError as e:
    print(f"에러: {e}")


if __name__ == "__main__":
  main()
