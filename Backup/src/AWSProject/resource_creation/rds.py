import boto3


class RDS:

    def __init__(self, account_id, client):
        self.client = client
        self.account_id = account_id

    def create_db_instance(self, db_instance_class, db_instance_identifier, engine, allocated_storage, master_username, master_password):

        try:
            response = self.client.create_db_instance(
                AllocatedStorage=allocated_storage,
                DBInstanceClass=db_instance_class,
                DBInstanceIdentifier=db_instance_identifier,
                Engine=engine,
                MasterUserPassword=master_username,
                MasterUsername=master_password,
            )
            print("Successfully created RDS instance")
        except NameError:
            print("Error occurred when creating RDS instance")
