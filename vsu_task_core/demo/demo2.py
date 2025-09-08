from vsu_task_core.common.lang import Lang

if __name__ == '__main__':
    string = "value1-value2"
    l, c, r = string.partition("-")
    print(f"{l = }, {c = }, {r = }")

    #lang = Lang("ru")
    #print(f"{lang = }")

