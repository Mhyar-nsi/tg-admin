import aiosqlite


class Model():
    
    path = './data/sqlite.db'
    
    
    async def check_user(self, chat_id):
        db = await aiosqlite.connect(self.path)
        cursor = await db.cursor()

        await cursor.execute('''SELECT * FROM user WHERE chat_id = :chat_id''', {'chat_id' , chat_id})
        
        user = await cursor.fetchone()
        
        await db.close()
        return user
        
        
    async def create_user(self, chat_id, full_name, username):
        db = await aiosqlite.connect(self.path)
        
        cursor = await db.cursor()
        
        await cursor.execute('''INSERT INTO user VALUES (
                :chat_id,
                :full_name,
                :username
            )
        ''',  
            {
                'chat_id' : chat_id,
                'full_name' : full_name,
                'username' : username
            }
        )
        
        await db.commit()
        await db.close()