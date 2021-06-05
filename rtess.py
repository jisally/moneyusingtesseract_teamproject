#tesseract 사용
#국민은행 카드사용내용 picture1&2
#카드 사용내용 문자 이미지를 tesseract를 사용하여 텍스트로 변환
#변환한 것을 해당 카테고리, 몇월인지 선택 후 txt파일에 저장
#txt파일에 금액만 남기고 삭제
#월별 총 사용금액 합계 계산
#소창 팀플에 사용하려했으나 다른 조원 컴퓨터에서 tesseract가 실행되지 않아서 사용못함->tesseract말고 은행에서 제공하는 엑셀파일 이용하여 가계부 프로그램 제작 예상

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string('C:\\Temp\picture1.jpg', lang='kor+eng', config='-c preserve_interword_spaces=1--psm4'))


a=pytesseract.image_to_string('C:\\Temp\picture1.jpg', lang='kor+eng', config='-c preserve_interword_spaces=1--psm4')


f=open("test1.txt","a")
f.write(a)
f.close()


f=open("eat_cost.txt", "w")
f=open("mart_cost.txt", "w")
f=open("phone_cost.txt", "w")
f=open("cong_cost.txt", "w")
f=open("house_cost.txt", "w")
f=open("fash_cost.txt", "w")



f=open("test1.txt", "r")

line1=f.readline()
line2=f.readline()
line3=f.readline()
line4=f.readline()
line5=f.readline()
line6=f.readline()
line7=f.readline()

characters="원"

for x in range(len(characters)):
    line7=line7.replace(characters[x], "")
    
characters=","

for x in range(len(characters)):
    line7=line7.replace(characters[x], "")
print(line7)


p2=int(input("몇 월인가요?\n"))


if p2==1:
    str='jan_cost.txt'
elif p2==2:
    str='feb_cost.txt'
elif p2==3:
    str='mar_cost.txt'
elif p2==4:
    str='apr_cost.txt'
elif p2==5:
    str='may_cost.txt'
elif p2==6:
    str='jun_cost.txt'
elif p2==7:
    str='jul_cost.txt'
elif p2==8:
    str='aug_cost.txt'
elif p2==9:
    str='sep_cost.txt'
elif p2==10:
    str='oct_cost.txt'
elif p2==11:
    str='nov_cost.txt'
else:
    str='dec_cost.txt'


f=open(str, "a")
f.write(line7)
f.close()


p=int(input("카테고리는 무엇인가요? \n1.식비\n2.마트\n3.통신\n4.경조사/회비\n5.주택청약\n6. 패션/미용\n"))

if p==1:
    f=open("eat_cost.txt", "a")
    f.write(line7)
    f.close()
elif p==2:
    f=open("mart_cost.txt", "a")
    f.write(line7)
    f.close()
elif p==3:
    f=open("phone_cost.txt", "a")
    f.write(line7)
    f.close()
elif p==4:
    f=open("cong_cost.txt", "a")
    f.write(line7)
    f.close()
elif p==5:
    f=open("house_cost.txt", "a")
    f.write(line7)
    f.close()
else:
    f=open("fash_cost.txt", "a")
    f.write(line7)
    f.close()









print(pytesseract.image_to_string('C:\\Temp\picture2.jpg', lang='kor+eng', config='-c preserve_interword_spaces=1--psm4'))
b=pytesseract.image_to_string('C:\\Temp\picture2.jpg', lang='kor+eng', config='-c preserve_interword_spaces=1--psm4')

f=open("test2.txt","w")
f.write(b)
f.close()

                  
f=open("test2.txt", "r")

line1=f.readline()
line2=f.readline()
line3=f.readline()
line4=f.readline()
line5=f.readline()
line6=f.readline()
line7=f.readline()

characters="원"

for x in range(len(characters)):
    line7=line7.replace(characters[x], "")

characters=","

for x in range(len(characters)):
    line7=line7.replace(characters[x], "")
    
print(line7)

p2=int(input("몇 월인가요?\n"))


if p2==1:
    str='jan_cost.txt'
elif p2==2:
    str='feb_cost.txt'
elif p2==3:
    str='mar_cost.txt'
elif p2==4:
    str='apr_cost.txt'
elif p2==5:
    str='may_cost.txt'
elif p2==6:
    str='jun_cost.txt'
elif p2==7:
    str='jul_cost.txt'
elif p2==8:
    str='aug_cost.txt'
elif p2==9:
    str='sep_cost.txt'
elif p2==10:
    str='oct_cost.txt'
elif p2==11:
    str='nov_cost.txt'
else:
    str='dec_cost.txt'


f=open(str, "a")
f.write(line7)
f.close()

p=int(input("카테고리는 무엇인가요? \n1.식비\n2.마트\n3.통신\n4.경조사/회비\n5.주택청약\n6. 패션/미용\n"))

if p==1:
    f=open("eat_cost.txt", "a")
    f.write(line7)
    f.close()
elif p==2:
    f=open("mart_cost.txt", "a")
    f.write(line7)
    f.close()
elif p==3:
    f=open("phone_cost.txt", "a")
    f.write(line7)
    f.close()
elif p==4:
    f=open("cong_cost.txt", "a")
    f.write(line7)
    f.close()
elif p==5:
    f=open("house_cost.txt", "a")
    f.write(line7)
    f.close()
else:
    f=open("fash_cost.txt", "a")
    f.write(line7)
    f.close()




f.close()

print("카테고리별 사용 금액은")
print("1. 식비")
f=open("eat_cost.txt", "r")
text=f.read()
print(text)
print("2. 마트")
f=open("mart_cost.txt", "r")
text=f.read()
print(text)
print("3. 통신")
f=open("phone_cost.txt", "r")
text=f.read()
print(text)
print("4. 경조사/회비")
f=open("cong_cost.txt", "r")
text=f.read()
print(text)
print("5. 주택청약")
f=open("house_cost.txt", "r")
text=f.read()
print(text)
print("6. 패션/미용")
f=open("fash_cost.txt", "r")
text=f.read()
print(text)
print("입니다.")


f=open("may_cost.txt", "r")
lines=f.read().splitlines()
data=[]
sum=0

for line in lines:
    data.append(line)

for k in range(0, len(data)):
    sum+=int(data[k])

print(data)
print("5월 총 사용금액은", sum, "원 입니다.\n")
