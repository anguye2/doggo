from .Model import Model
from datetime import datetime
import boto3

class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb", region_name="us-east-1")
        self.table = self.resource.Table('favorite')
        try:
            self.table.load()
        except:
            self.resource.create_table(
                TableName="favorite",
                KeySchema=[
                    { "AttributeName": "name", "KeyType": "HASH" },
                ],
                AttributeDefinitions=[
                    { "AttributeName": "name", "AttributeType": "S" },
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 1, "WriteCapacityUnits": 1
                }
            )

    def select(self):
        try:
            gbentries = self.table.scan()
        except Exception as e:
            return([['scan failed', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])

        return([ [f['id'], f['name'], f['weight'], f['height'], f['bred_for'], f['breed_group'], f['life_span'], 
        f['temperament'], f['origin'], f['date_submitted'], f['image']] for f in gbentries['Items']])

    def insert(self, info):
        gbitem = {
            'id' : info[0],
            'name': info[1],
            'weight' : info[2],
            'height': info[3],
            'bred_for': info[4],
            'breed_group': info[5],
            'life_span': info[6],
            'temperament': info[7],
            'origin': info[8],
            'date_submitted': str(datetime.today()),
            'image': info[9]
            }

        try:
            self.table.put_item(Item=gbitem)
        except:
            return False

        return True