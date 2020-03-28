import sys
import speech_recognition as sr
import vlc
import time
import webbrowser

cnt = 0
 
while True:
 
    # ID, PW 입력받기
    id = input('ID 입력:')
    pw = input('PW 입력:')
 
    # ID 와 PW 일치하는지 비교
    if id=='amadeus' and pw=='amadeus' or id=='jm0730' and pw=='jm0730':
        print("login 中")
        time.sleep(2)
        print('로그인 성공')
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                    print('HELLO')
                    print('한국어로 말하세요')
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new('hello.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(1)
                    audio = r.listen(source)
                    # 크리스 목소리 파일 실행


            try:
                print("당신은 말했습니다." + r.recognize_google(audio, language="ko-KR"))

                if '안녕' in r.recognize_google(audio, language="ko-KR"):
                    print ("처음뵙겠습니다. 마키세 크리스 입니다.")
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new('nice_to.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(4)
                    continue

                if r.recognize_google(audio, language="ko-KR") == "하츠네미쿠 노래 틀어 줘":
                    webbrowser.open("https://www.nicovideo.jp/watch/sm1097445")

                if r.recognize_google(audio, language="ko-KR") == "타임머신":
                    print ("타임머신 입니까?")
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new('tm_you_said.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(4)
                    continue

                if r.recognize_google(audio, language="ko-KR") == "크리스티나":
                    print ("크리스티나?")
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new('christina.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(4)
                    continue


                if r.recognize_google(audio, language="ko-KR") == "무엇을 도와줄 수 있니":
                    print ("무엇이든 물어봐 주세요. 가능한 범위에서 대답해드릴테니까요.")
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new('ask_me_whatever.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(5)
                    continue

                if r.recognize_google(audio, language="ko-KR") == "타임머신은 가능할까":
                    print ("그렇네요. 결론부터 이야기하자면 타임머신은 가능하지 않아...")
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new('tm_not_possible.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(6)
                    continue

                if r.recognize_google(audio, language="ko-KR") == "꺼져":
                    print ("하지만 거절한다.")
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new('daga_kotowaru.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(4)
                    continue
                
                if '슈타인즈 게이트 망' in r.recognize_google(audio, language="ko-KR"):
                    print ("하지만 거절한다.")
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new('daga_kotowaru.mp3')
                    player.set_media(media)
                    player.play()
                    time.sleep(4)
                    continue

                if r.recognize_google(audio, language="ko-KR") == "소스코드":
                    webbrowser.open("www.amadeus.coo.kr")
                
                if r.recognize_google(audio, language="ko-KR") == "검색":
                        print ("무엇을 검색할까요?")
                        time. sleep(1)
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            audio = r.listen(source)
                            print(r.recognize_google(audio, language="ko-KR") + "\n이것을 검색할게요.")
                            time. sleep(1)
                            webbrowser.open("http://www.google.com/search?client=chrome&rls=en-us&q=" + r.recognize_google(audio, language="ko-KR") + "&ie=UTF-8&oe=UTF-8")
                            break
                    



                else:
                      webbrowser.open("http://www.google.com/search?client=chrome&rls=en-us&q=" + r.recognize_google(audio, language="ko-KR") + "&ie=UTF-8&oe=UTF-8")
                      break


            except sr.UnknownValueError:
                print("질문을 이해할 수 없습니다.")
                instance = vlc.Instance()
                player = instance.media_player_new()
                media = instance.media_new('sorry.mp3')
                player.set_media(media)
                player.play()
                time.sleep(4)
                continue


    else:
        cnt = cnt + 1
        print('로그인 {}회 실패'.format(cnt))
 
    if cnt >= 3:       
        print('보안을 위해 로그인 시스템을 종료합니다!')
        break
