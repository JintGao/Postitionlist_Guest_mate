#todo: 1.產生圖片   2.做成LINE機器人 input: 客戶編號,位數 txt , output: 文字 + 圖片


# [桌號,位數]
Postitionlist = [
    ['R03', 4],
    ['R02', 4],
    ['R12', 2]

]

# [客人編號,位數]
guest = [
    [0, 4],
    [1, 2],
    [2, 4]
]

# [桌號,客人編號]
# result = [
#     ['R03', 0],
#     ['R02', 2],
#     ['R12', 1]
# ]


def ResultCompute():

    result = []
    Finish = 0
    Flag = 0

    while Finish == 0:

        for p in Postitionlist:
            for g in guest:
                #客人人數 剛好等於 座位的話
                if g[1] == p[1]:
                    result.append([p[0],g[0]])
                    Postitionlist.remove(p)
                    guest.remove(g)
                    Flag = 1
                    break

                #如果顧客全都巡迴過一遍但沒有成功配對的話
                elif g == guest[len(guest)-1]:
                    result.append([p[0],g[0]])
                    Postitionlist.remove(p)
                    guest.remove(g)
                    Flag = 1
                    break


            if Flag == 1:
                Flag = 0

                #已經把座位都填完了
                if len(Postitionlist) == 0 :
                    Finish = 1
                break

    result2 = result

if __name__ == '__main__':
    ResultCompute()

