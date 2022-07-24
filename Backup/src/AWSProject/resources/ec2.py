class EC2:

    def __init__(self, account_id, resource):
        self.resource = resource
        self.account_id = account_id

    def create_instances(self, ami_image_id):

        try:
            response = self.resource.create_instances(
                ImageId=ami_image_id,
                MinCount=1,
                MaxCount=1,
            )
            print("Successfully created EC2 instance")
        except NameError:
            print("Error occurred when creating EC2 instances")
