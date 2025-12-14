import os, glob, json 

def convert_into_json(video_folder_path, video_json_file):
    

    if os.path.exists(video_folder_path):
        print('working...')
    else:
        print('not working...')

    video_file_list = []
    for root, dirs, files in os.walk(video_folder_path):
        
        if not root == video_folder_path:
            for file in files:
                if file != 'metadata.csv':
                    filter_video = os.path.join(root, file)

                    json_format = {
                        "video": filter_video
                    }
                    # print(filter_video)
                    video_file_list.append(json_format)

    if os.path.exists(video_json_file):
        print('working...')
    else:
        print('not working...')

    with open(video_json_file, 'w', encoding='utf-8') as f:
        json.dump(video_file_list, f, indent=2)
    print("succesfuly dumps")






if __name__ == "__main__":

    # video_folder_path = "./Data"
    # video_json_file = "./annotation/video_dataset.jsonl"
    # convert_into_json(video_folder_path, video_json_file)
    # ----------------------------------------------------------------------------------------
    # Testing video json 
    # video_folder_path = "./Data"
    video_json_file = "./annotation/sample_video_dataset.jsonl"
    # convert_into_json(video_folder_path, video_json_file)
    # ------------------------------------------------------------------------------
    with open(video_json_file, 'r') as f:
        datas = json.load(f)
        for data in datas:
            print(data['video'])

    

    

    

