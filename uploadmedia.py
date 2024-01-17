from helpers.config import Config
import gdown
import glob


def upload_google_media():
   # file_tuple = (_uuid, io.BytesIO(xml_sub))
   # files = {'xml_submission_file': file_tuple}
    config = Config().dest
    q_links = config["question_link"]
    print(q_links)

    for item in q_links:
        print(item)
        for question in item:
            drive_link = item[question]
            gdown.download_folder(drive_link, quiet=True, use_cookies=False)
            submission_attachments_path = "./{question}/*"
            for file_path in glob.glob(submission_attachments_path):
                 filename = os.path.basename(file_path)
                 print(filename, open(file_path, 'rb'))

            #  files[filename] = (filename, open(file_path, 'rb'))


if __name__ == "__main__":
    upload_google_media()