# Tkinter 라이브러리 호출
import tkinter as tk
# Time 라이브러리 호출
import time

# 넣고 싶은 번호 리스트(순서대로)
num_list = ['7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', '=']

# 넣고 싶은 연산자 리스트(순서대로)
op_list = ['*', '/',
           '+', '-',
           '(', ')',
           'C', 'AC']

# num_list와 op_list를 합친 key_list 생성
key_list = num_list + op_list
# key_list에서 'AC', 'C', '='를 제거
key_list.remove('AC')
key_list.remove('C')
key_list.remove('=')

# 키보드 입력시 실행 함수
def inputKey(key):
    # display_entry를 입력가능한 상태로 전환
    display_entry.configure(state=tk.NORMAL)

    # 입력된 키가 key_list에 있는 키인 경우
    if key.char in key_list:
        # display_entry에 입력된 키 값을 추가
        display_entry.insert(tk.END, key.char)
    # 입력된 키가 '=' 또는 엔터인 경우
    elif key.char == '=' or key.char == '\r':
        try:
            # display_entry 수식을 계산
            result = str(round(eval(display_entry.get()), 2))
            # display_entry 내용 지우기
            display_entry.delete(0, tk.END)
            # display_entry에 결과값 출력
            display_entry.insert(tk.END, result)
        # 계산이 되지 않는 수식인 경우 1초 동안 '오류' 표시
        except:
            # 현재 display_entry 수식을 임시로 저장
            result_tmp = display_entry.get()
            # display_entry 내용 지우기
            display_entry.delete(0, tk.END)
            # 안내 메시지 표출
            display_entry.insert(0, "계산할 수 없는 수식입니다")
            display_entry.update()
            # 1초간 정지
            time.sleep(1)
            # display_entry 내용 지우기
            display_entry.delete(0, tk.END)
            # 임시로 저장해두었던 수식 다시 보여주기
            display_entry.insert(0, result_tmp)
    # 입력된 키가 'C'인 경우
    elif key.char == 'C' or key.char == 'c':
        # display_entry 내용 삭제
        display_entry.delete(0, tk.END)
    # 입력된 키가 'A'인 경우
    elif key.char == 'A' or key.char == 'a':
        # display_entry 내용 삭제
        display_entry.delete(0, tk.END)

    # display_entry를 입력불가능한 상태로 전환
    display_entry.configure(state="readonly")

# 버튼 클릭시 실행 함수
def buttonClick(key):
    # display_entry를 입력가능한 상태로 전환
    display_entry.configure(state=tk.NORMAL)

    # '=' 버튼을 누른 경우
    if key == '=':
        try:
            # display_entry 수식을 계산
            result = str(round(eval(display_entry.get()), 2))
            # display_entry 내용 지우기
            display_entry.delete(0, tk.END)
            # display_entry에 결과값 출력
            display_entry.insert(tk.END, result)
        # 계산이 되지 않는 수식인 경우 1초 동안 '오류' 표시
        except:
            # 현재 display_entry 수식을 임시로 저장
            result_tmp = display_entry.get()
            # display_entry 내용 지우기
            display_entry.delete(0, tk.END)
            # 안내 메시지 표출
            display_entry.insert(0, "계산할 수 없는 수식입니다")
            display_entry.update()
            # 1초간 정지
            time.sleep(1)
            # display_entry 내용 지우기
            display_entry.delete(0, tk.END)
            # 임시로 저장해두었던 수식 다시 보여주기
            display_entry.insert(0, result_tmp)
    # 'C' 버튼을 누른 경우
    elif key == 'C':
        # display_entry 내용 삭제
        display_entry.delete(0, tk.END)
    # 'AC' 버튼을 누른 경우
    elif key == 'AC':
        # display_entry 내용 삭제
        display_entry.delete(0, tk.END)
    # '=', 'C', 'AC' 외의 버튼을 누른 경우
    else:
        # 눌러진 버튼 텍스트 값을 디스플레이에 추가
        display_entry.insert(tk.END, key)

    # display_entry를 입력불가능한 상태로 전환
    display_entry.configure(state="readonly")


# 메인 윈도우 생성
main_win = tk.Tk()
# 메인 윈도우 이름 설정
main_win.title("CB_Calc")
# 메인 윈도우를 항상 위로
main_win.attributes("-topmost", True)
# focus-on 상태에서 키를 누르면 inputKey 함수 실행
main_win.bind("<Key>", inputKey)

# 디스플레이 엔트리 생성 및 배치
# columnspan=2 추가
display_entry = tk.Entry(main_win, width=45, readonlybackground="light green", bg="light green")
display_entry.grid(row=0, column=0, columnspan=2)

# display_entry를 입력불가능한 상태로 전환
display_entry.configure(state="readonly")

# 번호 프레임 생성 및 배치
num_frame = tk.Frame(main_win)
num_frame.grid(row=1, column=0, sticky='W')

# 반복문에서 사용할 임시 변수
row_tmp = 0
col_tmp = 0

# num_text는 num_list 값을 순서대로 갖게 된다
for num_text in num_list:

    # 버튼을 눌렀을 때 cmd_tmp가 실행된다
    def cmd_tmp(key_input=num_text):
        # num_text 값을 넘겨주면서 button_click을 호출
        buttonClick(key_input)

    # Button을 생성하고, row_tmp, col_tmp 위치에 배치
    num_button = tk.Button(num_frame, text=num_text, width=5, command=cmd_tmp)
    num_button.grid(row=row_tmp, column=col_tmp)

    # 버튼을 배치했으면 다음 칸으로 이동하도록 col_tmp에 1 더한다
    col_tmp = col_tmp + 1
    # col_tmp가 2보다 크다면 다음 줄로 이동한다
    if col_tmp > 2:
        col_tmp = 0
        row_tmp = row_tmp + 1

# 연산자 프레임 생성 및 배치
op_frame = tk.Frame(main_win)
op_frame.grid(row=1, column=1, sticky='E')

# 반복문에서 사용할 임시 변수
row_tmp = 0
col_tmp = 0

# op_text는 op_list 값을 순서대로 갖게 된다
for op_text in op_list:

    # 버튼을 눌렀을 때 cmd_tmp가 실행된다
    def cmd_tmp(key_input=op_text):
        # op_text 값을 넘겨주면서 button_click을 호출
        buttonClick(key_input)

    # Button을 생성하고, row_tmp, col_tmp 위치에 배치
    op_button = tk.Button(op_frame, text=op_text, width=5, command=cmd_tmp)
    op_button.grid(row=row_tmp, column=col_tmp)

    # 버튼을 배치했으면 다음 칸으로 이동하도록 col_tmp에 1 더한다
    col_tmp = col_tmp + 1
    # col_tmp가 1보다 크다면 다음 줄로 이동한다
    if col_tmp > 1:
        col_tmp = 0
        row_tmp = row_tmp + 1

# 메인 윈도우 반복 명령
main_win.mainloop()