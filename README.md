# Thư viện cần thiết
- pygame
- PyOpenGL
- numpy
- json

Người dùng có thể tự cài đặt các thư viện trên, hoặc đơn giản hơn có thể dùng dòng lệnh này trên Command Line
```
$ pip install -r requirements.txt
```
# Chạy chương trình
Chúng ta chạy chương trình bằng cách chạy dòng lệnh này trên Command Line
```
$ python run.py number_of_level play_or_algorithm
```
Trong đó
- number_of_level: số thứ tự của màn chơi (nếu nhỏ hơn 10 thì nhập 01, 02, ...)
- play_or_algorithm: chọn một trong
    - play: chúng ta sẽ tự chơi
    - bfs: giải màn chơi bằng thuật toán BFS
    - astar: giải màn chơi bằng thuật toán Astar Pathfinding
    - mcts: giải màn chơi bằng thuật toán Monte Carlo Tree Search