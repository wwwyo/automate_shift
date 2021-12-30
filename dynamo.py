import boto3

class Dynamo:
    def __init__(self, table):
        self.setDynamo(table)

    def getItems(self):
        items = self.table.scan()
        return items['Items']


    def getItem(self, id):
        item = self.table.get_item(Key={'id': id})
        return item['Item']

    def updateItem(self, id):
        res = self.table.update_item(
            Key={
                "id": id
            },
            
        )

    def setDynamo(self,table):
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='local',
            aws_access_key_id='ACCESS_ID',
            aws_secret_access_key='ACCESS_KEY')

        self.table = dynamodb.Table(table)
