import numpy as np


def main():
    D = np.zeros((4, 4), float)
    R = np.zeros((4, 4), float)
    L = np.zeros((4, 4), float)
    A = [[4.855, 1.239, 0.272, 0.258],
         [1.491, 4.954, 0.124, 0.236],
         [0.456, 0.285, 4.354, 0.254],
         [0.412, 0.335, 0.158, 2.874]]

    e = input("Точность вычислений: ")
    o = int(input("Количество знаков после запятой: "))

    for i in range(len(A)):  # условие сходимости
        flag = False
        summ = 0
        for j in range(len(A[i])):
            summ = summ + A[i][j]
            if i == j:
                curr = A[i][j]
            if j == 3:
                if curr > (summ - curr):
                    flag = True
                if not flag:
                    print("Условие сходимости не выполнено в строке", i)
                    exit()
                else:
                    print("Условие сходимости выполнено в строке", i)

    for i in range(len(A)):  # создание D
        for j in range(len(A[i])):
            if i != j:
                D[i][j] = 0
            else:
                D[i][j] = A[i][j]

    for i in range(len(A)):  # создание L
        for j in range(len(A[i])):
            if i <= j:
                L[i][j] = 0
            else:
                L[i][j] = A[i][j]

    for i in range(len(A)):  # создание R
        for j in range(len(A[i])):
            if i >= j:
                R[i][j] = 0
            else:
                R[i][j] = A[i][j]
    print("\nИсходная матрица\n", R + L + D)
    B = np.dot((-(np.linalg.inv(D))), L + R)
    print("матрица В\n", B)
    normB = 0
    vecB = []
    for i in range(len(B)):  # создание нормы В
        summ = 0
        for j in range(len(B[i])):
            summ = summ + abs(B[i][j])
            if normB < abs(summ):
                normB = abs(summ)
        vecB.append(abs(summ))

    print("Вектор b ", vecB)
    print("Норма b ", normB)

    x = [0, 0, 0, 0]
    xtmp = [0, 0, 0, 0]

    proverka = ((1 - normB) / normB) * float(e)
    proverka = round(proverka, int(o))
    print("||B|| =", proverka)

    c = [0.2455, 0.0517, 0.1957, 0.2999]

    count = 0
    while abs((round(x[0], int(o)) - round(xtmp[0], int(o)))) > proverka or count == 0:
        for k in range(4):
          xtmp[k] = x[k]

        x[0] = B[0][0] * xtmp[0] + B[0][1] * xtmp[1] + B[0][2] * xtmp[2] + B[0][3] * xtmp[3] + c[0]
        x[1] = B[1][0] * x[0] + B[1][1] * xtmp[1] + B[1][2] * xtmp[2] + B[1][3] * xtmp[3] + c[1]
        x[2] = B[2][0] * x[0] + B[2][1] * x[1] + B[2][2] * xtmp[2] + B[2][3] * xtmp[3] + c[2]
        x[3] = B[3][0] * x[0] + B[3][1] * x[1] + B[3][2] * x[2] + B[3][3] * xtmp[3] + c[3]

        for i in range(4):
            x[i] = round(x[i], o)

        count = count + 1
        print(count, x, "дельта:", x[0], "-", xtmp[0], "=", abs(x[0] - xtmp[0]))


if __name__ == "__main__":
    main()

