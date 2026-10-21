from database.database import get_connection

class CampaignManager:
    #Create a campaign and return its ID
    def create_campaign(self, name):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO campaigns (name)
                VALUES (?)
                """,
                (name,)
            )

            return cursor.lastrowid