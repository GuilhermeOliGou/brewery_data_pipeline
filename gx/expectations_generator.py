import great_expectations as gx
from great_expectations.data_context.types.base import DataContextConfig, InMemoryStoreBackendDefaults
import os
import json

class ExpectationsGenerator():
    def __init__(self):
        project_config = DataContextConfig(store_backend_defaults=InMemoryStoreBackendDefaults())
        self.context = gx.data_context.EphemeralDataContext(project_config = project_config)

        self.datasource = 'ephemeral_spark_data_source'
        self.data_asset = 'ephemeral_spark_data_asset'

    def generate_dataframe_expectations(self, df, file_name):
        datasource = self.context.sources.add_or_update_spark(name=self.datasource)
        data_asset = datasource.add_dataframe_asset(name=self.data_asset, dataframe=df)
        batch_request = data_asset.build_batch_request()

        data_assistant_result = self.context.assistants.onboarding.run(batch_request=batch_request)

        expectation_suite = data_assistant_result.get_expectation_suite(expectation_suite_name="ephemeral_expectation_suite")
        suite_dict = expectation_suite.to_raw_dict()
        expectations = [{'expectation_type':expectation['_expectation_type'], 'kwargs':expectation['_kwargs']} for expectation in suite_dict['expectatios']]

        output_file_path = os.path.join('expectations', file_name)
        directory = os.path.dirname(output_file_path)

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(output_file_path, "w") as file:
                json.dump(expectations, file, indent=4)