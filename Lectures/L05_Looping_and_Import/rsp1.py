import random

# 게임 선택지
CHOICES = ['가위', '바위', '보']


def get_computer_choice():
  """
  컴퓨터의 선택을 반환
  random.choice()를 사용하여 랜덤 선택

  Returns:
      str: 컴퓨터의 선택 ('가위', '바위', '보' 중 하나)
  """
  return random.choice(CHOICES)


def determine_winner(user, computer):
  """
  승부 판정

  Args:
      user (str): 사용자의 선택
      computer (str): 컴퓨터의 선택

  Returns:
      str: 게임 결과 ('win', 'lose', 'tie')
  """
  if user == computer:
    return 'tie'
  elif (user == '가위' and computer == '보') or \
       (user == '바위' and computer == '가위') or \
       (user == '보' and computer == '바위'):
    return 'win'
  else:
    return 'lose'


def is_valid_choice(choice):
  """
  유효한 선택인지 확인

  Args:
      choice (str): 사용자 입력

  Returns:
      bool: 유효 여부
  """
  return choice in CHOICES


def print_result(result):
  """
  게임 결과 출력

  Args:
      result (str): 게임 결과 ('win', 'lose', 'tie')
  """
  if result == 'win':
    print("당신이 이겼습니다!")
  elif result == 'lose':
    print("컴퓨터가 이겼습니다!")
  else:
    print("비겼습니다!")


def play_game():
  """메인 게임 실행 함수"""
  print("=== 가위바위보 게임 ===")
  print("가위, 바위, 보 중 하나를 입력하세요.")
  print("게임을 종료하려면 'q'를 입력하세요.\n")

  # 게임 통계
  wins = 0
  losses = 0
  ties = 0

  # 메인 게임 루프 (while 사용)
  while True:
    # 사용자 입력
    user_choice = input("당신의 선택: ").strip()

    # 종료 조건
    if user_choice == 'q':
      print("\n=== 게임 종료 ===")
      print(f"승: {wins}, 패: {losses}, 무: {ties}")
      print("게임을 종료합니다. 감사합니다!")
      break

    # 유효한 입력인지 확인
    if not is_valid_choice(user_choice):
      print("잘못된 입력입니다. '가위', '바위', '보' 중 하나를 입력하세요.\n")
      continue

    # 컴퓨터의 선택 (random.choice 사용)
    computer_choice = get_computer_choice()
    print(f"컴퓨터의 선택: {computer_choice}")

    # 승부 판정
    result = determine_winner(user_choice, computer_choice)
    print_result(result)

    # 통계 업데이트
    if result == 'win':
      wins += 1
    elif result == 'lose':
      losses += 1
    else:
      ties += 1

    # 현재 통계 출력
    print(f"현재 전적 - 승: {wins}, 패: {losses}, 무: {ties}\n")


# 모듈이 직접 실행될 때만 게임 시작
if __name__ == "__main__":
  play_game()
