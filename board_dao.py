import pymysql

class BoardDAO:
    def __init__(self):
        self.host = "localhost"
        self.user = "board_user"
        self.password = "board1234"
        self.database="board_db"
    def get_connection(self):
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset="utf8mb4" # main.py와 연결
        )
    def insert_board(self,title,content,writer):
        conn=self.get_connection()
        cursor=conn.cursor()
        sql="""
        INSERT INTO board
        (title,content,writer)
        VALUES
        (%s,%s,%s)
        """
        cursor.execute(
            sql,
            (title,content,writer)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def select_all(self):
        conn =self.get_connection()
        cursor =conn.cursor()
        sql = """
        SELECT *
        FROM board
        ORDER BY id DESC
        """

        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

        return result
    def select_one(self,board_id):
        conn = self.get_connection()
        cursor=conn.cursor()
        sql="""
        SELECT *
        FROM board
        WHERE id=%s
        """
        cursor.execute(sql,(board_id,))
        result=cursor.fetchone()
        cursor.close()
        conn.close()
        return result
    def delete_board(self, board_id):
        conn = self.get_connection()
        cursor= conn.cursor()
        sql="""
        DELETE
        FROM board
        WHERE id=%s
        """
        cursor.execute(sql,(board_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("삭제 완료")
    def search(self,keyword):
        conn=self.get_connection()
        cursor=conn.cursor()
        sql="""
        SELECT *
        FROM board
        WHERE title LIKE %s
            OR writer LIKE %s
            OR content LIKE %s
        ORDER BY id DESC
        """
        keyword="%"+keyword+"%"
        cursor.execute(sql,(keyword,keyword,keyword))
        result=cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    def update(self,board_id,title,content):
        conn=self.get_connection()
        cursor=conn.cursor()
        sql="""
        UPDATE board
        SET title=%s,
        content=%s
        WHERE id=%s
        """
        cursor.execute(sql,(title,content,board_id))
        conn.commit()
        row_count=cursor.rowcount
        cursor.close()
        conn.close()
        return row_count