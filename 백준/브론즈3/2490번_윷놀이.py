for i in range(3):
    dbt=list(map(int, input().split()))
    if dbt.count(0)==4:
        print("D")
    elif dbt.count(0) == 3:
        print("C")
    elif dbt.count(0) == 2:
        print("B")
    elif dbt.count(0) == 1:
        print("A")
    else:
        print("E")
