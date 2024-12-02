print("Sinh vien:Nguyễn Danh Ánh")
print("Mssv:235752021610023")
import math

def move_robot(pos, direction, steps):
    """Di chuyển robot theo hướng và số bước cho trước.

    Args:
        pos: Vị trí hiện tại của robot.
        direction: Hướng di chuyển (UP, DOWN, LEFT, RIGHT).
        steps: Số bước di chuyển.
    """
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        print("Hướng di chuyển không hợp lệ.")

def calculate_distance(pos):
    """Tính khoảng cách Euclidean từ vị trí hiện tại đến gốc tọa độ.

    Args:
        pos: Vị trí hiện tại của robot.

    Returns:
        Khoảng cách Euclidean.
    """
    return int(round(math.sqrt(pos[1]**2 + pos[0]**2)))

if __name__ == "__main__":
    pos = [0, 0]

    while True:
        s = input("Nhập lệnh di chuyển (ví dụ: UP 5): ")
        if not s:
            break

        try:
            direction, steps = s.split()
            steps = int(steps)
            if direction not in ["UP", "DOWN", "LEFT", "RIGHT"]:
                print("Hướng di chuyển không hợp lệ.")
                continue
        except ValueError:
            print("Dữ liệu đầu vào không hợp lệ.")
            continue

        move_robot(pos, direction, steps)

    distance = calculate_distance(pos)
    print("Khoảng cách đến vị trí ban đầu:", distance)
