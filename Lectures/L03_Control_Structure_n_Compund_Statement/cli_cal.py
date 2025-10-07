import sys  # 명령행 인자 처리를 위한 sys 모듈 임포트


def add(a, b):
  """덧셈 결과 출력"""
  result = a + b
  print(f"addition: {a} + {b} = {result}")
  return result


def subtract(a, b):
  """뺄셈 결과 출력"""
  result = a - b
  print(f"subtraction: {a} - {b} = {result}")
  return result


def multiply(a, b):
  """곱셈 결과 출력"""
  result = a * b
  print(f"multiplication: {a} * {b} = {result}")
  return result


def divide(a, b):
  """나눗셈 결과 출력"""
  if b == 0:  # 0으로 나누기 방지
    print("Error: Division by zero is not allowed")
    return None
  result = a / b
  print(f"division: {a} / {b} = {result}")
  return result


def calculate_with_operator(operator, a, b):
  """연산자에 따른 계산 함수 호출"""
  # match-case 문 사용 (Python 3.10+) - 구조적 패턴 매칭
  match operator:
    case '+':
      return add(a, b)
    case '-':
      return subtract(a, b)
    case '*':
      return multiply(a, b)
    case '/':
      return divide(a, b)
    case _:  # 기본 케이스 (지원하지 않는 연산자)
      print(f"Error: Unsupported operator '{operator}'")
      print("Supported operators: +, -, *, /")
      return None


def user_input_mode():
  """사용자 입력 모드"""
  try:
    # 연산자 입력 받기
    operator = input("Enter operation (+,-,*,/) : ")

    # 연산자 유효성 검사
    if operator not in ['+', '-', '*', '/']:
      print(f"Error: Unsupported operator '{operator}'")
      print("Supported operators: +, -, *, /")
      return

    # 피연산자 입력 받기
    a_input = input("a = ")
    b_input = input("b = ")

    # 문자열을 숫자로 변환 (예외 처리 포함)
    try:
      a = float(a_input)
      b = float(b_input)
    except ValueError:  # 숫자가 아닌 값이 입력된 경우
      print("Error: Please enter valid numbers")
      return

    # 계산 수행
    calculate_with_operator(operator, a, b)

  except KeyboardInterrupt:  # Ctrl+C 처리
    print("\nProgram terminated by user")
  except Exception as e:  # 기타 예외 처리
    print(f"Error: {e}")


def command_line_mode():
  """명령행 인자 모드"""
  try:
    # sys.argv에서 명령행 인자 파싱
    operator = sys.argv[1]  # 첫 번째 인자: 연산자
    a_input = sys.argv[2]   # 두 번째 인자: 첫 번째 피연산자
    b_input = sys.argv[3]   # 세 번째 인자: 두 번째 피연산자

    # 연산자 유효성 검사
    if operator not in ['+', '-', '*', '/']:
      print(f"Error: Unsupported operator '{operator}'")
      print("Supported operators: +, -, *, /")
      return

    # 문자열을 숫자로 변환
    # 문자열을 숫자로 변환
    try:
      a = float(a_input)
      b = float(b_input)
    except ValueError:  # 숫자 변환 실패 시
      print(f"Error: '{a_input}' or '{b_input}' is not a valid number")
      return

    # 계산 수행
    calculate_with_operator(operator, a, b)

  except Exception as e:
    print(f"Error: {e}")


def show_usage():
  """사용법 출력"""
  print("Usage:")
  print("  Command line mode: python calc.py <operator> <number1> <number2>")
  print("  Interactive mode:  python calc.py")
  print("")
  print("Examples:")
  print("  python calc.py + 3 5")
  print("  python calc.py - 10 4")
  print("  python calc.py '*' 2 6    # Note: quotes needed for * operator")
  print("  python calc.y / 15 3")
  print("")
  print("Supported operators: +, -, *, /")
  print("")
  print("Important: When using '*' operator, wrap it in quotes to prevent")
  print("shell wildcard expansion: python calc.py '*' 1 3")


def main():
  """메인 함수"""
  argc = len(sys.argv)  # 명령행 인자 개수 확인

  if argc == 1:
    # 인자가 없으면 사용자 입력 모드로 실행
    user_input_mode()
  elif argc == 4:
    # 인자가 3개면 명령행 인자 모드로 실행
    command_line_mode()
  else:
    # 인자 개수가 잘못된 경우 오류 메시지 출력
    print(
        f"Error: Invalid number of arguments (received {argc-1} arguments, expected 0 or 3)")
    print(f"Arguments received: {sys.argv[1:] if argc > 1 else 'none'}")
    print("")
    print("Note: If using '*' operator, wrap it in quotes: python calc.py '*' 1 3")
    print("")
    show_usage()


if __name__ == "__main__":  # 스크립트가 직접 실행될 때만 main() 함수 호출
  main()
