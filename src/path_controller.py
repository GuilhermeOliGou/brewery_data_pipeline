import os

class PathController():
    def __init__(self):
        self.base_dir = os.path.join('..','data')
        self.bronze_data_dir = os.path.join(self.base_dir,'bronze_layer')
        self.silver_data_dir = os.path.join(self.base_dir,'silver_layer')
        self.gold_data_dir = os.path.join(self.base_dir,'gold_layer')

    def get_path_for_bronze_layer(self, database, schema, table, file):
        return os.path.join(self.bronze_data_dir, database, schema, table, file)

    def get_path_for_silver_layer(self, database, schema, table):
        return os.path.join(self.silver_data_dir, database, schema, table)

    def get_path_for_gold_layer(self, database, schema, table):
        return os.path.join(self.gold_data_dir, database, schema, table)

