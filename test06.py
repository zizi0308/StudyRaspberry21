
try:
    f = open('./data/readme.txt', mode='r', encoding='utf-8') # 텍스트파일 오픈
    f2 = open('./data/writeme.txt', mode='w', encoding='utf-8') # 작성파일 오픈
    
    line = f.read() # 모든 값들은 read에서 읽음
    while line:
        print(line)
        f2.write(line)
        line = f.read()

    f2.write('\n추가내용 입니다.')
    f.close()   # 오픈 후 무조건 닫기
    f2.close()

    print('파일작성 완료!')

except Exception as e:  # 모든 예외들 중 최상위 에러는 Exception
    print('예외발생 : {0}'.format(e))