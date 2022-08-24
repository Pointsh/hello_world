# # site = "http://naver.com"

# # depl=site.replace("http://","")

# # depl=depl[:depl.index(".")]
# # pwd = depl[:3] + str(len(depl)) + str(depl.count("e")) + "!"

# # print(pwd)


# a,b,c = map(int,input("전화번호를 입력하세요").split("-"))
# print("통신사 : "+str(a).zfill(3))
# print("국번호 : {0}".format(b))
# print("전화번호 : {0}".format(c))


day = "20220819Cloduy"
print("연도 = "+day[0:4])
print("월 = "+day[4:6])
print("일 = "+day[6:8])
print("날씨 = "+day[8:])