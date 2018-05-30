# 최종 수정: 2018-05-30
# 수정자: 20307 박진철

import re

def checkMulDiv(text): #곱하기/나누기 연산
    rule = re.compile('([0-9]+[.0-9]*[0-9]*)(곱하기|나누기)([0-9]+[,0-9]*[0-9]*)')
    searchResult = rule.search(text)

    if searchResult == None:
        return text.strip()
    if searchResult.group(2) == '곱하기':
        calc = float(searchResult.group(1)) * float(searchResult.group(3))
    elif searchResult.group(2) == '나누기':
        try:
            calc = float(searchResult.group(1)) / float(searchResult.group(3))
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
            return

    result = text[:searchResult.span()[0]] + str(calc) + text[searchResult.span()[1]:]
    return checkMulDiv(result)

def checkPluMin(text): #더하기/빼기 연산
    rule = re.compile('([0-9]+[.0-9]*[0-9]*)(더하기|빼기)([0-9]+[.0-9]*[0-9]*)')
    searchResult = rule.search(text)

    if searchResult == None:
        return text.strip()
    if searchResult.group(2) == '더하기':
        calc = float(searchResult.group(1)) + float(searchResult.group(3))
    elif searchResult.group(2) == '빼기':
        calc = float(searchResult.group(1)) - float(searchResult.group(3))

    result = text[:searchResult.span()[0]] + str(calc) + text[searchResult.span()[1]:]
    return checkPluMin(result)

def checkMath(text): #식 맞는지 확인 여부, 나중에 제대로 수정(ast 이용)
    return True

def doCalc(text):
    text = text.replace(' ', '')
    text = checkMulDiv(text)        #곱하기 계열 먼저 진행
    if text == None:
        return
    text = checkPluMin(text)        #그 후 더하기 계열 진행
    if float(text) % 1.0 != 0:
        return float(text)
    else:
        return int(text[:text.find('.')])

#입력 형식: a 더하기|빼기|곱하기|나누기 b ... (띄어쓰기 상관X)        
def main():
    while True:
        try:
            text = input("> ")
            temp = doCalc(text)
            if temp != None:
                print(temp)
            else:
                pass
        except:
            print("계산기 형식으로 입력해주세요.")
            print("형식: A 더하기/빼기/곱하기/나누기 B ...", end='\n\n')
        
if __name__ == "__main__":
    main()

