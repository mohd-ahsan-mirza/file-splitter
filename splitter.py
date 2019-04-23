import os
from datetime import datetime
class Splitter:
    def __init__(self,filename,row_limit,preserve_headers=False,debug=False):
        self.file = filename
        self.file_name, self.file_extension = extension = os.path.splitext(self.file)
        self.row_limit = int(row_limit)
        self.preserve_headers = preserve_headers
        self.debug = debug
        self._data = []
        self._load()
        self._folder_name = ""
        if self.can_split():
            self._folder_name = self._generate_folder()
    def _load(self):
        data_file = open(self.file,"r")
        self._data = data_file.readlines()
        data_file.close()
        self._debug_handler("Data file that got loaded","\n".join(self._data))
    def _debug_handler(self,message,data):
        if(self.debug):
            print(message)
            print("---------------------")
            print(data)
    def _split_array(self,starting_index,array_length):
        print("\n".join(self._data[starting_index:array_length]))
    def _generate_folder(self):
        directory = os.path.join(
        os.getcwd(), 
        datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        os.makedirs(directory)
        return directory
    def _compute(self):
        file_count = round(len(self._data)/self.row_limit)
        self._debug_handler("Number of files that will be generated",file_count)
        files_data  = []
        starting_index = 0
        file_length = self.row_limit
        files_data.append(self._data[starting_index:file_length])

        while (file_length+self.row_limit) < len(self._data):
            starting_index = file_length
            file_length =  file_length + self.row_limit
            files_data.append(self._data[starting_index:file_length])
        files_data.append(self._data[starting_index:len(self._data)])
        return files_data
    def can_split(self):
        if int(len(self._data)/self.row_limit) == 0:
            print("Rows provided in the parameters are greater than rows in the file")
            return False
        return True
    def get_folder_name(self):
        return self._folder_name
    def generate(self):
        files_data = self._compute()
        if len(files_data) > 0:
            self._debug_handler("First Array","\n".join(files_data[0]))
            self._debug_handler("Last array","\n".join(files_data[len(files_data)-1]))
            file_number = 1 
            for file_data in files_data:
                with open(os.path.join(self._folder_name, self.file_name + " - " + str(file_number)) + self.file_extension, 'w') as writer:
                    writer.writelines(file_data)
                file_number = file_number + 1
            return True
        else:
            return False
        
        

