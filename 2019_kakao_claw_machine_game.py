def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        for doll in board:
            if doll[i - 1] != 0:
                if basket == []:
                    basket.append(doll[i - 1])
                    doll[i - 1] = 0
                else:
                    if basket[-1] == doll[i - 1]:
                        basket.pop()
                        doll[i - 1] = 0
                        answer += 2
                    else:
                        basket.append(doll[i - 1])
                        doll[i - 1] = 0
                break
    
    return answer

    '''
    def solution(board, moves):
        stacklist = []
        answer = 0

        for i in moves:
            for j in range(len(board)):
                if board[j][i - 1] != 0:
                    stacklist.appen(board[j][i - 1])
                    board[j][i - 1] = 0

                    if len(stacklist) > 1:
                        if stacklist[-1] == stacklist[-2]:
                            stacklist.pop(-1)
                            stacklist.pop(-1)
                            answer += 2
                    break
                
        return answer
    '''

    '''
    def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a
    '''