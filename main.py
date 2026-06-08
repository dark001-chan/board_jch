from board_dao import *

board_dao = BoardDAO()

#커넥션 테스트
board_dao.get_connection()

while True:
    print("="*40)
    print("1.목록 2.등록 3.내용 4.삭제 5.검색 6.수정 0.종료")
    print("="*40)
    menu=input("선택 > ")
    if menu == "0":
        break
    elif menu == "1": # 게시판 select * from board
        boards=board_dao.select_all()
        print(boards)
        for board in boards:
            print(board[0],
                  board[1],
                  board[2],
                  board[3])
    elif menu == "2":
        title =input("제목 : ")
        content = input("내용 : ")
        writer = input("작성자 : ")
        board_dao.insert_board(
            title,
            content,
            writer
        )
        print("등록 완료")
    elif menu == "3":
        num = input("번호 : ")
        board = board_dao.select_one(num)
        if board:
            print()
            print("번호 : ",board[0])
            print("제목 : ",board[1])
            print("내용 : ",board[2])
            print("작성자 : ",board[3])
            print("작성일 : ",board[4])
    elif menu == "4":
        num = input("삭제 번호 : ")
        board_dao.delete_board(num)
        print("삭제 완료")
    elif menu=="5":
        keyword=input("검색어 입력 > ")
        boards=board_dao.search(keyword)
        print("[검색 결과]")
        for board in boards:
            print(
                board[0],
                board[1],
                board[2],
                board[3]
            )
    elif menu=="6":
        board_id=input("수정할 게시글 번호 입력 > ")
        board=board_dao.select_one(board_id)
        if board is None:
            print("해당 번호의 게시글이 없습니다.")
        else:
            print("[기존 게시글]")
            print("번호: ",board[0])
            print("제목: ",board[1])
            print("작성자: ",board[2])
            print("내용: ",board[3])

            new_title=input("새 제목 입력 > ")
            new_content=input("새 내용 입력 > ")
            result=board_dao.update(board_id,new_title,new_content)
            if result>0:
                print("게시글이 수정되었습니다.")
            else:
                print("수정에 실패했습니다.")
        
    
print("게시판 종료")