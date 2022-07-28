import boto3
from quicksight import quicksight
from quicksight import cfnresponse


#####################################################
# Create the required clients and resources         #
#####################################################
quicksight_client = boto3.client('quicksight')


def refresh_spice_data(account_id):
    quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
    quicksightClass.refresh_spice_data()


def refresh_cost_spice_data(account_id):
    quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
    quicksightClass.refresh_cost_spice_data()


def update_data_set(account_id):
    quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
    quicksightClass.update_data_set()


def cost_update_data_set(account_id):
    quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
    quicksightClass.cost_update_data_set()


def update_analysis(account_id):
    quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
    quicksightClass.update_analysis()


def update_dashboard(account_id):
    quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
    quicksightClass.update_dashboard()


def lambda_handler(event, context):

    print("Welcome to create your Quicksight Backup Dashboard ")
    account_id = context.invoked_function_arn.split(":")[4]

    #####################################################
    # Set Quicksight Template Permission                #
    #####################################################

    refresh_spice_data(account_id)
    refresh_cost_spice_data(account_id)
    update_data_set(account_id)
    cost_update_data_set(account_id)
    update_analysis(account_id)
    update_dashboard(account_id)

    responseData = {}
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)

    return
