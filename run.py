import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./Temps -o ./AllureReports --clean")
    print("allure报告已生成")