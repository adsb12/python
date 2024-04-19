import os

def save_to_file(file_name,jobs):
    f_dir = os.path.dirname(os.path.realpath(__file__)) + f"\\{file_name}.csv"
    file = open(f_dir,"w")
    
    file.write("Position,Company,Location,URL\n")
    
    for job in jobs:
        file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
        
    file.close()