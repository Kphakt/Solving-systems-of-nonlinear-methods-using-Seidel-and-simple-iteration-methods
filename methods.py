import math
class Methods():
    def __init__(self, eq1, eq2, iterations, x, y, epsilon):
        self.eq1 = eq1
        self.eq2 = eq2
        self.iterations = iterations
        self.x = x
        self.y = y
        self.epsilon = epsilon
        self.answer = ''

    def method(self):
        self.answer = self.seidel()
        self.answer += self.mpi()

    def seidel(self):
        x1 = self.x
        y1 = self.y
        iteration = 0
        ans = " " * 50 + "Метод Зейделя \n"
        delta = self.epsilon * 2
        while delta > self.epsilon and iteration <= self.iterations:
            iteration += 1
            x0, y0 = x1, y1
            x1 = self.eq1(x0, y0)
            y1 = self.eq2(x1, y0)
            delta = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
            ans += f"Итерация: {iteration} x = {x1} y = {y1} \n"
        ans += " " * 50 + "Метод простых итераций \n"
        return ans

    def mpi(self):
        x1 = self.x
        y1 = self.y
        iteration = 0
        delta = self.epsilon * 2
        ans = ''
        while delta > self.epsilon and iteration <= self.iterations:
            iteration += 1
            x0, y0 = x1, y1
            x1 = self.eq1(x0, y0)
            y1 = self.eq2(x0, y0)
            delta = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
            ans += f"Итерация: {iteration} x = {x1} y = {y1} \n"
        return ans
