from automator import Automator
from target import TargetType

if __name__ == '__main__':
    # 声明货物要移动到的建筑 ID 。
    targets = {
        TargetType.Chair: 1,
        TargetType.Wood: 8,
        TargetType.Bottle: 4,
        TargetType.Vegetable: 5,
        TargetType.Box: 2,
        TargetType.Food: 7,
        TargetType.Sofa: 3,
        TargetType.Rock: 9,
        TargetType.Book: 5,
        TargetType.Maocao: 7,
        TargetType.Bag: 6,
    }

    # 连接 adb 。
    instance = Automator('emulator-5554', targets)

    # 启动脚本。
    instance.start()
