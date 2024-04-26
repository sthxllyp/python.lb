def main():
    num = int(input("Введите количество оценок: "))
    ocs = []
    for i in range(num):
        oc = float(input("Введите оценку {}: ".format(i + 1)))
        ocs.append(oc)
    print("Оценки в том же порядке:")
    for oc in ocs:
        print(ocs)
    sr_oc = sum(ocs) / len(ocs)
    print("Средняя оценка:", sr_oc)
if __name__ == "__main__":
    main()