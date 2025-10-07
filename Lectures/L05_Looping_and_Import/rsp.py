"""
가위바위보 게임 모듈
Rock-Paper-Scissors Game Module
"""

import random


class RPSGame:
  """가위바위보 게임 클래스"""

  def __init__(self):
    """게임 초기화"""
    self.choices = ['가위', '바위', '보']
    self.wins = 0
    self.losses = 0
    self.ties = 0

  def get_computer_choice(self):
    """
    컴퓨터의 선택을 반환
    random.choice()를 사용하여 랜덤 선택
    """
    return random.choice(self.choices)

  def determine_winner(self, user, computer):
    """
    승부 판정

    Args:
        user (str): 사용자의 선택
        computer (str): 컴퓨터의 선택

    Returns:
        str: 게임 결과 메시지
    """
    if user == computer:
      self.ties += 1
      return "비겼습니다!"
    elif (user == '가위' and computer == '보') or \
         (user == '바위' and computer == '가위') or \
         (user == '보' and computer == '바위'):
      self.wins += 1
      return "당신이 이겼습니다!"
    else:
      self.losses += 1
      return "컴퓨터가 이겼습니다!"

  def is_valid_choice(self, choice):
    """
    유효한 선택인지 확인

    Args:
        choice (str): 사용자 입력

    Returns:
        bool: 유효 여부
    """
    return choice in self.choices

  def get_statistics(self):
    """
    현재 게임 통계 반환

    Returns:
        dict: 승/패/무 통계
    """
    return {
        'wins': self.wins,
        'losses': self.losses,
        'ties': self.ties,
        'total': self.wins + self.losses + self.ties
    }

  def print_statistics(self):
    """현재 게임 통계 출력"""
    stats = self.get_statistics()
    print(
        f"현재 전적 - 승: {stats['wins']}, 패: {stats['losses']}, 무: {stats['ties']}")

  def reset_statistics(self):
    """게임 통계 초기화"""
    self.wins = 0
    self.losses = 0
    self.ties = 0


def play_game():
  """메인 게임 실행 함수"""
  game = RPSGame()

  print("=== 가위바위보 게임 ===")
  print("가위, 바위, 보 중 하나를 입력하세요.")
  print("게임을 종료하려면 'q'를 입력하세요.\n")

  while True:
    # 사용자 입력
    user_choice = input("당신의 선택: ").strip()

    # 종료 조건
    if user_choice == 'q':
      print("\n=== 게임 종료 ===")
      stats = game.get_statistics()
      print(f"승: {stats['wins']}, 패: {stats['losses']}, 무: {stats['ties']}")
      print("게임을 종료합니다. 감사합니다!")
      break

    # 유효한 입력인지 확인
    if not game.is_valid_choice(user_choice):
      print("잘못된 입력입니다. '가위', '바위', '보' 중 하나를 입력하세요.\n")
      continue

    # 컴퓨터의 선택 (random.choice 사용)
    computer_choice = game.get_computer_choice()

    # 결과 출력
    print(f"컴퓨터의 선택: {computer_choice}")

    # 승부 판정
    result = game.determine_winner(user_choice, computer_choice)
    print(result)

    # 통계 출력
    game.print_statistics()
    print()


if __name__ == "__main__":
  play_game()
