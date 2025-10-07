import argparse


def main():

  parser = argparse.ArgumentParser(
      prog='hello.py',
      description='argparse 빠른 시작 예제'
  )

  parser.add_argument(
      'fname',  # 위치 인자
      help='인사할 사람 이름 (positional argument)'
  )

  parser.add_argument(
      'lname',  # 위치 인자
      help='인사할 사람 성 (positional argument)'
  )

  args = parser.parse_args()
  print(f"Hello, {args.fname} {args.lname}!")


if __name__ == "__main__":
  main()
