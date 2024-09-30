#Create
def create_records(file):

    with open(file, "wb") as file:
        o_count = 0
        try :
            count = int(input("How many record?: "))
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

#Add
def add_records(file):

    with open(file, "a") as file:
        pass

#Read
def read_records(file) ->str:

    with open(file, "r") as file:
        pass

#Find
def find_records(filePath) ->str:

    with open(file, "r") as file:
        pass

#Remove
def remove_record(filePath):
    
    with open(file, "r") as file:
        pass

#Delete
def delete_record(filePath):
    
    with open(file, "r") as file:
        pass